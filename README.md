# 🚀 DocFlow-CLI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/Zero%20Dependencies-✓-brightgreen.svg" alt="Zero Dependencies">
  <img src="https://img.shields.io/badge/Platform-Cross--Platform-orange.svg" alt="Cross Platform">
</p>

<p align="center">
  <b>🌐 语言选择</b> |
  <a href="./README.md">简体中文</a> |
  <a href="./README_zh_TW.md">繁體中文</a> |
  <a href="./README_en.md">English</a>
</p>

---

## 🎉 项目介绍

**DocFlow-CLI** 是一款轻量级多源文档智能聚合与转换工具，灵感来源于对信息碎片化问题的深度思考。在信息爆炸的时代，我们每天需要从 RSS、网页、本地文件等多个来源获取信息，而 DocFlow-CLI 正是为了解决这一痛点而生。

### 💡 核心定位

- **多源聚合**：一键整合 RSS 订阅、网页内容、本地文档
- **智能处理**：内置 AI 摘要生成与标签自动提取
- **格式转换**：支持 Markdown、HTML、JSON 多种输出格式
- **零依赖**：纯 Python 标准库实现，开箱即用

### ✨ 自研差异化亮点

| 特性 | DocFlow-CLI | 其他工具 |
|------|-------------|----------|
| 依赖数量 | **0** | 通常 5-20+ |
| 数据源支持 | RSS + 网页 + 本地文件 | 通常单一来源 |
| AI 摘要 | 内置轻量级实现 | 需调用外部 API |
| 标签提取 | 智能技术关键词识别 | 通常不支持 |
| 跨平台 | Windows/macOS/Linux | 部分受限 |

---

## ✨ 核心特性

### 📡 多源内容获取
- **RSS 订阅解析**：支持 RSS 2.0 和 Atom 格式
- **网页内容抓取**：智能提取正文内容
- **本地文件读取**：支持 Markdown、HTML、TXT、JSON

### 🤖 AI 智能处理
- **自动摘要生成**：基于内容提取关键信息
- **智能标签识别**：自动识别技术关键词（Python、React、AI 等）
- **内容去重优化**：相同来源内容智能合并

### 📄 多格式输出
- **Markdown**：适合文档编辑与笔记软件导入
- **HTML**：美观的网页格式，支持样式定制
- **JSON**：结构化数据，便于二次开发

### ⚡ 轻量高效
- **零外部依赖**：仅使用 Python 标准库
- **单文件实现**：核心代码仅 500+ 行
- **快速启动**：无需安装复杂环境

---

## 🚀 快速开始

### 环境要求

- **Python**: 3.8 或更高版本
- **操作系统**: Windows / macOS / Linux

### 安装方式

#### 方式一：直接下载使用

```bash
# 克隆仓库
git clone https://github.com/gitstq/DocFlow-CLI.git
cd DocFlow-CLI

# 直接使用
python docflow.py --help
```

#### 方式二：安装为系统命令

```bash
# 安装
pip install -e .

# 全局使用
docflow --help
```

### 快速使用示例

```bash
# 聚合 RSS 订阅并输出 Markdown
python docflow.py -r https://news.ycombinator.com/rss -o output.md

# 抓取网页内容输出 HTML
python docflow.py -u https://example.com/article -o article.html -f html

# 批量处理本地 Markdown 文件
python docflow.py -f "./docs/*.md" -o combined.md

# 多源混合聚合
python docflow.py \
  -r https://feeds.feedburner.com/TechCrunch \
  -u https://github.blog/ \
  -f "./notes/*.md" \
  -o daily_digest.md
```

---

## 📖 详细使用指南

### 命令行参数

```
usage: docflow.py [-h] [-r RSS [RSS ...]] [-u URL [URL ...]]
                  [-f FILE [FILE ...]] -o OUTPUT [-f {md,markdown,html,json}]
                  [--no-summary] [--no-tags] [-v]

🚀 DocFlow-CLI - 轻量级多源文档智能聚合与转换工具

可选参数:
  -h, --help            显示帮助信息
  -r RSS [RSS ...], --rss RSS [RSS ...]
                        RSS订阅源URL
  -u URL [URL ...], --url URL [URL ...]
                        网页URL
  -f FILE [FILE ...], --file FILE [FILE ...]
                        本地文件路径（支持通配符）
  -o OUTPUT, --output OUTPUT
                        输出文件路径（必需）
  -f {md,markdown,html,json}, --format {md,markdown,html,json}
                        输出格式 (默认: md)
  --no-summary          不包含AI摘要
  --no-tags             不生成标签
  -v, --version         显示版本信息
```

