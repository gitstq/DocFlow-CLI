# 🚀 DocFlow-CLI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/Zero%20Dependencies-✓-brightgreen.svg" alt="Zero Dependencies">
  <img src="https://img.shields.io/badge/Platform-Cross--Platform-orange.svg" alt="Cross Platform">
</p>

<p align="center">
  <b>🌐 Language</b> |
  <a href="./README.md">简体中文</a> |
  <a href="./README_zh_TW.md">繁體中文</a> |
  <a href="./README_en.md">English</a>
</p>

---

## 🎉 Introduction

**DocFlow-CLI** is a lightweight multi-source document intelligence aggregation and conversion tool, inspired by deep thinking about information fragmentation problems. In the era of information explosion, we need to gather information from multiple sources such as RSS, web pages, and local documents every day. DocFlow-CLI was born to solve this pain point.

### 💡 Core Positioning

- **Multi-source Aggregation**: One-click integration of RSS subscriptions, web content, and local documents
- **Intelligent Processing**: Built-in AI summary generation and automatic tag extraction
- **Format Conversion**: Support for Markdown, HTML, and JSON output formats
- **Zero Dependencies**: Pure Python standard library implementation, ready to use out of the box

### ✨ Differentiation Highlights

| Feature | DocFlow-CLI | Other Tools |
|---------|-------------|-------------|
| Dependencies | **0** | Usually 5-20+ |
| Data Source Support | RSS + Web + Local Files | Usually single source |
| AI Summary | Built-in lightweight implementation | Requires external API calls |
| Tag Extraction | Intelligent tech keyword recognition | Usually not supported |
| Cross-platform | Windows/macOS/Linux | Partially limited |

---

## ✨ Key Features

### 📡 Multi-source Content Fetching
- **RSS Feed Parsing**: Support for RSS 2.0 and Atom formats
- **Web Content Scraping**: Intelligent extraction of main content
- **Local File Reading**: Support for Markdown, HTML, TXT, JSON

### 🤖 AI Intelligent Processing
- **Automatic Summary Generation**: Extract key information based on content
- **Smart Tag Recognition**: Automatically identify tech keywords (Python, React, AI, etc.)
- **Content Deduplication**: Intelligent merging of duplicate content from same sources

### 📄 Multi-format Output
- **Markdown**: Suitable for document editing and note software import
- **HTML**: Beautiful web format with customizable styles
- **JSON**: Structured data for secondary development

### ⚡ Lightweight & Efficient
- **Zero External Dependencies**: Uses only Python standard library
- **Single File Implementation**: Core code is only 500+ lines
- **Quick Start**: No complex environment setup required

---

## 🚀 Quick Start

### Requirements

- **Python**: 3.8 or higher
- **OS**: Windows / macOS / Linux

### Installation

#### Option 1: Direct Download

```bash
# Clone repository
git clone https://github.com/gitstq/DocFlow-CLI.git
cd DocFlow-CLI

# Use directly
python docflow.py --help
```

#### Option 2: Install as System Command

```bash
# Install
pip install -e .

# Use globally
docflow --help
```

### Quick Usage Examples

```bash
# Aggregate RSS feeds and output Markdown
python docflow.py -r https://news.ycombinator.com/rss -o output.md

# Scrape web page content and output HTML
python docflow.py -u https://example.com/article -o article.html -f html

# Batch process local Markdown files
python docflow.py -f "./docs/*.md" -o combined.md

# Multi-source hybrid aggregation
python docflow.py \
  -r https://feeds.feedburner.com/TechCrunch \
  -u https://github.blog/ \
  -f "./notes/*.md" \
  -o daily_digest.md
```

---

## 📖 Detailed Usage Guide

### Command Line Arguments

```
usage: docflow.py [-h] [-r RSS [RSS ...]] [-u URL [URL ...]]
                  [-f FILE [FILE ...]] -o OUTPUT [-f {md,markdown,html,json}]
                  [--no-summary] [--no-tags] [-v]

🚀 DocFlow-CLI - Lightweight Multi-Source Document Intelligence Aggregation & Conversion Tool

Optional arguments:
  -h, --help            Show help message
  -r RSS [RSS ...], --rss RSS [RSS ...]
                        RSS feed URLs
  -u URL [URL ...], --url URL [URL ...]
                        Web page URLs
  -f FILE [FILE ...], --file FILE [FILE ...]
                        Local file paths (supports wildcards)
  -o OUTPUT, --output OUTPUT
                        Output file path (required)
  -f {md,markdown,html,json}, --format {md,markdown,html,json}
                        Output format (default: md)
  --no-summary          Exclude AI summary
  --no-tags             Do not generate tags
  -v, --version         Show version information
```

