---
title: CoPilot CLI
description: "How to install and use GitHub CoPilot CLI"
author: "[Vishal Koparde](https://github.com/kopardev)"
toc-location: right-body
---

:::{.callout-important}

The Copilot CLI has had major changes since this guide was created.
We plan to update this guide to reflect the latest changes, but
in the meantime, please see this issue for more details:
<https://github.com/CCBR/HowTos/issues/46>

:::

# Installing GitHub Copilot CLI (Laptop Setup Only)

> ⚠️ **Note:** These instructions are for **laptop setup only**. Instructions for **Biowulf (HPC)** will follow separately.

GitHub Copilot CLI brings AI assistance directly to your terminal — helping you explain, generate, and optimize shell commands, scripts, or code snippets. It acts like an AI command-line companion, understanding natural language queries and producing executable shell syntax. This guide describes how to install **both** the GitHub CLI extension (`gh copilot`) and the standalone npm Copilot CLI (with `??`-style aliases) within a **single, unified Mamba environment**.

---

## 🧩 Prerequisites

Before proceeding, ensure you have the following:

* ✅ A **GitHub account** with **Copilot CLI access**
  (available via your GitHub Enterprise account)
* ✅ **Mamba or Conda** installed locally
* ✅ A terminal configured for **bash** or **zsh**
* ✅ Internet connectivity (Copilot CLI requires an active connection to GitHub servers)

---

## 🧱 Step 1. Create and Activate a Unified Environment

We’ll create a single environment to house both the GitHub CLI (`gh`) and the Node.js-based Copilot CLI. Using one environment avoids path conflicts and keeps both tools version-synced. You may also use an existing mamba environment on your laptop ... remember to activate it first.

```bash
mamba create -n ghcopilot -c conda-forge gh nodejs -y
mamba activate ghcopilot
```

### Verify Installation

```bash
gh --version
node --version
npm --version
```

Expected output (approximate):

```
gh version 2.63.0 (2025-03-15)
node v20.11.0
npm 10.2.5
```

> 🧠 **Tip:** Using Node.js ≥ 18 ensures ES2022 compatibility and smoother npm package builds.

---

## 🔑 Step 2. Authenticate GitHub CLI

Authenticate GitHub CLI to your personal or enterprise account:

```bash
gh auth login
```

When prompted:

* Choose **GitHub.com**
* Select **HTTPS** as the protocol
* Opt to **Authenticate Git with your GitHub credentials**
* Choose **Login with a web browser** and follow the browser flow ... you may be given a code in the terminal which you should be copy-pasting in the browser

Confirm authentication:

```bash
gh auth status
```

Expected output example:

```
✓ Logged in to github.com as <your_GH_handle> (GitHub Enterprise)
✓ Git operations authenticated for github.com
...
```

---

## ⚙️ Step 3. Install Copilot CLI as a GitHub Extension

The GitHub CLI supports extensions that integrate seamlessly. Copilot CLI is one such extension.

```bash
gh extension install github/gh-copilot
```

Check the installation:

```bash
gh extension list
```

You should see:

```
github/gh-copilot  latest  Copilot for gh CLI
```

Now, test the basic commands:

```bash
gh copilot --help
Your AI command line copilot.

Usage:
  copilot [command]

Examples:

$ gh copilot suggest "Install git"
$ gh copilot explain "traceroute github.com"


Available Commands:
  alias       Generate shell-specific aliases for convenience
  config      Configure options
  explain     Explain a command
  suggest     Suggest a command

Flags:
  -h, --help              help for copilot
      --hostname string   The GitHub host to use for authentication
  -v, --version           version for copilot

Use "copilot [command] --help" for more information about a command.
```
Take a test drive:

```bash
gh copilot suggest "a bash script to compress all .fastq.gz files"

Welcome to GitHub Copilot in the CLI!
version 1.1.1 (2025-06-17)

I'm powered by AI, so surprises and mistakes are possible. Make sure to verify any generated code or suggestions, and share feedback so that we can learn and improve. For more information, see https://gh.io/gh-copilot-transparency

? What kind of command can I help you with?
> generic shell command

Suggestion:

  for file in *.fastq.gz; do
      gzip "$file"
  done

? Select an option  [Use arrows to move, type to filter]
> Copy command to clipboard
  Explain command
  Execute command
  Revise command
  Rate response
  Exit
```

```bash
gh copilot suggest "a command to list all files changed in the last 10 hours"

Welcome to GitHub Copilot in the CLI!
version 1.1.1 (2025-06-17)

I'm powered by AI, so surprises and mistakes are possible. Make sure to verify any generated code or suggestions, and share feedback so that we can learn and improve. For more information, see https://gh.io/gh-copilot-transparency

? What kind of command can I help you with?
> generic shell command

Suggestion:

  find . -type f -mmin -600

? Select an option  [Use arrows to move, type to filter]
> Copy command to clipboard
  Explain command
  Execute command
  Revise command
  Rate response
  Exit
```

---

## 🧠 Step 4. Install Standalone Copilot CLI (via npm)


While the `gh` extension is GitHub-integrated, the standalone Copilot CLI offers a lightweight, shell-native interface. It provides convenient commands such as `??`, `gh?`, and `git?`, which allow you to quickly generate shell commands, GitHub CLI commands, or git commands based on natural language prompts. This makes it easier to automate tasks, discover command-line workflows, and boost productivity directly from your terminal without leaving your development environment.

