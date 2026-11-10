# Repository Guide for AI Agents

## Runtime and dependencies

- Use Python 3.14, as declared in `.python-version`.
- `requirements.in` is the human-edited dependency source.
- `requirements.txt` is the generated, hash-locked environment. Do not edit it by hand.
- Regenerate the lock with `uv pip compile requirements.in --output-file requirements.txt --generate-hashes --universal --python-version 3.14 --upgrade`.
- Install reproducibly with `python -m pip install --require-hashes -r requirements.txt`.

## Required checks

Run these before opening a pull request:

```text
python -m compileall -q main.py
python -m unittest discover -v
ruff check .
ruff format --check .
pre-commit run --all-files
```

Changes must go through a pull request. Do not push directly to `main`; CI must pass before merging.
