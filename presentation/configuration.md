# Configuration

![ross shush](images/ross_shushing.jpg)

Keep it to a minimum


---

## black


```
# pyproject.toml

[tool.black]
line-length = 120
```

---

## isort

```
# pyproject.toml

[tool.isort]
profile = "black"
line_length = 120
skip_gitignore = true
```

---

## flynt

Nothing to see here 👀 ...

---

## bandit

```
# .bandit

[bandit]
targets: src,tests
skips: B101
```

- [B101 - assert used](https://bandit.readthedocs.io/en/latest/plugins/index.html#complete-test-plugin-listing)

Note:
- ⚠️  Don't confuse the "ini" file **AND/OR** the "yaml" config file. ⚠️
- assert is removed with compiling to optimized byte code.
- Bandit likes to complain about random, use the secrets module instead if you can or silent individual lines with `# nosec: B311`
---

## flake8/flake8-docstrings

```
# .flake8

[flake8]
max_line_length = 120
ignore = W503,D1
docstring-convention = google
```

- W503: Line break occurred before a binary operator
- D1: [Missing docstring](http://www.pydocstyle.org/en/stable/error_codes.html)

Note:
I don't care about missing docstrings as I try to keep them to a minimum. Instead I prefer to rely on explicit variable and function names, as well as type hints.

---

## pre-commit

<span style="font-size: 20px;">
<pre class="code-wrapper"><code class="yaml hljs" style="max-height: none; height: 585px;">
repos:
  - repo: local
    hooks:
      - id: isort
        name: isort
        entry: isort
        types: [python]
        language: python
      - id: flynt
        name: flynt
        entry: flynt
        args: [--fail-on-change]
        types: [python]
        language: python
      - id: black
        name: black
        entry: black
        language: python
        types: [python]
        exclude: node_modules
      - id: flake8
        name: flake8
        entry: flake8
        language: python
        types: [python]
        exclude: .serverless,node_modules
      - id: bandit
        name: bandit
        entry: bandit
        language: python
        types: [python]
        args:  [--ini, .bandit, --recursive]
      - id: mypy
        name: mypy
        entry: mypy
        types: [python]
        language: python
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.0.1
    hooks:
      - id: end-of-file-fixer
        exclude: .*(min.js|min.css|html|svg|css.map|js.map)
      - id: trailing-whitespace
        exclude: .*(md)
</code></pre>
</span>


Note:
Notice that everything is setup as "local" because I keep track of the packages (black, flake8, etc.) in my dev-requirements.in.

---

## Dev requirements


```
# dev-requirements.in

bandit==1.7.0
black==21.4b2
flake8-docstrings==1.6.0
flake8==3.9.1
flynt==0.64
isort==5.8.0
mypy==0.812
pre-commit==2.12.1
```

Note:
We use pip-tools to compile our requirements.txt files with pinned libraries for dependencies.
