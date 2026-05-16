#!/usr/bin/env python3
"""
DocFlow-CLI 🚀
轻量级多源文档智能聚合与转换工具
Lightweight Multi-Source Document Intelligence Aggregation & Conversion CLI

Author: AI Agent
License: MIT
"""

import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path
from typing import List, Dict, Optional, Callable
from dataclasses import dataclass, asdict
from datetime import datetime
import xml.etree.ElementTree as ET

# Version
__version__ = "1.0.0"


@dataclass
class Document:
    """文档数据模型"""
    title: str
    content: str
    source: str
    url: str
    author: str = ""
    date: str = ""
    tags: List[str] = None
    summary: str = ""

    def __post_init__(self):
        if self.tags is None:
            self.tags = []


class ContentFetcher:
    """内容获取器基类"""

    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.0'
        }

    def fetch(self, url: str) -> str:
        """获取URL内容"""
        try:
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                return response.read().decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"⚠️  获取内容失败: {url} - {e}")
            return ""


class RSSFetcher(ContentFetcher):
    """RSS订阅源获取器"""

    def parse(self, url: str) -> List[Document]:
        """解析RSS feed"""
        content = self.fetch(url)
        if not content:
            return []

        documents = []
        try:
            root = ET.fromstring(content)

            # 处理RSS 2.0
            if root.tag == 'rss':
                channel = root.find('channel')
                if channel is not None:
                    for item in channel.findall('item'):
                        doc = self._parse_rss_item(item, url)
                        if doc:
                            documents.append(doc)

            # 处理Atom
            elif root.tag.endswith('feed'):
                for entry in root.findall('.//{http://www.w3.org/2005/Atom}entry'):
                    doc = self._parse_atom_entry(entry, url)
                    if doc:
                        documents.append(doc)

        except ET.ParseError as e:
            print(f"⚠️  RSS解析失败: {e}")

        return documents

    def _parse_rss_item(self, item: ET.Element, source: str) -> Optional[Document]:
        """解析RSS item"""
        title = item.find('title')
        link = item.find('link')
        desc = item.find('description')
        pub_date = item.find('pubDate')
        author = item.find('author')

        return Document(
            title=title.text if title is not None else "无标题",
            content=desc.text if desc is not None else "",
            source=source,
            url=link.text if link is not None else "",
            author=author.text if author is not None else "",
            date=pub_date.text if pub_date is not None else ""
        )

    def _parse_atom_entry(self, entry: ET.Element, source: str) -> Optional[Document]:
        """解析Atom entry"""
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        title = entry.find('atom:title', ns)
        link = entry.find('atom:link', ns)
        content = entry.find('atom:content', ns)
        summary = entry.find('atom:summary', ns)
        published = entry.find('atom:published', ns)
        author = entry.find('atom:author/atom:name', ns)

        url = link.get('href') if link is not None else ""

        return Document(
            title=title.text if title is not None else "无标题",
            content=content.text if content is not None else (summary.text if summary is not None else ""),
            source=source,
            url=url,
            author=author.text if author is not None else "",
            date=published.text if published is not None else ""
        )


class WebPageFetcher(ContentFetcher):
    """网页内容获取器"""

    def parse(self, url: str) -> Optional[Document]:
        """解析网页内容（简化版）"""
        content = self.fetch(url)
        if not content:
            return None

        # 提取标题
        title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else "无标题"

        # 提取正文（简化处理）
        # 移除script和style标签
        content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.IGNORECASE | re.DOTALL)
        content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.IGNORECASE | re.DOTALL)

        # 提取正文文本
        text = re.sub(r'<[^>]+>', ' ', content)
        text = re.sub(r'\s+', ' ', text).strip()

        # 截取前2000字符作为摘要
        body = text[:2000] if len(text) > 2000 else text

        return Document(
            title=title,
            content=body,
            source=url,
            url=url
        )


class FileFetcher:
    """本地文件获取器"""

    SUPPORTED_EXTENSIONS = {'.md', '.txt', '.html', '.htm', '.json'}

    def parse(self, filepath: str) -> Optional[Document]:
        """解析本地文件"""
        path = Path(filepath)

        if not path.exists():
            print(f"⚠️  文件不存在: {filepath}")
            return None

        if path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            print(f"⚠️  不支持的文件格式: {path.suffix}")
            return None

        try:
            content = path.read_text(encoding='utf-8', errors='ignore')

            return Document(
                title=path.stem,
                content=content,
                source=f"file://{filepath}",
                url=f"file://{filepath}",
                date=datetime.fromtimestamp(path.stat().st_mtime).isoformat()
            )
        except Exception as e:
            print(f"⚠️  读取文件失败: {filepath} - {e}")
            return None


