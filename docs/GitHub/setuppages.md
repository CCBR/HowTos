### GitHub Pages
GitHub [Pages](https://pages.github.com/) is quick and easy way to build static websites for your GitHub repositories. Essentially, you write pages in [Markdown](https://www.markdownguide.org/) which are then rendered to HTML and hosted on GitHub, free of cost! 

CCBR has used GitHub pages to provide extensive, legible and origanized documentation for many of our pipelines:

- [Pipeliner](https://ccbr.github.io/pipeliner-docs/)
- [RNA-seek](https://ccbr.github.io/RNA-seek/)
- [Exome-seek](https://ncipangea.github.io/CCBR_GATK4_Exome_Seq_Pipeline/)
and many others.

We prefer to use [`mkdocs`](https://www.mkdocs.org/) with [Material](https://squidfunk.github.io/mkdocs-material/getting-started/) theme for most of our GitHub Pages websites.

#### Install tools

`mkdocs` and the Material for mkdocs theme can be installed using the following:

```bash
pip install --upgrade pip
pip install mkdocs
pip install mkdocs-material
```

#### Conventions

Generally, for GitHub repos with GitHub pages:

- The repository needs to be public (not private)
- The main/master branch has the markdown documents under a `docs` folder at the root level
- Rendered HTMLs are hosted under a `gh-pages` branch at root level

#### Create website

The following steps can be followed to build your first website 

##### Add `mkdocs.yaml`

`mkdocs.yaml` needs to be added to the root of the **master** branch. Clone the repo. Add the file. 

```bash
% git clone https://github.com/CCBR/xyz.git
% cd xyz
% vi mkdocs.yaml
% git add mkdocs.yaml
% git commit -m "adding mkdocs.yaml"
% git push
```

Here is a sample `mkdocs.yaml`:

```yaml
# Project Information
site_name: CCBR How Tos
site_author: Vishal Koparde, Ph.D.
site_description: >-
  The **DEVIL** is in the **DETAILS**. Step-by-step detailed How To Guides for data management and other CCBR-relevant tasks.

# Repository
repo_name: CCBR/HowTos
repo_url: https://github.com/CCBR/HowTos
edit_uri: https://github.com/CCBR/HowTos/edit/main/docs/

# Copyright
copyright: Copyright &copy; 2022 CCBR

# Configuration
theme:
  name: material
  features:
    - navigation.tabs
    - navigation.top
    - navigation.indexes
    - toc.integrate 
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/toggle-switch-off-outline
        name: Switch to dark mode
    - scheme: slate
      primary: red
      accent: red
      toggle:
        icon: material/toggle-switch
        name: Switch to light mode
  logo: assets/images/doc-book.svg
  favicon: assets/images/favicon.png

# Plugins
plugins:
  - search
  - git-revision-date
  - minify:
      minify_html: true


# Customization
extra:
  social:
    - icon: fontawesome/solid/users
      link: http://bioinformatics.cancer.gov
    - icon: fontawesome/brands/github
      link: https://github.com/CCRGeneticsBranch
    - icon: fontawesome/brands/docker
      link: https://hub.docker.com/orgs/nciccbr/repositories
  version:
    provider: mike


# Extensions
markdown_extensions:
  - markdown.extensions.admonition
  - markdown.extensions.attr_list
  - markdown.extensions.def_list
  - markdown.extensions.footnotes
  - markdown.extensions.meta
  - markdown.extensions.toc:
      permalink: true
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.betterem:
      smart_enable: all
  - pymdownx.caret
  - pymdownx.critic
  - pymdownx.details
  - pymdownx.emoji:
      emoji_index: !!python/name:materialx.emoji.twemoji
      emoji_generator: !!python/name:materialx.emoji.to_svg
  - pymdownx.highlight
  - pymdownx.inlinehilite
  - pymdownx.keys
  - pymdownx.magiclink:
      repo_url_shorthand: true
      user: squidfunk
      repo: mkdocs-material
  - pymdownx.mark
  - pymdownx.smartsymbols
  - pymdownx.snippets:
      check_paths: true
  - pymdownx.superfences
  - pymdownx.tabbed
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.tilde

# Page Tree
nav:
  - Intro : index.md
```

##### Create `index.md`

Create `docs` folder, add your `index.md` there.

```bash
% mkdir docs
% echo "### Testing" > docs/index.md
% git add docs/index.md
% git commit -m "adding landing page"
% git push
```

##### Build site

`mkdocs` can now be used to render `.md` to HTML

```bash
% mkdocs build
INFO     -  Cleaning site directory
INFO     -  Building documentation to directory: /Users/kopardevn/Documents/GitRepos/parkit/site
INFO     -  Documentation built in 0.32 seconds
```

The above command creates a local `site` folder which is the root of your "to-be-hosted" website. You can now open the HTMLs in the `site` folder locally to ensure that that HTML is as per you liking. If not, then you can make edits to the `.md` files and rebuild the site.

> **NOTE**: You do not want to push the `site` folder back to GH and hence it needs to be added to `.gitignore` file like so:
> ```bash
> % echo "**/site/*" > .gitignore
> % git add .gitignore
> % git commit -m "adding .gitignore"
> % git push
> ```

##### Deploy site

The following command with auto-create a `gh-pages` branch (if it does not exist) and copy the contents of the `site` folder to the root of that branch. It will also provide you the URL to your newly created website.

```bash
% mkdocs gh-deploy
INFO     -  Cleaning site directory
INFO     -  Building documentation to directory: /Users/kopardevn/Documents/GitRepos/xyz/site
INFO     -  Documentation built in 0.34 seconds
WARNING  -  Version check skipped: No version specified in previous deployment.
INFO     -  Copying '/Users/kopardevn/Documents/GitRepos/xyz/site' to 'gh-pages' branch and pushing to
            GitHub.
Enumerating objects: 51, done.
Counting objects: 100% (51/51), done.
Delta compression using up to 16 threads
Compressing objects: 100% (47/47), done.
Writing objects: 100% (51/51), 441.71 KiB | 4.29 MiB/s, done.
Total 51 (delta 4), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (4/4), done.
remote:
remote: Create a pull request for 'gh-pages' on GitHub by visiting:
remote:      https://github.com/CCBR/xyz/pull/new/gh-pages
remote:
To https://github.com/CCBR/xyz.git
 * [new branch]      gh-pages -> gh-pages
INFO     -  Your documentation should shortly be available at: https://CCBR.github.io/xyz/
```

Done! Now if you point your web browser to the URL from `gh-deploy` command you will see your HTML hosted on GitHub.

