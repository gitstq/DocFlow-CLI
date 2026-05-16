# 🚀 DocFlow-CLI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/Zero%20Dependencies-✓-brightgreen.svg" alt="Zero Dependencies">
  <img src="https://img.shields.io/badge/Platform-Cross--Platform-orange.svg" alt="Cross Platform">
</p>

<p align="center">
  <b>🌐 語言選擇</b> |
  <a href="./README.md">簡體中文</a> |
  <a href="./README_zh_TW.md">繁體中文</a> |
  <a href="./README_en.md">English</a>
</p>

---

## 🎉 專案介紹

**DocFlow-CLI** 是一款輕量級多源文件智慧聚合與轉換工具，靈感來源於對資訊碎片化問題的深度思考。在資訊爆炸的時代，我們每天需要從 RSS、網頁、本地文件等多個來源獲取資訊，而 DocFlow-CLI 正是為了解決這一痛點而生。

### 💡 核心定位

- **多源聚合**：一鍵整合 RSS 訂閱、網頁內容、本地文件
- **智慧處理**：內建 AI 摘要生成與標籤自動提取
- **格式轉換**：支援 Markdown、HTML、JSON 多種輸出格式
- **零依賴**：純 Python 標準庫實現，開箱即用

### ✨ 自研差異化亮點

| 特性 | DocFlow-CLI | 其他工具 |
|------|-------------|----------|
| 依賴數量 | **0** | 通常 5-20+ |
| 資料來源支援 | RSS + 網頁 + 本地文件 | 通常單一來源 |
| AI 摘要 | 內建輕量級實現 | 需呼叫外部 API |
| 標籤提取 | 智慧技術關鍵詞識別 | 通常不支援 |
| 跨平台 | Windows/macOS/Linux | 部分受限 |

---

## ✨ 核心特性

### 📡 多源內容獲取
- **RSS 訂閱解析**：支援 RSS 2.0 和 Atom 格式
- **網頁內容抓取**：智慧提取正文內容
- **本地文件讀取**：支援 Markdown、HTML、TXT、JSON

### 🤖 AI 智慧處理
- **自動摘要生成**：基於內容提取關鍵資訊
- **智慧標籤識別**：自動識別技術關鍵詞（Python、React、AI 等）
- **內容去重優化**：相同來源內容智慧合併

### 📄 多格式輸出
- **Markdown**：適合文件編輯與筆記軟體匯入
- **HTML**：美觀的網頁格式，支援樣式定製
- **JSON**：結構化資料，便於二次開發

### ⚡ 輕量高效
- **零外部依賴**：僅使用 Python 標準庫
- **單文件實現**：核心程式碼僅 500+ 行
- **快速啟動**：無需安裝複雜環境

---

## 🚀 快速開始

### 環境要求

- **Python**: 3.8 或更高版本
- **作業系統**: Windows / macOS / Linux

### 安裝方式

#### 方式一：直接下載使用

```bash
# 克隆倉庫
git clone https://github.com/gitstq/DocFlow-CLI.git
cd DocFlow-CLI

# 直接使用
python docflow.py --help
```

#### 方式二：安裝為系統命令

```bash
# 安裝
pip install -e .

# 全域性使用
docflow --help
```

### 快速使用範例

```bash
# 聚合 RSS 訂閱並輸出 Markdown
python docflow.py -r https://news.ycombinator.com/rss -o output.md

# 抓取網頁內容輸出 HTML
python docflow.py -u https://example.com/article -o article.html -f html

# 批次處理本地 Markdown 文件
python docflow.py -f "./docs/*.md" -o combined.md

# 多源混合聚合
python docflow.py \
  -r https://feeds.feedburner.com/TechCrunch \
  -u https://github.blog/ \
  -f "./notes/*.md" \
  -o daily_digest.md
```

---

## 📖 詳細使用指南

### 命令列參數

```
usage: docflow.py [-h] [-r RSS [RSS ...]] [-u URL [URL ...]]
                  [-f FILE [FILE ...]] -o OUTPUT [-f {md,markdown,html,json}]
                  [--no-summary] [--no-tags] [-v]

🚀 DocFlow-CLI - 輕量級多源文件智慧聚合與轉換工具

可選參數:
  -h, --help            顯示幫助資訊
  -r RSS [RSS ...], --rss RSS [RSS ...]
                        RSS訂閱源URL
  -u URL [URL ...], --url URL [URL ...]
                        網頁URL
  -f FILE [FILE ...], --file FILE [FILE ...]
                        本地文件路徑（支援萬用字元）
  -o OUTPUT, --output OUTPUT
                        輸出檔案路徑（必需）
  -f {md,markdown,html,json}, --format {md,markdown,html,json}
                        輸出格式 (預設: md)
  --no-summary          不包含AI摘要
  --no-tags             不生成標籤
  -v, --version         顯示版本資訊
```

