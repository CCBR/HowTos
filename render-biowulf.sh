#!/usr/bin/env bash
# Render from the repository root; additional arguments go to quarto render.
set -eo pipefail

repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$repo_dir"

if ! type module >/dev/null 2>&1; then
    echo "Error: run this script from a shell with the module command available." >&2
    exit 1
fi
module load ccbrpipeliner
module load python/3.11

venv_dir="$repo_dir/.venv-quarto"
if [[ ! -x "$venv_dir/bin/python" ]]; then
    python3.11 -m venv --system-site-packages "$venv_dir"
fi
if ! "$venv_dir/bin/python" -c 'import sys; sys.exit(sys.version_info[:2] != (3, 11))'; then
    echo "Error: .venv-quarto must use Python 3.11. Move it aside and rerun this script." >&2
    exit 1
fi
source "$venv_dir/bin/activate"
export QUARTO_PYTHON="$venv_dir/bin/python"

# Install only when dependencies are missing; reuse the environment thereafter.
if ! "$QUARTO_PYTHON" -c 'import jupyter_core, nbformat, nbconvert, ipykernel, yaml' >/dev/null 2>&1; then
    "$QUARTO_PYTHON" -m pip install jupyter nbconvert pyyaml
fi
"$QUARTO_PYTHON" -c 'from ccbr_tools.github import print_contributor_images'

# Keep Jupyter runtime files in a writable, private local directory.
export JUPYTER_RUNTIME_DIR="$venv_dir/jupyter-runtime"
mkdir -p "$JUPYTER_RUNTIME_DIR"
chmod 700 "$JUPYTER_RUNTIME_DIR"

exec quarto render "$@"
