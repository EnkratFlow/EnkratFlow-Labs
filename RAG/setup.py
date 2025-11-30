"""Setup script for MindOS RAG System"""

from setuptools import setup, find_packages

setup(
    name="mindos-rag",
    version="0.1.0",
    description="Personal RAG system for semantic search across all data sources",
    author="Guy Roberts",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "llama-index>=0.10.0",
        "chromadb>=0.4.22",
        "openai>=1.12.0",
        "pypdf>=4.0.1",
        "markdown>=3.5.2",
        "python-dotenv>=1.0.1",
        "pyyaml>=6.0.1",
        "tqdm>=4.66.1",
        "python-frontmatter>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "mindos-rag=cli:main",
        ],
    },
    python_requires=">=3.10",
)

