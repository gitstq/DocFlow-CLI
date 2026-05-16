#!/usr/bin/env python3
"""
DocFlow-CLI Setup
"""

from setuptools import setup, find_packages
from pathlib import Path

# 读取README
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding='utf-8') if readme_path.exists() else ""

setup(
    name="docflow-cli",
    version="1.0.0",
    author="DocFlow Team",
    author_email="docflow@example.com",
    description="🚀 轻量级多源文档智能聚合与转换工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/docflow-cli",
    py_modules=["docflow"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
        "Topic :: Text Processing",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "docflow=docflow:main",
        ],
    },
    keywords="document aggregator rss web cli markdown html json",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/docflow-cli/issues",
        "Source": "https://github.com/yourusername/docflow-cli",
    },
)