Install it inside the same environment:

```bash
npm install -g @githubnext/github-copilot-cli
```

Check installation path and version:

```bash
which github-copilot-cli
github-copilot-cli --version
```

Expected output should be something like this:

```
~/mambaforge/envs/ghcopilot/bin/github-copilot-cli
GitHub Copilot CLI version 1.0.8
```

---

## 🔑 Step 5. Authenticate Standalone Copilot CLI

Login to associate your CLI instance with your GitHub account:

```bash
github-copilot-cli auth login
```

This launches a browser window to complete authentication. Again, copy-paste the code in browser.

Confirm login status:

```bash
github-copilot-cli auth status
```

Expected output:

```
✓ Authenticated as <your_github_handle>
...
```

---

## 🧰 Step 6. Enable Shell Aliases (??, gh?, git?)

To enable shortcut-style commands, append the following to your shell configuration file (`~/.bashrc` or `~/.zshrc`):

```bash
eval "$(github-copilot-cli alias -- "$0")"
```

Reload your shell:

```bash
source ~/.zshrc
```

Verify alias activation:

```bash
alias | grep copilot
```

You should see entries such as:

```
alias ??='github-copilot-cli what-the-shell'
alias gh?='github-copilot-cli git-assist'
alias git?='github-copilot-cli explain'
```

---

## 🧪 Step 7. Verify Dual-Mode Copilot Operation

Now, test both integrations:

### Example 1 — Explain a Command

```bash
?? "explain this: find . -type f -name '*.fq.gz' | xargs du -sh"

 ──────────────────── Command ────────────────────

This command finds all files in the current directory and its subdirectories with the extension '.fq.gz' and then calculates and
displays the disk usage (size) of each of those files in a human-readable format.

 ────────────────── Explanation ──────────────────

○ find . -name "*.fq.gz" is used to list files.
  ◆ . specifies that we start the search in the current directory.
  ◆ -name "*.fq.gz" stipulates that we search for files ending in .fq.gz.
○ | xargs du -h means we pass that list of files to xargs which constructs and executes a command using those files as arguments.
  ◆ du is used to calculate disk usage (size) of files.
  ◆ -h specifies that we want the sizes in a human-readable format (e.g., KB, MB, GB).

❯ ✅ Run this command
  📝 Revise query
  ❌ Cancel
```


### Example 2 — Generate a Bash Script

```bash
?? "bash script to count unique reads in all fastq files"

 ──────────────────── Command ────────────────────

for file in *.fastq; do
  awk 'NR % 4 == 2' $file | sort | uniq | wc -l;
done

 ────────────────── Explanation ──────────────────

○ The for loop iterates over a list of items and executes

❯ ✅ Run this command
  📝 Revise query
  ❌ Cancel
```

### Example 3 — Git Workflow Help

```bash
git? "how to undo the last commit but keep changes"

 ──────────────────── Command ────────────────────

git reset --soft HEAD~1

 ────────────────── Explanation ──────────────────

○ git reset resets the current branch to a previous commit.
  ◆ --soft means that we keep any changes made to the files in the working directory.
  ◆ HEAD~1 specifies that we reset to the commit one before the current one.

❯ ✅ Run this command
  📝 Revise query
  ❌ Cancel
```

### Example 4 — Commit information

```bash
git? when was the last commit made

 ──────────────────── Command ────────────────────

git log -1 --pretty=format:"%ad" --date=iso

 ────────────────── Explanation ──────────────────

○ git log is used to show the commit history.
  ◆ -1 specifies that we only want to see the latest commit.
  ◆ --pretty=format:"%ad" specifies that we want to format the output to only show the author date of the commit.
  ◆ --date=iso specifies that we want the date to be in ISO format.

❯ ✅ Run this command
  📝 Revise query
  ❌ Cancel
```

### Example 5 - GitHub Issues in terminal

```bash
gh? list all the issues

 ──────────────────── Command ────────────────────

gh issue list -L 10000

 ────────────────── Explanation ──────────────────

○ gh issue list lists all issues in the current GitHub repository.
  ◆ -L 10000 specifies that we want to list up to 10,000 issues.

❯ ✅ Run this command
  📝 Revise query
  ❌ Cancel
```

---

## 🧰 Step 8. Maintenance and Upgrades

Keep both components up to date:

| Action              | Command                                           |
| ------------------- | ------------------------------------------------- |
| Update `gh-copilot` | `gh extension upgrade github/gh-copilot`          |
| Remove `gh-copilot` | `gh extension remove github/gh-copilot`           |
| Update npm CLI      | `npm update -g @githubnext/github-copilot-cli`    |
| Remove npm CLI      | `npm uninstall -g @githubnext/github-copilot-cli` |

---

## 🧾 Summary Table

| Task                 | Command                                                 |
| -------------------- | ------------------------------------------------------- |
| Create Environment   | `mamba create -n ghcopilot -c conda-forge gh nodejs -y` |
| Activate Environment | `mamba activate ghcopilot`                              |
| Install gh Extension | `gh extension install github/gh-copilot`                |
| Install npm CLI      | `npm install -g @githubnext/github-copilot-cli`         |
| Authenticate         | `gh auth login` / `github-copilot-cli auth login`       |
| Enable Aliases       | `eval "$(github-copilot-cli alias -- "$0")"`            |
| Test Commands        | `gh copilot suggest` / `?? "explain command"`           |

---
