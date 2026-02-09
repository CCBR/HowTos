---
author: "[Samantha Sevilla](https://github.com/slsevilla) & [Ned Cauley](https://github.com/escauley)"
date: 2023-11-01
date-modified: 2025-12-12
---

# GitHub HowTo: Pre-Commit

Pre-commit should be added to all GitHub repositories on Biowulf and any clones created elsewhere to ensure cohesive and informative commit messages. After the creating the repository the following commands should be run in order to initialize the pre-commit hook, and establish the following requirements for all commit messages:

## Using Precommit
Pre-commit has been installed as a module on Biowulf. Set up an interactive session, and follow the steps below. A pre-commit configuration file is needed, and can be copied from the [CCBR template repo](https://github.com/CCBR/CCBR_NextflowTemplate/blob/main/.pre-commit-config.yaml).
```
# load module on biowulf
module load precommit

# CD into the GitHub repo
cd <repo_name>

# install precommit in the repo - this is the only time you need to do this, per local repo location
pre-commit install

# copy and update the precommit config
touch .pre-commit.config
```

## Structure of Commit Messages
Commits must follow the format listed below, as designated by [Angular](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines):
```
<type>(<scope>): <subject>
<body>
<BLANK LINE>
<footer>
```

### Type (REQUIRED)
The `type` must be one of the following options:

- feat: A new feature
- fix: A bug fix
- docs: Documentation only changes
- perf: A code change that improves performance
- style: Style changes that do not affect the meaning of the code (white-space, formatting, etc.)
- test: Adding tests or correcting existing tests
- ci: Changes to our CI configuration files and scripts
- build: Changes that affect the build system or external dependencies
- refactor: A code change that neither fixes a bug nor adds a feature, such as to improve code understandability
- chore: Maintenance tasks that don't affect production code behavior (e.g. configuration files)

`feat`, `fix`, `docs`, and `perf` changes are user-facing changes because they affect users of the code, and should be included in the changelog.
All other types are non user-facing changes and typically do not need to be included in the changelog.

### Scope (OPTIONAL)
The `scope` must be one of the following options:

- animations
- common
- compiler
- compiler-cli
- core
- elements
- forms
- http
- language-service
- platform-browser
- platform-browser-dynamic
- platform-server
- platform-webworker
- platform-webworker-dynamic
- router
- service-worker
- upgrade

### Subject (REQUIRED)
The `subject` must be a succinct description of the change. It should follow the following rules:

- use the imperative, present tense: "change" not "changed" nor "changes"
- don't capitalize the first letter
- no dot (.) at the end

### Body (OPTIONAL)
The `body` should include the motivation for the change and contrast this with previous behavior. It should follow the following rule:

- use the imperative, present tense: "change" not "changed" nor "changes"

### Footer (OPTIONAL)
The `footer` should contain any information about `Breaking Changes` and is also the place to reference GitHub issues that this commit Closes.

- [Breaking Changes](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#heading=h.uyo6cb12dt6w) should start with the word BREAKING CHANGE: with a space or two newlines. The rest of the commit message is then used for this.
- `Closed bugs` should be listed on a separate line in the footer from `Breaking Changes`, prefixed with "Closes" keyword (Closes #234
or Closes #123, #245, #992).

### Examples
Below are some examples of properly formatted commit messages
```
# example
docs(changelog): update changelog to beta.5

# example
fix(release): need to depend on latest rxjs and zone.js

# example
feat($browser): onUrlChange event (popstate/hashchange/polling)
Added new event to $browser:
- forward popstate event if available
- forward hashchange event if popstate not available
- do polling when neither popstate nor hashchange available

Breaks $browser.onHashChange, which was removed (use onUrlChange instead)

# example
fix($compile): couple of unit tests for IE9
Older IEs serialize html uppercased, but IE9 does not...
Would be better to expect case insensitive, unfortunately jasmine does
not allow to user regexps for throw expectations.

Closes #392
Breaks foo.bar api, foo.baz should be used instead
```
