# Obsidian Vault Template

This is a template Obsidian vault structure that works well with the MindOS RAG system.

## Structure

```
vault/
├── 00_MindOS/
│   ├── MindOS_Home.md
│   └── Templates/
├── 01_Personal/
├── 02_Family/
├── 03_Work_Career/
├── 04_Trading_Investing/
├── 05_RealEstate/
├── 06_Projects/
├── 07_Knowledge/
├── 08_Health/
├── 09_Creativity_Music/
└── 10_MindOS_System/
```

## Best Practices for RAG

1. **Use Clear Headings** - Headings help with semantic chunking
2. **Add Tags** - Tags improve searchability (#tag format)
3. **Link Documents** - Internal links [[like this]] create connections
4. **Frontmatter** - Add metadata to important documents:

```yaml
---
title: Document Title
tags: [tag1, tag2]
created: 2025-01-01
---
```

5. **Consistent Naming** - Use descriptive file names
6. **Regular Updates** - Keep your vault organized and up-to-date

## Example Document

```markdown
---
title: Trading Strategy Notes
tags: [trading, strategy, psychology]
created: 2025-01-15
---

# Trading Strategy Notes

## Overview

This document outlines my trading approach.

## Key Principles

1. Risk management first
2. Follow the plan
3. Review weekly

## Related

- [[Trading Journal]]
- [[Market Analysis]]
```