### 典型使用场景

#### 场景一：每日资讯聚合

创建每日技术资讯摘要：

```bash
#!/bin/bash
# daily_news.sh

date_str=$(date +%Y%m%d)

python docflow.py \
  -r "https://news.ycombinator.com/rss" \
  -r "https://www.reddit.com/r/programming/.rss" \
  -o "./daily/news_${date_str}.md"
```

#### 场景二：文档批量转换

将多个 Markdown 文件合并为一份 HTML 报告：

```bash
python docflow.py \
  -f "./project-docs/**/*.md" \
  -o "./reports/project-documentation.html" \
  -f html
```

#### 场景三：研究资料整理

整合多个来源的研究资料：

```bash
python docflow.py \
  -r "https://arxiv.org/rss/cs.AI" \
  -u "https://openai.com/blog/" \
  -f "./research/*.md" \
  -o "./research/ai-research-collection.json" \
  -f json
```

---

## 💡 设计思路与迭代规划

### 🎯 设计理念

1. **极简主义**：保持代码简洁，避免过度工程化
2. **实用优先**：聚焦核心功能，解决真实痛点
3. **零依赖**：减少安装负担，提高可移植性
4. **可扩展**：模块化设计，便于功能扩展

### 🏗️ 技术架构

```
┌─────────────────────────────────────────────────────────┐
│                    DocFlow-CLI                          │
├─────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ RSS      │  │ WebPage  │  │ File     │   数据源层   │
│  │ Fetcher  │  │ Fetcher  │  │ Fetcher  │              │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘              │
│       └─────────────┼─────────────┘                     │
│                     ▼                                   │
│            ┌─────────────────┐                          │
│            │  Document Model │      数据模型层          │
│            └────────┬────────┘                          │
│                     ▼                                   │
│       ┌─────────────────────────┐                       │
│       │    AI Summarizer        │    智能处理层         │
│       │    - Summary Gen        │                       │
│       │    - Tag Extraction     │                       │
│       └───────────┬─────────────┘                       │
│                   ▼                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ Markdown │  │   HTML   │  │   JSON   │   输出格式层  │
│  │ Formatter│  │ Formatter│  │ Formatter│              │
│  └──────────┘  └──────────┘  └──────────┘              │
└─────────────────────────────────────────────────────────┘
```

### 📝 迭代规划

#### v1.1.0 (计划中)
- [ ] 支持更多 RSS 格式（RSS 1.0, RDF）
- [ ] 添加并发请求支持，提升抓取速度
- [ ] 支持自定义 CSS 样式模板

#### v1.2.0 (计划中)
- [ ] 添加配置文件支持（YAML/JSON）
- [ ] 支持数据库存储（SQLite）
- [ ] 添加内容去重算法

#### v2.0.0 (远期规划)
- [ ] TUI 交互界面（使用 rich/textual）
- [ ] 插件系统支持
- [ ] 与主流笔记软件集成（Notion, Obsidian）

---

## 📦 打包与部署指南

### 本地开发

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装开发模式
pip install -e .

# 运行测试
python -m pytest tests/
```

### 构建分发包

```bash
# 安装构建工具
pip install build twine

# 构建源码分发包
python -m build

# 上传到 PyPI (需要权限)
python -m twine upload dist/*
```

### 单文件可执行版本

使用 PyInstaller 打包为独立可执行文件：

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包
pyinstaller --onefile --name docflow docflow.py

# 输出在 dist/ 目录
```

---

## 🤝 贡献指南

我们欢迎各种形式的贡献！请参阅 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解详情。

### 快速开始贡献

1. **Fork** 本仓库
2. 创建您的特性分支：`git checkout -b feature/AmazingFeature`
3. **提交** 您的更改：`git commit -m 'feat: 添加某个特性'`
4. **推送** 到分支：`git push origin feature/AmazingFeature`
5. 打开 **Pull Request**

### 提交规范

我们使用 Angular 提交规范：

- `feat:` 新增功能
- `fix:` 修复问题
- `docs:` 文档更新
- `style:` 代码格式调整
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建/工具相关

---

## 📄 开源协议

本项目采用 [MIT License](./LICENSE) 开源协议。

```
MIT License

Copyright (c) 2025 DocFlow-CLI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 致谢

感谢以下开源项目和社区提供的灵感：

- [Hacker News](https://news.ycombinator.com/) - 技术资讯来源
- [qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) - 项目灵感来源

---

<p align="center">
  Made with ❤️ by DocFlow Team
</p>
