---
date-modified: 2026-02-09
author: "[Kelly Sovacool](https://github.com/kelly-sovacool)"
---

# GitHub Setup: Preparing the Environment

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

## Authentication

It is possible to use a personal access token (PAT) to authenticate, but we now
recommend using SSH Keys instead. [View the instructions on setting up SSH
keys](/docs/GitHub/authentication) and follow all of the steps before
proceeding.