class AISummarizer:
    """AI摘要生成器（模拟）"""

    def generate_summary(self, content: str, max_length: int = 200) -> str:
        """生成内容摘要"""
        # 简单的摘要生成：取前N个句子
        sentences = re.split(r'[。！？.!?]', content)
        summary = ""

        for sentence in sentences:
            if len(summary) + len(sentence) < max_length:
                summary += sentence + "。"
            else:
                break

        return summary if summary else content[:max_length] + "..."

    def extract_tags(self, title: str, content: str) -> List[str]:
        """提取标签"""
        # 简单的关键词提取
        text = (title + " " + content).lower()

        # 技术关键词库
        tech_keywords = {
            'python': 'Python', 'javascript': 'JavaScript', 'typescript': 'TypeScript',
            'rust': 'Rust', 'go': 'Go', 'java': 'Java', 'cpp': 'C++', 'c++': 'C++',
            'react': 'React', 'vue': 'Vue', 'angular': 'Angular', 'svelte': 'Svelte',
            'node': 'Node.js', 'deno': 'Deno', 'bun': 'Bun',
            'docker': 'Docker', 'kubernetes': 'Kubernetes', 'k8s': 'Kubernetes',
            'aws': 'AWS', 'azure': 'Azure', 'gcp': 'GCP', 'cloud': 'Cloud',
            'ai': 'AI', 'ml': 'Machine Learning', 'llm': 'LLM',
            'api': 'API', 'cli': 'CLI', 'ui': 'UI', 'ux': 'UX',
            'git': 'Git', 'github': 'GitHub', 'devops': 'DevOps',
            'database': 'Database', 'sql': 'SQL', 'nosql': 'NoSQL',
            'security': 'Security', 'testing': 'Testing', 'ci/cd': 'CI/CD'
        }

        tags = []
        for keyword, tag in tech_keywords.items():
            if keyword in text and tag not in tags:
                tags.append(tag)

        return tags[:5]  # 最多返回5个标签


class OutputFormatter:
    """输出格式化器"""

    def to_markdown(self, documents: List[Document], include_summary: bool = True) -> str:
        """转换为Markdown格式"""
        lines = ["# 📚 DocFlow 文档聚合\n"]
        lines.append(f"*生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")

        for i, doc in enumerate(documents, 1):
            lines.append(f"\n## {i}. {doc.title}\n")
            lines.append(f"**来源**: [{doc.source}]({doc.url})\n")

            if doc.author:
                lines.append(f"**作者**: {doc.author}\n")
            if doc.date:
                lines.append(f"**日期**: {doc.date}\n")
            if doc.tags:
                lines.append(f"**标签**: {', '.join(doc.tags)}\n")

            lines.append("\n")

            if include_summary and doc.summary:
                lines.append(f"> 📋 **摘要**: {doc.summary}\n\n")

            lines.append(f"{doc.content}\n")
            lines.append("---\n")

        return '\n'.join(lines)

    def to_html(self, documents: List[Document], include_summary: bool = True) -> str:
        """转换为HTML格式"""
        html_parts = [
            "<!DOCTYPE html>",
            "<html lang=\"zh-CN\">",
            "<head>",
            "<meta charset=\"UTF-8\">",
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
            "<title>DocFlow 文档聚合</title>",
            "<style>",
            "body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; }",
            "h1 { color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }",
            "h2 { color: #444; margin-top: 30px; }",
            ".meta { color: #666; font-size: 14px; margin: 10px 0; }",
            ".meta a { color: #007bff; text-decoration: none; }",
            ".tags { margin: 10px 0; }",
            ".tag { display: inline-block; background: #e9ecef; padding: 2px 8px; border-radius: 12px; font-size: 12px; margin-right: 5px; }",
            ".summary { background: #f8f9fa; padding: 15px; border-left: 4px solid #007bff; margin: 15px 0; }",
            ".content { margin: 20px 0; }",
            "hr { border: none; border-top: 1px solid #dee2e6; margin: 30px 0; }",
            "</style>",
            "</head>",
            "<body>",
            f"<h1>📚 DocFlow 文档聚合</h1>",
            f"<p class=\"meta\">生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>"
        ]

        for doc in documents:
            html_parts.append(f"<h2>{doc.title}</h2>")
            html_parts.append(f"<div class=\"meta\"><strong>来源</strong>: <a href=\"{doc.url}\">{doc.source}</a></div>")

            if doc.author:
                html_parts.append(f"<div class=\"meta\"><strong>作者</strong>: {doc.author}</div>")
            if doc.date:
                html_parts.append(f"<div class=\"meta\"><strong>日期</strong>: {doc.date}</div>")

            if doc.tags:
                tags_html = ''.join([f'<span class="tag">{tag}</span>' for tag in doc.tags])
                html_parts.append(f"<div class=\"tags\">{tags_html}</div>")

            if include_summary and doc.summary:
                html_parts.append(f"<div class=\"summary\">📋 <strong>摘要</strong>: {doc.summary}</div>")

            # 简单处理内容为HTML
            content_html = doc.content.replace('\n', '<br>')
            html_parts.append(f"<div class=\"content\">{content_html}</div>")
            html_parts.append("<hr>")

        html_parts.extend(["</body>", "</html>"])

        return '\n'.join(html_parts)

    def to_json(self, documents: List[Document]) -> str:
        """转换为JSON格式"""
        data = {
            "generated_at": datetime.now().isoformat(),
            "count": len(documents),
            "documents": [asdict(doc) for doc in documents]
        }
        return json.dumps(data, ensure_ascii=False, indent=2)