### Typical Use Cases

#### Case 1: Daily News Aggregation

Create daily tech news digest:

```bash
#!/bin/bash
# daily_news.sh

date_str=$(date +%Y%m%d)

python docflow.py \
  -r "https://news.ycombinator.com/rss" \
  -r "https://www.reddit.com/r/programming/.rss" \
  -o "./daily/news_${date_str}.md"
```

#### Case 2: Document Batch Conversion

Merge multiple Markdown files into one HTML report:

```bash
python docflow.py \
  -f "./project-docs/**/*.md" \
  -o "./reports/project-documentation.html" \
  -f html
```

#### Case 3: Research Material Organization

Integrate research materials from multiple sources:

```bash
python docflow.py \
  -r "https://arxiv.org/rss/cs.AI" \
  -u "https://openai.com/blog/" \
  -f "./research/*.md" \
  -o "./research/ai-research-collection.json" \
  -f json
```

---

## 💡 Design Philosophy & Roadmap

### 🎯 Design Principles

1. **Minimalism**: Keep code clean and avoid over-engineering
2. **Practicality First**: Focus on core features to solve real pain points
3. **Zero Dependencies**: Reduce installation burden and improve portability
4. **Extensibility**: Modular design for easy feature expansion

### 🏗️ Technical Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    DocFlow-CLI                          │
├─────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ RSS      │  │ WebPage  │  │ File     │   Data Source│
│  │ Fetcher  │  │ Fetcher  │  │ Fetcher  │   Layer      │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘              │
│       └─────────────┼─────────────┘                     │
│                     ▼                                   │
│            ┌─────────────────┐                          │
│            │  Document Model │      Data Model Layer    │
│            └────────┬────────┘                          │
│                     ▼                                   │
│       ┌─────────────────────────┐                       │
│       │    AI Summarizer        │    Intelligence Layer  │
│       │    - Summary Gen        │                       │
│       │    - Tag Extraction     │                       │
│       └───────────┬─────────────┘                       │
│                   ▼                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ Markdown │  │   HTML   │  │   JSON   │   Output     │
│  │ Formatter│  │ Formatter│  │ Formatter│   Format Layer│
│  └──────────┘  └──────────┘  └──────────┘              │
└─────────────────────────────────────────────────────────┘
```

### 📝 Roadmap

#### v1.1.0 (Planned)
- [ ] Support more RSS formats (RSS 1.0, RDF)
- [ ] Add concurrent request support for faster fetching
- [ ] Support custom CSS style templates

#### v1.2.0 (Planned)
- [ ] Add configuration file support (YAML/JSON)
- [ ] Support database storage (SQLite)
- [ ] Add content deduplication algorithm

#### v2.0.0 (Long-term)
- [ ] TUI interactive interface (using rich/textual)
- [ ] Plugin system support
- [ ] Integration with popular note-taking software (Notion, Obsidian)

---

## 📦 Packaging & Deployment Guide

### Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Run tests
python -m pytest tests/
```

### Build Distribution Package

```bash
# Install build tools
pip install build twine

# Build source distribution
python -m build

# Upload to PyPI (requires permission)
python -m twine upload dist/*
```

### Single File Executable

Package as standalone executable using PyInstaller:

```bash
# Install PyInstaller
pip install pyinstaller

# Package
pyinstaller --onefile --name docflow docflow.py

# Output in dist/ directory
```

---

## 🤝 Contributing

We welcome all forms of contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

### Quick Start Contributing

1. **Fork** this repository
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. **Commit** your changes: `git commit -m 'feat: Add some AmazingFeature'`
4. **Push** to the branch: `git push origin feature/AmazingFeature`
5. Open a **Pull Request**

### Commit Convention

We use Angular commit convention:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation update
- `style:` Code style adjustment
- `refactor:` Code refactoring
- `test:` Testing related
- `chore:` Build/tooling related

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).

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

## 🙏 Acknowledgments

Thanks to the following open source projects and communities for inspiration:

- [Hacker News](https://news.ycombinator.com/) - Tech news source
- [qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) - Project inspiration source

---

<p align="center">
  Made with ❤️ by DocFlow Team
</p>
