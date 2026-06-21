# Exercism Helper Scripts

Three small Bash helpers that streamline my Exercism workflow. They live in
`~/.local/bin` (on `PATH`) and wrap the `exercism` CLI, `pytest`/CMake, and `git`.

| Script | What it does | Sends to |
| --- | --- | --- |
| [`exercism-get`](#exercism-get) | Download a new exercise and open it in VS Code | — |
| [`exercism-review`](#exercism-review) | Run the tests, then submit if they pass | exercism.org |
| [`exercism-push`](#exercism-push) | Stage, commit, and push the repo | GitHub |

> **Two different "sends":** `exercism-review` submits a solution to **exercism.org**
> (for the track / mentoring). `exercism-push` pushes the repo to **GitHub** (backup /
> portfolio). They are unrelated — one does not trigger the other.

## The workflow

```
exercism-get <exercise>      # 1. download + open
   ↓  (write your solution)
exercism-review <exercise>   # 2. test, then submit to exercism.org
   ↓
exercism-push "message"      # 3. back up to GitHub
```

## Requirements

- `exercism` CLI, configured (`exercism configure`) — workspace is `~/Exercism`
- `python3` + `pytest` (Python tracks)
- `cmake` + a C++ compiler (C++ tracks)
- `git` + `gh`, authenticated, with `origin` set (GitHub pushes)
- `~/.local/bin` on `PATH`

---

## `exercism-get`

Download an exercise, move it into the repo layout (`Execism_Work/<track>/`), and open
the solution file(s) in VS Code.

```
exercism-get <exercise> [-t TRACK] [--force] [--no-open]
```

| Option | Meaning |
| --- | --- |
| `-t TRACK` | Track to download from (default `python`) |
| `--force` | Re-download / overwrite if it already exists |
| `--no-open` | Don't open the files in VS Code |

```bash
exercism-get acronym             # python
exercism-get leap -t cpp         # another track
exercism-get darts --no-open     # download only
```

**Note:** the Exercism CLI downloads to `<workspace>/<track>/`, but this repo keeps
solutions under `<workspace>/Execism_Work/<track>/`. The script moves the exercise into
that layout for you.

---

## `exercism-review`

Run an exercise's tests, then submit it to exercism.org **only if they pass**.

```
exercism-review <exercise> [-t TRACK] [--dry-run] [--force] [--no-test]
```

| Option | Meaning |
| --- | --- |
| `-t TRACK` | Track (default `python`) |
| `--dry-run` | Run tests, show what would be submitted, submit nothing |
| `--force` | Submit even if tests fail |
| `--no-test` | Skip tests and submit |

```bash
exercism-review acronym              # test + submit
exercism-review leap -t cpp          # C++ (CMake + Catch2)
exercism-review hamming --dry-run    # check without submitting
```

- **Python** runs `pytest`.
- **C++** does a clean CMake build (`-DEXERCISM_RUN_ALL_TESTS=1`) and runs the Catch2 binary.
- Solution files are read from each exercise's `.exercism/config.json`, so the right
  files are submitted automatically (test files are never submitted).

---

## `exercism-push`

Stage, commit, and push the whole repo to GitHub in one step. A convenience wrapper
around `git` — **not** an Exercism command.

```
exercism-push [commit message...]
exercism-push --dry-run
```

| Form | Meaning |
| --- | --- |
| `exercism-push "solved hamming"` | Commit with that message, then push |
| `exercism-push` | Commit with a dated default message, then push |
| `exercism-push --dry-run` | Show the changes and what would happen; change nothing |

```bash
exercism-push "solved hamming"
exercism-push --dry-run
```

- Won't make an **empty commit** — a clean tree just prints "Nothing to commit."
- Finds the repo from the Exercism config, so it works from any directory.

---

## Gotcha: case-sensitive submit paths

The Exercism CLI compares the submit path against the configured workspace
**case-sensitively**. The workspace is configured as `/Users/jp/Exercism` (capital `E`),
but the path can resolve through lowercase `/Users/jp/exercism`; macOS treats them as the
same folder, but the CLI rejects the mismatch. All three scripts avoid this by reading
the workspace from `exercism configure` and building paths from that exact casing.
