# Usage

---

## Setup your IDE/Editor

![pycharm](images/pycharm.png)  ![vim](images/vim.png)  ![vscode](images/vscode.png)
![sublime](images/sublime.png)  ![emacs](images/emacs.png)  ![atom](images/atom.png)

---

## Install pre-commit hook

```bash
pre-commit install
git add .
```

Note:
- You can configure pre-commit to use any sort of hooks, pre/post push, pre/post message, etc.
- pre-commit runs only for the staged files, not the entire project. And only relevant linters/formatters are applied.

---

![git commit](images/git_commit.png)


---

## Continuous Integration

```bash
pre-commit run --all-files
```

Note:
Devs can skip hooks with `git commit --no-verify`.