### 典型使用場景

#### 場景一：每日資訊聚合

建立每日技術資訊摘要：

```bash
#!/bin/bash
# daily_news.sh

date_str=$(date +%Y%m%d)

python docflow.py \
  -r "https://news.ycombinator.com/rss" \
  -r "https://www.reddit.com/r/programming/.rss" \
  -o "./daily/news_${date_str}.md"
```

#### 場景二：文件批次轉換

將多個 Markdown 文件合併為一份 HTML 報告：

```bash
python docflow.py \
  -f "./project-docs/**/*.md" \
  -o "./reports/project-documentation.html" \
  -f html
```

#### 場景三：研究資料整理

整合多個來源的研究資料：

```bash
python docflow.py \
  -r "https://arxiv.org/rss/cs.AI" \
  -u "https://openai.com/blog/" \
  -f "./research/*.md" \
  -o "./research/ai-research-collection.json" \
  -f json
```

---

## 💡 設計思路與迭代規劃

### 🎯 設計理念

1. **極簡主義**：保持程式碼簡潔，避免過度工程化
2. **實用優先**：聚焦核心功能，解決真實痛點
3. **零依賴**：減少安裝負擔，提高可移植性
4. **可擴展**：模組化設計，便於功能擴展

### 🏗️ 技術架構

```
┌─────────────────────────────────────────────────────────┐
│                    DocFlow-CLI                          │
├─────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ RSS      │  │ WebPage  │  │ File     │   資料來源層  │
│  │ Fetcher  │  │ Fetcher  │  │ Fetcher  │              │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘              │
│       └─────────────┼─────────────┘                     │
│                     ▼                                   │
│            ┌─────────────────┐                          │
│            │  Document Model │      資料模型層          │
│            └────────┬────────┘                          │
│                     ▼                                   │
│       ┌─────────────────────────┐                       │
│       │    AI Summarizer        │    智慧處理層         │
│       │    - Summary Gen        │                       │
│       │    - Tag Extraction     │                       │
│       └───────────┬─────────────┘                       │
│                   ▼                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ Markdown │  │   HTML   │  │   JSON   │   輸出格式層  │
│  │ Formatter│  │ Formatter│  │ Formatter│              │
│  └──────────┘  └──────────┘  └──────────┘              │
└─────────────────────────────────────────────────────────┘
```

### 📝 迭代規劃

#### v1.1.0 (計劃中)
- [ ] 支援更多 RSS 格式（RSS 1.0, RDF）
- [ ] 新增並發請求支援，提升抓取速度
- [ ] 支援自定義 CSS 樣式模板

#### v1.2.0 (計劃中)
- [ ] 新增設定檔支援（YAML/JSON）
- [ ] 支援資料庫儲存（SQLite）
- [ ] 新增內容去重演算法

#### v2.0.0 (遠期規劃)
- [ ] TUI 互動介面（使用 rich/textual）
- [ ] 外掛系統支援
- [ ] 與主流筆記軟體整合（Notion, Obsidian）

---

## 📦 打包與部署指南

### 本地開發

```bash
# 建立虛擬環境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安裝開發模式
pip install -e .

# 執行測試
python -m pytest tests/
```

### 構建分發包

```bash
# 安裝構建工具
pip install build twine

# 構建原始碼分發包
python -m build

# 上傳到 PyPI (需要許可權)
python -m twine upload dist/*
```

### 單文件可執行版本

使用 PyInstaller 打包為獨立可執行檔案：

```bash
# 安裝 PyInstaller
pip install pyinstaller

# 打包
pyinstaller --onefile --name docflow docflow.py

# 輸出在 dist/ 目錄
```

---

## 🤝 貢獻指南

我們歡迎各種形式的貢獻！請參閱 [CONTRIBUTING.md](./CONTRIBUTING.md) 瞭解詳情。

### 快速開始貢獻

1. **Fork** 本倉庫
2. 建立您的特性分支：`git checkout -b feature/AmazingFeature`
3. **提交** 您的更改：`git commit -m 'feat: 新增某個特性'`
4. **推送** 到分支：`git push origin feature/AmazingFeature`
5. 開啟 **Pull Request**

### 提交規範

我們使用 Angular 提交規範：

- `feat:` 新增功能
- `fix:` 修復問題
- `docs:` 文件更新
- `style:` 程式碼格式調整
- `refactor:` 程式碼重構
- `test:` 測試相關
- `chore:` 構建/工具相關

---

## 📄 開源協議

本專案採用 [MIT License](./LICENSE) 開源協議。

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

## 🙏 致謝

感謝以下開源專案和社群提供的靈感：

- [Hacker News](https://news.ycombinator.com/) - 技術資訊來源
- [qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) - 專案靈感來源

---

<p align="center">
  Made with ❤️ by DocFlow Team
</p>
