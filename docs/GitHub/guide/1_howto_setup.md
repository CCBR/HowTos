---
date: 2023-04-27
date-modified: 2026-02-09
author: "[Kelly Sovacool](https://github.com/kelly-sovacool)"
---

# GitHub Setup: Preparing the Environment

git is installed by default on macOS and Linux.

You can also optionally install the GitHub CLI for easy access to GitHub-related commands from your terminal.

## GitHub CLI

On macOS you can install the GitHub CLI with homebrew:
```sh
brew install gh
```

For other platforms, see the [github cli installation instructions](https://github.com/cli/cli?tab=readme-ov-file#installation).

### Log in

Log in to GitHub via the CLI and follow the prompts:

```sh
gh auth login
```

## Configure git

On any machine where you use git (e.g. your laptop, biowulf, frce, etc.), you
will need to configure your name and email address.

```{.bash filename="sh"}
git config --global user.name "Firstname Lastname"
git config --global user.email YOUR_EMAIL@example.com
```

Make sure you replace `YOUR_EMAIL@example.com` with the primary email associated
with your GitHub account. For CCBR members, this should be your NIH email i.e.
`firstname.lastname@nih.gov`.

## Authenticating git with GitHub

It is possible to use a personal access token (PAT) to authenticate with GitHub,
but we now recommend using SSH Keys instead. [View the instructions on setting
up SSH keys](/docs/GitHub/authentication) and follow all of the steps before
proceeding.
