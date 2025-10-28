# Development Guide

## Package Management with uv

This project uses [uv](https://github.com/astral-sh/uv) for fast, reliable Python package management.

### Common Commands

**Install/sync dependencies:**
```bash
uv sync
```

**Run Python scripts:**
```bash
uv run python script.py
```

**Run Jupyter:**
```bash
uv run jupyter lab
```

**Preview the Quarto blog:**
```bash
quarto preview
```

**Render the blog:**
```bash
quarto render
```

### Adding New Dependencies

Add packages to `pyproject.toml` under `dependencies`, then run:
```bash
uv sync
```

Or add directly:
```bash
uv add package-name
```

### Virtual Environment

The virtual environment is located in `.venv/` and is automatically managed by uv.

**To activate manually (optional):**
```bash
source .venv/bin/activate
```

**Or use uv run for one-off commands:**
```bash
uv run python -c "import pandas; print(pandas.__version__)"
```

## Creating Blog Posts

1. Create a new directory in `posts/` with your post name
2. Create an `index.qmd` file in that directory
3. Use this template:

```markdown
---
title: "Your Post Title"
author: "Your Name"
date: "YYYY-MM-DD"
categories: [category1, category2]
---

Your content here with Python code blocks.
```

4. Preview with `quarto preview`
5. Render final version with `quarto render`