class DocFlowCLI:
    """DocFlow CLI主程序"""

    def __init__(self):
        self.rss_fetcher = RSSFetcher()
        self.web_fetcher = WebPageFetcher()
        self.file_fetcher = FileFetcher()
        self.summarizer = AISummarizer()
        self.formatter = OutputFormatter()

    def run(self):
        """运行CLI"""
        parser = argparse.ArgumentParser(
            description='🚀 DocFlow-CLI - 轻量级多源文档智能聚合与转换工具',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
使用示例:
  %(prog)s -r https://example.com/feed.xml -o output.md
  %(prog)s -u https://example.com/article -o output.html
  %(prog)s -f ./docs/*.md -o output.json
  %(prog)s -r feed.xml -u https://example.com -o combined.md
            """
        )

        parser.add_argument('-r', '--rss', nargs='+', help='RSS订阅源URL')
        parser.add_argument('-u', '--url', nargs='+', help='网页URL')
        parser.add_argument('-f', '--file', nargs='+', help='本地文件路径')
        parser.add_argument('-o', '--output', required=True, help='输出文件路径')
        parser.add_argument('-t', '--format', choices=['md', 'markdown', 'html', 'json'],
                           default='md', help='输出格式 (默认: md)')
        parser.add_argument('--no-summary', action='store_true', help='不包含AI摘要')
        parser.add_argument('--no-tags', action='store_true', help='不生成标签')
        parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

        args = parser.parse_args()

        # 收集所有文档
        all_documents = []

        print("🚀 DocFlow-CLI 开始聚合文档...\n")

        # 处理RSS源
        if args.rss:
            for rss_url in args.rss:
                print(f"📡 正在获取RSS: {rss_url}")
                docs = self.rss_fetcher.parse(rss_url)
                print(f"   ✅ 获取到 {len(docs)} 篇文档")
                all_documents.extend(docs)

        # 处理网页
        if args.url:
            for url in args.url:
                print(f"🌐 正在获取网页: {url}")
                doc = self.web_fetcher.parse(url)
                if doc:
                    print(f"   ✅ 获取成功: {doc.title}")
                    all_documents.append(doc)
                else:
                    print(f"   ❌ 获取失败")

        # 处理本地文件
        if args.file:
            import glob
            for pattern in args.file:
                for filepath in glob.glob(pattern):
                    print(f"📄 正在读取文件: {filepath}")
                    doc = self.file_fetcher.parse(filepath)
                    if doc:
                        print(f"   ✅ 读取成功: {doc.title}")
                        all_documents.append(doc)
                    else:
                        print(f"   ❌ 读取失败")

        if not all_documents:
            print("\n⚠️  未获取到任何文档，请检查输入参数")
            sys.exit(1)

        print(f"\n📊 共获取 {len(all_documents)} 篇文档")

        # 生成AI摘要和标签
        if not args.no_summary or not args.no_tags:
            print("🤖 正在生成AI摘要和标签...")
            for doc in all_documents:
                if not args.no_summary:
                    doc.summary = self.summarizer.generate_summary(doc.content)
                if not args.no_tags:
                    doc.tags = self.summarizer.extract_tags(doc.title, doc.content)

        # 格式化输出
        output_format = args.format.lower()
        if output_format in ['md', 'markdown']:
            content = self.formatter.to_markdown(all_documents, not args.no_summary)
        elif output_format == 'html':
            content = self.formatter.to_html(all_documents, not args.no_summary)
        elif output_format == 'json':
            content = self.formatter.to_json(all_documents)
        else:
            content = self.formatter.to_markdown(all_documents, not args.no_summary)

        # 写入文件
        try:
            output_path = Path(args.output)
            output_path.write_text(content, encoding='utf-8')
            print(f"\n✅ 文档已保存至: {output_path.absolute()}")
        except Exception as e:
            print(f"\n❌ 保存文件失败: {e}")
            sys.exit(1)

        print("\n🎉 文档聚合完成!")


def main():
    """入口函数"""
    cli = DocFlowCLI()
    cli.run()


if __name__ == '__main__':
    main()
