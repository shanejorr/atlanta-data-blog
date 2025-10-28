# Atlanta Metro Data Blog

A self-hosted data analysis blog exploring the Atlanta metropolitan area and Georgia using public datasets. Built with Quarto and featuring interactive visualizations using Altair.

## Technology Stack

- **Python 3.11+** - Data analysis and visualization
- **Pandas** - Data manipulation
- **Altair** - Interactive visualizations
- **Quarto** - Blog publishing with the journal theme
- **uv** - Fast, reliable package management

## Getting Started

### Prerequisites

- [Quarto](https://quarto.org/docs/get-started/) installed
- [uv](https://github.com/astral-sh/uv) installed

### Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   uv sync
   ```

### Development

**Preview the blog locally:**
```bash
quarto preview
```

**Render the blog:**
```bash
quarto render
```

**Run Python scripts:**
```bash
uv run python script.py
```

For detailed development instructions, see [DEVELOPMENT.md](DEVELOPMENT.md).

## Project Structure
```
atlanta-data-blog/
├── _quarto.yml        # Quarto configuration
├── index.qmd          # Blog homepage
├── about.qmd          # About page
├── posts/             # Blog posts (Quarto .qmd files)
├── data/              # Raw and processed datasets
├── outputs/           # Intermediate analysis outputs and tables
├── figures/           # Publication-ready visualizations
├── styles.css         # Custom CSS styling
├── pyproject.toml     # Project dependencies
└── DEVELOPMENT.md     # Development guide
```

## Creating Blog Posts

See [DEVELOPMENT.md](DEVELOPMENT.md) for detailed instructions on creating new blog posts.
