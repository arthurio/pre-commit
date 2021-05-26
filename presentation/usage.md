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
git commit -m "Some bad code"
```

Note:
- You can configure pre-commit to use any sort of hooks, pre/post push, pre/post message, etc.
- pre-commit runs only for the staged files, not the entire project. And only relevant linters/formatters are applied.

---

![git commit failure](images/git_commit_fail.png)

Note:
- Linters only show errors but generally don't fix the issue.
- Formatters automatically fix the code so you'll unstaged changes.
---

![git commit](images/git_commit.png)

---

## Continuous Integration

```bash
pre-commit run --all-files
```

Note:
Devs can skip hooks with `git commit --no-verify`.
