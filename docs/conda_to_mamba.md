---
title: Move from Conda to Mamba
description: "Export Conda environments, uninstall conda, install mamba and rebuild new Mamba environments"
author: "[Vishal Koparde](https://github.com/kopardev)"
---

# Migrating from Anaconda/Miniconda (**conda**) to **Miniforge** (**mamba**)

::: {.callout-important}
This guide migrates your environments away from **Anaconda/Miniconda (conda)** to **Miniforge (mamba)**, using **conda-forge** only (non-commercial) and avoiding `anaconda.org`/`repo.anaconda.com`.  
Steps 1–3 use your existing `conda` to export environments. After uninstall (Step 4) you’ll install **Miniforge** (Step 5) and rebuild environments with **mamba** (Step 9).
:::

---

## Table of Contents

- [Migrating from Anaconda/Miniconda (**conda**) to **Miniforge** (**mamba**)](#migrating-from-anacondaminiconda-conda-to-miniforge-mamba)
  - [Table of Contents](#table-of-contents)
  - [1. List the conda environments](#1-list-the-conda-environments)
  - [2. Download the Python script to fix exported YAML](#2-download-the-python-script-to-fix-exported-yaml)
  - [3. Create **mamba** compatible exported YAML files](#3-create-mamba-compatible-exported-yaml-files)
  - [4. Uninstall conda (Anaconda/Miniconda)](#4-uninstall-conda-anacondaminiconda)
  - [5. Install **mamba** (Miniforge)](#5-install-mamba-miniforge)
  - [6. Clear cache](#6-clear-cache)
  - [7. Enforce strict channel policy](#7-enforce-strict-channel-policy)
  - [8. Verify channel configuration](#8-verify-channel-configuration)
  - [9. Rebuild old env with **mamba**](#9-rebuild-old-env-with-mamba)
  - [Appendix A: `fix_yaml.py`](#appendix-a-fix_yamlpy)


---

## 1. List the conda environments

Use your current **conda** to list environments before migrating.

```bash
conda env list
# or (equivalent)
conda info --envs
```


---

## 2. Download the Python script to fix exported YAML

This script:
- removes duplicate packages,
- drops `prefix:` and other install-specific metadata,
- forces **conda-forge**, **bioconda** and **defaults** as the only channels,
- prepares the file for **mamba** environment creation.


::: {.callout-important}
Copy the script from [**Appendix A**](#appendix-a-fix_yaml.py) into `fix_yaml.py`.
:::

---

## 3. Create **mamba** compatible exported YAML files

Export a single environment named `xyz`:

```bash
conda env export --name xyz | python3 fix_yaml.py - -o xyz.yml
```

::: {.callout-note}
You can export **all** environments at once:
```bash
for env in $(conda env list | awk 'NR>2 && NF {print $1}'); do
  conda env export --name "$env" | python3 fix_yaml.py - -o "${env}.yml"
done
```
:::

::: {.callout-caution}
If you have **path-only** environments (created from arbitrary folders), `conda env list` may show full paths instead of simple names. Consider exporting those individually to ensure correct `name:` in the YAML.
:::

---

## 4. Uninstall conda (Anaconda/Miniconda)

Follow vendor instructions (macOS/Linux):  
<https://www.anaconda.com/docs/getting-started/anaconda/uninstall#macos-or-linux>

Then remove common leftovers:

```bash
# If Miniconda
rm -rf ~/miniconda ~/miniconda3

# If Anaconda
rm -rf ~/anaconda ~/anaconda3

rm -rf ~/.conda
rm -rf ~/.condarc
rm -rf ~/.continuum
rm -rf ~/.conda_envs_dir
rm -rf ~/.conda_envs_dir_test
```

Edit your shell init and delete the `conda init` block:

```text
# >>> conda initialize >>>
...
# <<< conda initialize <<<
```

Files to check (depending on your shell): `~/.zshrc`, `~/.bashrc`, `~/.bash_profile`.

Restart your terminal.

::: {.callout-warning}
Make sure `conda` is no longer on your `PATH`:
```bash
which conda || echo "conda not found (expected)"
```
:::

---

## 5. Install **mamba** (Miniforge)

Download **mamba** for macOS:

```bash
# Apple Silicon (M1/M2/M3):
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge-MacOSX-arm64.sh

# Intel Macs:
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge-MacOSX-x86_64.sh

# Install (interactive)
bash Miniforge-MacOSX-*.sh
```

Verify:

```bash
mamba --version
mamba info | sed -n '1,60p'
```

::: {.callout-note}
Once **mamba** installation is completed then delete the install script.
```bash
rm -f Miniforge-MacOSX-*.sh
```
:::

---

## 6. Clear cache

```bash
# Safe to run; ignores errors if conda is gone
conda clean --all -y || true
mamba clean --all -y || true
```

---

## 7. Enforce strict channel policy

```bash
# Start fresh (ignore error if key doesn't exist)
mamba config remove-key channels 2>/dev/null || true

# Add exactly the three you want
mamba config prepend channels conda-forge
mamba config append  channels bioconda
mamba config append  channels defaults

# Recommended
mamba config set channel_priority strict
```

This:
 - forces to be **conda-forge**, **bioconda** and **defaults** in that order
 - removes any other channels that may point to `anaconda.com`

---

## 8. Verify channel configuration

```bash
# High-level info (shows channel list)
mamba info

# Full config dump
mamba config list | sed -n '1,200p'
```

What you want to **see**:
- `channels` shows only `conda-forge`, `bioconda` and `defaults` 
- **Nothing** should reference `repo.anaconda.com` or `anaconda.org`.


---

## 9. Rebuild old env with **mamba**

Recreate from your cleaned YAMLs:

```bash
# Single env
mamba create -f xyz.yml --yes --override-channels

# All YAMLs in current directory
for y in *.yml *.yaml 2>/dev/null; do
  [ -f "$y" ] || continue
  echo "Rebuilding from $y"
  mamba create -f "$y" --yes --override-channels
done
```

::: {.callout-warning}
During solve, **you should NOT** see:
```
warning  libmamba 'repo.anaconda.com', a commercial channel hosted by Anaconda.com, is used.
```
If you do, revisit **Steps 7–8** to correct your channel configuration.
:::

Activate and test:

```bash
mamba activate xyz
python -V
```

---

## Appendix A: `fix_yaml.py`

::: {.callout-note}
This script reads an exported `conda env export` YAML from **stdin** (or a file), removes duplicates, deletes `prefix:`, forces appropriate channels, removes unwanted channels, preserves `pip:` sections, and writes the cleaned YAML to **stdout** (or `-o FILE`).
:::

```python
#!/usr/bin/env python3
"""
fix_yaml.py
- Normalize an exported conda environment YAML for mamba recreation.
- Drops install-specific fields (prefix), forces conda-forge channels, de-duplicates dependencies.
Usage:
  python3 fix_yaml.py input.yml -o output.yml
  conda env export --name myenv | python3 fix_yaml.py - -o myenv.yml
"""
import sys
import argparse
import io
from collections import OrderedDict

try:
    import yaml  # PyYAML if available
except Exception:
    yaml = None

def load_text(stream):
    return stream.read()

def parse_yaml(text):
    if yaml is None:
        # Minimal fallback: very light parser for a subset of env YAML
        # It preserves lines and does line-level dedup under `dependencies:`.
        # For robust parsing, install PyYAML: mamba install pyyaml
        data = {"_raw": text}
        return data
    return yaml.safe_load(text)

def dump_yaml(data):
    if yaml is None:
        # Fallback: return original text with only simple text transforms
        lines = data["_raw"].splitlines(True)

        out, in_deps, seen, skip_prefix = [], False, set(), False
        for ln in lines:
            if ln.strip().startswith("prefix:"):
                # drop
                continue
            if ln.strip().startswith("channels:"):
                # replace entire channels block with conda-forge only
                out.append("channels:\n  - conda-forge\n")
                skip_prefix = True
                continue
            if skip_prefix:
                # skip original channel lines until a non-channel item appears
                if ln.startswith(" ") or ln.startswith("\t") or ln.strip().startswith("-"):
                    # still channel block; skip
                    continue
                else:
                    skip_prefix = False

            if ln.strip() == "dependencies:":
                in_deps = True
                out.append(ln)
                continue

            if in_deps:
                if ln and ln[0] in " \t":
                    # dependency lines (including 'pip:' sublist)
                    if ln.strip().startswith("- "):
                        dep_item = ln.strip()[2:]
                        # Dedup only top-level conda deps; leave 'pip:' subtree intact
                        if dep_item != "pip:":
                            if dep_item in seen:
                                continue
                            seen.add(dep_item)
                    out.append(ln)
                    continue
                else:
                    in_deps = False
                    out.append(ln)
                    continue
            out.append(ln)
        return "".join(out)

    # PyYAML path (preferred)
    if data is None:
        data = {}
    data.pop("prefix", None)

    # Normalize channels → conda-forge only
    data["channels"] = ["conda-forge"]

    # De-duplicate top-level conda dependencies
    deps = data.get("dependencies", [])
    new_deps = []
    seen = set()

    for item in deps:
        if isinstance(item, str):
            if item not in seen:
                new_deps.append(item)
                seen.add(item)
        elif isinstance(item, dict) and "pip" in item:
            # Keep pip sublist as-is (with de-dup inside)
            pip_list = item.get("pip", [])
            pip_seen = set()
            new_pip = []
            for p in pip_list:
                if p not in pip_seen:
                    new_pip.append(p)
                    pip_seen.add(p)
            new_deps.append({"pip": new_pip})
        else:
            # Unknown structured entry; keep
            new_deps.append(item)

    data["dependencies"] = new_deps

    # Emit YAML
    class OrderedDumper(yaml.SafeDumper):
        pass
    def _dict_representer(dumper, data):
        return dumper.represent_dict(data.items())
    OrderedDumper.add_representer(OrderedDict, _dict_representer)

    return yaml.dump(data, Dumper=OrderedDumper, sort_keys=False)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="Input YAML file or '-' for stdin")
    ap.add_argument("-o", "--output", help="Output YAML file (default: stdout)")
    args = ap.parse_args()

    if args.input == "-":
        text = load_text(sys.stdin)
    else:
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()

    data = parse_yaml(text)
    out = dump_yaml(data)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(out)
    else:
        sys.stdout.write(out)

if __name__ == "__main__":
    main()
```

---


**That’s it!** You’ve exported your old `conda` environments, removed Anaconda/Miniconda, installed **Miniforge**, enforced **conda-forge** only, and rebuilt your environments with **mamba**—without touching `anaconda.org`.
