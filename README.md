# Personal Website

A static website built with [Hugo](https://gohugo.io/), a fast and flexible static site generator.

## Prerequisites

- [Hugo](https://gohugo.io/installation/) (extended version recommended)
- Git (for theme management)

## Building

1. Build the site:
   ```bash
   hugo
   ```

2. Preview locally:
   ```bash
   hugo server
   ```
   Then open `http://localhost:1313` in your browser.

3. For production builds with minification:
   ```bash
   hugo --minify
   ```

## Deployment

The site is configured for GitHub Pages. The built site is in the `public/` directory.

### Option 1: GitHub Actions (Recommended)

Create a `.github/workflows/hugo.yml` file with:
```yaml
name: Deploy Hugo site to Pages

on:
  push:
    branches:
      - main

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

defaults:
  runs-on: ubuntu-latest

steps:
  - name: Checkout
    uses: actions/checkout@v4
    with:
      submodules: recursive
      
  - name: Setup Hugo
    uses: peaceiris/actions-hugo@v2
    with:
      hugo-version: 'latest'
      extended: true

  - name: Build
    run: hugo --minify

  - name: Setup Pages
    uses: actions/configure-pages@v4

  - name: Upload artifact
    uses: actions/upload-pages-artifact@v3

  - name: Deploy to GitHub Pages
    id: deployment
    uses: actions/deploy-pages@v4
```

### Option 2: Manual Deployment

1. Build the site: `hugo --minify`
2. Copy the contents of `public/` to your GitHub Pages branch or repository root
3. Commit and push

## File Organization

### Content Files
- `content/_index.md` - Homepage
- `content/games.md` - Open Source projects page
- `content/math.md` - Math/Research page

### Configuration
- `hugo.toml` - Main Hugo configuration file
- `themes/paper/` - The Hugo theme (Paper theme)

### Static Assets
- `static/images/` - Image files
- `static/pdf/` - PDF documents
- `static/css/`, `static/js/`, `static/fonts/` - Legacy assets (if needed)

## Adding a New Page

1. Create a new Markdown file in `content/`:
   ```bash
   hugo new mypage.md
   ```

2. Add it to the navigation menu in `hugo.toml`:
   ```toml
   [[menu.main]]
     identifier = "mypage"
     name = "My Page"
     url = "/mypage/"
     weight = 40
   ```

3. Build and preview: `hugo server`

## Math Support

Mathematical notation is enabled globally using KaTeX. Math can be written inline with `$...$` or as blocks with `$$...$$`.

## Theme

This site uses the [Paper](https://github.com/nanxiaobei/hugo-paper) theme. To update the theme:

```bash
cd themes/paper
git pull
```

## Notes

- The old Python build system (`content/compile.py`) is no longer used
- Old HTML files in `content/` are kept for reference but not used
- Static assets have been moved to the `static/` directory
