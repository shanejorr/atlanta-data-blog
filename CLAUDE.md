# Claude Code Guidelines for Atlanta Data Blog

## Project Overview
This repository contains data analysis projects for a self-hosted blog focused on Georgia, with a heavy emphasis on the greater Atlanta area. Each analysis uses public data to create insightful blog posts.

## Technology Stack
- **Language**: Python 3.11+
- **Package Management**: uv for fast, reliable dependency management
- **Primary Library**: Pandas for data analysis
- **Visualization Library**: Altair for interactive visualizations
- **Publishing Format**: Quarto (.qmd files) with journal theme for self-hosted blog

## Code Standards

### Programming Paradigm
- **Primarily use functional programming** for data analysis
- Write pure functions where possible
- Avoid unnecessary state mutations
- Prefer function composition and data pipelines

### Code Quality
- **Clean code**: Write readable, well-structured code
- **Well-commented**: Add clear comments explaining:
  - What the code does
  - Why certain approaches were chosen
  - Any data-specific nuances or assumptions
  - Sources of data and their context

### Code Organization
- **No repetition within a single analysis**: If code is repeated, extract it into a function
- **Use descriptive function names**: Functions should clearly indicate their purpose
- **Keep functions focused**: Each function should do one thing well

### Project Structure
- **Blog posts**: Created as Quarto documents (.qmd files) in `posts/` directory
  - Each post should be in its own subdirectory (e.g., `posts/post-name/index.qmd`)
- **Quarto configuration**: `_quarto.yml` contains blog settings (theme, navigation, etc.)
- **Homepage**: `index.qmd` with automatic listing of posts
- **Data extraction**: Python scripts (.py) that fetch/process data
- **Data storage**: Extracted data stored in the `data/` folder
- **Each blog post is independent**: Every analysis/blog post should be a separate, self-contained Quarto document
- **No shared code between posts**: Unless explicitly specified, do not create shared utilities or modules
- Each analysis should be runnable on its own

## Data Focus
- **Geographic Scope**: Georgia, with heavy focus on greater Atlanta area
- **Data Sources**: Public data only
- **Analysis Types**: Varied data analysis projects based on available public datasets

## Testing
- **No unit tests required** unless explicitly requested
- Focus on exploratory data analysis and clear, reproducible results

## Workflow

### Creating a New Blog Post
1. **Data extraction**: Create Python scripts to fetch and process raw data
2. **Data storage**: Save extracted/processed data to the `data/` folder
3. **Create post directory**: Make a new folder in `posts/` (e.g., `posts/my-analysis/`)
4. **Create Quarto document**: Add `index.qmd` in the post directory with YAML frontmatter:
   ```yaml
   ---
   title: "Your Post Title"
   author: "Your Name"
   date: "YYYY-MM-DD"
   categories: [category1, category2]
   ---
   ```
5. **Analysis**: In the Quarto document, include:
   - Data loading and cleaning
   - Analysis with clear explanations
   - Interactive visualizations using Altair
   - Well-commented code explaining methodology
6. **Preview**: Run `quarto preview` to see your blog locally
7. **Render**: Run `quarto render` to build the final site

### Package Management
- Use `uv sync` to install/update dependencies
- Add new packages to `pyproject.toml`, then run `uv sync`
- Run Python scripts with `uv run python script.py`
- All code executes in the `.venv` virtual environment managed by uv

## Notes for Claude
- Prioritize code clarity over cleverness
- When extracting functions, use meaningful names that describe the transformation or calculation
- Always include comments about data sources and methodology
- Focus on storytelling through data - the code supports the narrative
- When creating new blog posts, follow the directory structure: `posts/post-name/index.qmd`
- Test blog posts with `quarto preview` before finalizing
- Use Altair for all visualizations to maintain consistency and interactivity
- Ensure all Python code blocks in .qmd files are properly formatted with triple backticks and `{python}` language identifier
