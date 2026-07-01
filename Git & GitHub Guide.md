# Git & GitHub Guide — For Students Who've Never Used Either

Read this on your own before Week 1's weekend assignment is due — you need it to actually submit your work. It assumes zero prior experience.

## 1. Why we're using this at all

Two completely separate tools, often confused because they're used together:

- **Git** is a program installed on *your computer* that tracks changes to your files over time — like an infinite, detailed "undo history" you control manually, one deliberate checkpoint at a time.
- **GitHub** is a *website* that stores a copy of that history online, so you have a backup, and so your instructor can see it.

You are not being asked to "learn version control" as a side skill — in this course, **Git/GitHub is simply how you turn in your work.** There is no other submission mechanism.

## 2. Core vocabulary (read this once, refer back as needed)

| Term | What it actually means |
|---|---|
| **Repository ("repo")** | A project folder that Git is tracking. Has a hidden `.git` folder inside it holding the entire history. |
| **Commit** | A saved checkpoint of your files at a moment in time, with a short message describing what changed. Like a save-point in a game — you can always come back to it. |
| **Stage / `add`** | Telling Git *which* changed files you want included in your *next* commit. You stage first, then commit. |
| **Push** | Uploading your local commits to GitHub (the website), so they're backed up and visible online. |
| **Pull** | Downloading commits from GitHub down to your computer — the reverse of push. |
| **Clone** | Downloading a full copy of a GitHub repo onto your computer for the first time, including its entire history. |
| **Fork** | Making your own personal copy of *someone else's* GitHub repo, under your own account, that you fully own and can push to. This is how you'll get your own copy of the course repo. |
| **Remote** | A saved nickname for a GitHub URL, so you don't have to type the full URL every time. `origin` is the default name for "my fork." |

The everyday loop you'll actually use, over and over, all course long:

```
edit files  →  git add  →  git commit  →  git push
```

Everything else in this doc is one-time setup or occasional maintenance around that four-step loop.

---

## 3. One-Time Setup

### 3.1 Create a GitHub account
Go to `github.com` and sign up, if you haven't already. Use an email you actually check.

### 3.2 Install Git
- **Windows:** download "Git for Windows" from `git-scm.com` — this also gives you "Git Bash," a terminal that behaves consistently with what's shown below.
- **macOS:** open a terminal and type `git --version` — macOS usually prompts you to install developer tools automatically if it's missing.
- **Linux:** `sudo apt install git` (or your distro's equivalent) if `git --version` doesn't already work.

### 🔴 CHECK YOUR INSTALL
```bash
git --version
```
You should see something like `git version 2.43.0`. If you get "command not found," installation didn't complete — fix this before continuing.

### 3.3 Tell Git who you are (once, ever, per computer)
Git stamps every commit with a name and email. Set this once:

```bash
git config --global user.name "Your Full Name"
git config --global user.email "the-email-you-used-for-github@example.com"
```

**Use the same email as your GitHub account.** If they don't match, your commits will still work, but GitHub won't visually credit them to your profile — which matters, since your commit history is part of how your instructor sees your work.

### 3.4 Set up authentication
GitHub no longer accepts your plain password for `git push`/`git clone` over the command line. Pick **one** of these — Option A is simpler to set up:

**Option A — Personal Access Token (recommended for this course)**
1. On GitHub: click your profile photo → **Settings** → **Developer settings** (bottom of left sidebar) → **Personal access tokens** → **Tokens (classic)** → **Generate new token**.
2. Give it a name (e.g., "MIT Python Course"), check the **`repo`** scope, generate it.
3. **Copy the token immediately — GitHub only shows it once.** Save it somewhere private (a password manager, not a public file).
4. The first time you `git push` from a new computer, Git will prompt for a username and password — enter your GitHub **username**, and paste the **token** as the password. Git will remember it afterward (via your OS's credential manager) so you won't be asked every time.

**Option B — SSH keys** (a bit more setup, no token to store)
This is covered in GitHub's own documentation (see References below) — use this if Option A gives you trouble, or if you're already comfortable with SSH from other work.

### ✅ Self-Check
You just generated a token and it disappeared after you closed the popup without copying it. What do you do?
<details><summary>Answer</summary>Generate a new one. Tokens are only ever shown once — there's no way to retrieve a lost one, only revoke and replace it.</details>

---

## 4. Getting Your Own Copy of the Course Repo

You will **not** edit the instructor's repo directly — you don't have permission to, and you shouldn't want to (your work needs to be *yours*, on *your* account, where your instructor can see it's you). Instead, you **fork** it.

### 4.1 Fork it (on the GitHub website)
1. Open the course repo's GitHub page (link will be shared by your instructor).
2. Click **Fork** (top right). Leave the defaults, click **Create fork**.
3. You now have your own copy at `github.com/YOUR-USERNAME/Python-Course-Module` — this is yours. You can push to it freely.

### 🔴 LIVE DEMO — Clone your fork to your computer
Copy your fork's URL from GitHub (click the green **Code** button, copy the HTTPS URL), then:

```bash
git clone https://github.com/YOUR-USERNAME/Python-Course-Module.git
cd Python-Course-Module
```

**What to observe in your terminal:**
- A new folder appears containing every file from the repo, plus a hidden `.git` folder — that hidden folder is the entire history, silently downloaded along with everything else.
- Running `git remote -v` inside this folder shows one remote, named `origin`, pointing at *your* fork — not the instructor's repo.

### ⚠️ Common Pitfalls
- **Editing the instructor's repo directly instead of your fork.** If the URL in your browser doesn't say your own GitHub username, you're in the wrong place.
- **Cloning the same repo into a folder that already has one cloned inside it.** You'll get a confusing `Python-Course-Module/Python-Course-Module` nested mess — always `cd` to check where you are before cloning.

---

## 5. The Weekly Workflow

Every time you finish a session, an exercise, or a project — repeat this exact loop:

```bash
git status                        # see what changed since your last commit
git add path/to/your_file.py      # stage the specific file(s) you changed
git commit -m "Finish exercise 2" # save a checkpoint, with a message describing WHAT changed
git push                          # upload it to your fork on GitHub
```

### 🔴 LIVE DEMO — A realistic sequence

```bash
# You just finished Exercise 1 of the Week 1 assignment.
git status
# -> shows: modified: week-01/assessment/exercises/exercise_1_input_and_casting.py

git add week-01/assessment/exercises/exercise_1_input_and_casting.py
git commit -m "Complete Exercise 1: bakery box packer"
git push
```

**What to observe:**
- `git status` before `add` shows files in red (changed, not staged). After `add`, the same files show in green (staged, ready to commit).
- After `git commit`, `git status` shows "nothing to commit" — the checkpoint is saved *locally*, but **not yet on GitHub** until you `push`.
- After `git push`, refresh your fork's page on GitHub — your new commit and updated file should be visible there. **This is how you confirm it actually worked** — don't just trust the terminal, check the website.

### ⚠️ Common Pitfalls
- **Committing but forgetting to push.** Your work is saved on your computer, but invisible to your instructor — a commit that never gets pushed might as well not exist for grading/review purposes. Get in the habit of pushing immediately after every commit.
- **Using `git add .` carelessly.** The `.` means "everything in this folder," which can accidentally stage files you didn't mean to commit (like a `.venv` folder if you created it somewhere it shouldn't be). Prefer adding specific files/folders by name when unsure, and always run `git status` first to see what you're about to stage.
- **Vague commit messages** like `"update"` or `"asdf"`. Six months from now (or even six days from now), `"Fix withdrawal validation bug"` tells you something; `"update"` tells you nothing. See Section 6 for the standard everyone uses.
- **One giant commit at the very end of the weekend.** Commit in small, meaningful chunks as you go (after each exercise, after each working stage of the ATM project) — not only is this safer (you can always go back to an earlier checkpoint if you break something), it also gives a much more honest picture of your actual process, which is useful raw material for you too.

### ✅ Self-Check
You ran `git commit -m "..."` successfully, closed your laptop, and went to sleep. Is your work backed up on GitHub yet?
<details><summary>Answer</summary>No. Commit only saves the checkpoint locally, on your machine. Nothing reaches GitHub until you also run <code>git push</code>.</details>

---

## 6. Writing Commit Messages That Don't Suck

Your commit history is a diary of your own work — `git log --oneline` on your repo is often the *first* thing anyone (including you, later, hunting for when a bug appeared) looks at. `"update"`, `"asdf"`, and `"final final v2"` are the three most common ways beginners waste that diary. There's a real, widely-used standard — learn it now and it's automatic forever after.

### The Seven Rules (industry standard, not just this course)

1. **Separate subject from body with a blank line.** A commit message can be a one-line summary, or a summary + blank line + a longer explanation — never squeeze both onto one line.
2. **Limit the subject line to ~50 characters.** Short enough to read at a glance in `git log --oneline`. If you need more room, that belongs in the body, not a longer subject.
3. **Capitalize the subject line.** `"Fix withdrawal bug"`, not `"fix withdrawal bug"`.
4. **Do not end the subject line with a period.** It's a headline, not a sentence.
5. **Use the imperative mood.** Write it as a command, as if finishing the sentence *"If applied, this commit will ___."* → `"Fix withdrawal bug"`, not `"Fixed withdrawal bug"` or `"Fixes withdrawal bug"`. This one rule fixes 90% of bad messages on its own.
6. **Wrap the body at ~72 characters per line**, if you write one (most of your commits this course won't need a body — a good subject line is often enough).
7. **Use the body to explain *what and why*, not *how*.** The code diff already shows *how* — nobody needs that repeated in English. What problem existed, and why this fixes it, is what a body is for.

### 🔴 LIVE DEMO — Bad vs. good, in your actual project context

```bash
# Bad -- vague, past tense, tells you nothing six days from now
git commit -m "fixed stuff"
git commit -m "updates"
git commit -m "asdf"

# Good -- imperative mood, specific, ~50 chars, capitalized, no period
git commit -m "Fix off-by-one in PIN attempt counter"
git commit -m "Add balance validation to withdraw option"
git commit -m "Complete Exercise 3: weekly expense tracker"

# Good, WITH a body -- for a commit that needs more explanation than
# the subject line alone can carry
git commit -m "Fix negative balance bug in withdraw option" -m "Withdrawal was subtracting from balance before checking
whether the amount exceeded it. Moved the comparison to
run first, so an invalid withdrawal is rejected before
balance is ever touched."
```

**What to observe:** every "good" example above reads naturally as the second half of *"If applied, this commit will..."* — that's the imperative-mood test, and it's the fastest way to self-check a message before you commit.

### A common variant you'll see in real teams: Conventional Commits

Many real projects (and job postings will assume you've seen this) prefix the subject with a **type**, so `git log` sorts into categories at a glance: `type: description`.

| Prefix | Use for |
|---|---|
| `feat:` | a new feature or capability |
| `fix:` | a bug fix |
| `docs:` | documentation only (like this guide) |
| `refactor:` | restructuring code with no behavior change |
| `test:` | adding or fixing tests |
| `chore:` | maintenance — dependencies, config, `.gitignore`, etc. |

```bash
git commit -m "feat: add deposit option to ATM menu"
git commit -m "fix: prevent balance from going negative on withdraw"
git commit -m "docs: fill in Week 1 reflection log"
```

**This isn't mandatory for this course** — the Seven Rules above are what actually matters and what you'll be using every day. But using prefixes from the start costs nothing extra and is worth the habit.

### ✅ Self-Check
Rewrite these three real bad habits using the rules above:
1. `"changes"`
2. `"Fixed the bug where pin was wrong"`
3. `"more work on atm project also cleaned up some stuff and fixed a typo"`

<details>
<summary><b>Answer</b></summary>

1. Too vague to fix without knowing what changed — the actual lesson: this message is unusable *because* it has no information, no matter how it's reworded. A real one might be `"Add tuple unpacking demo to Module 2"`.
2. `"Fix PIN comparison bug"` — past tense ("Fixed") became imperative ("Fix"), and it's tightened up.
3. This is really **three separate commits** pretending to be one — split them: `"Add withdraw confirmation message"`, `"Remove unused balance variable"`, `"Fix typo in menu prompt"`. If your message needs "also" in it, that's usually a sign you committed more than one logical change at once.

</details>

---

## 7. Getting New Weeks' Content Into Your Fork

Your fork is a snapshot from the moment you forked it. When your instructor adds Week 2, 3, or 4 to the original repo, **your fork does not update automatically.** Before starting a new week, sync it:

### 🔴 LIVE DEMO — Syncing your fork (easiest method)
On your fork's GitHub page, click the **"Sync fork"** button (near the top) → **"Update branch."** This updates your fork *on the website*. Then, on your computer:

```bash
git pull
```

**What to observe:** the new week's folder appears in your local copy, and none of your own previously committed work is touched or overwritten — syncing only *adds* what's new upstream.

### ⚠️ Common Pitfalls
- **Forgetting to sync before starting a new week**, then wondering why `week-02/` doesn't exist in your folder yet.
- **Editing files inside the handbook folders** (`session-1-.../`, `session-2-.../` etc.) directly. Do your own work in the `assessment/` folders and your own additional files — if you edit the instructor's handbook files and then sync later, you may get a **merge conflict** (Git not knowing whose version of a file to keep). Avoiding this entirely is much easier than fixing it as a beginner.

---

## 8. Command Cheat Sheet

| Command | What it does |
|---|---|
| `git status` | Shows what's changed, staged, or untracked — run this constantly, it's free and safe |
| `git add <file>` | Stages a specific file for the next commit |
| `git add .` | Stages everything changed in the current folder — use carefully |
| `git commit -m "message"` | Saves a checkpoint of staged files |
| `git push` | Uploads your commits to your GitHub fork |
| `git pull` | Downloads new commits from GitHub down to your computer |
| `git log --oneline` | Shows your commit history, most recent first |
| `git clone <url>` | Downloads a full copy of a repo for the first time |
| `git remote -v` | Shows which GitHub URL(s) your local repo is connected to |

## 9. Tell your instructor where your fork lives

Once you've forked and pushed your first commit, submit your fork's URL here: **`[instructor: insert your submission form/spreadsheet link here]`**. This is how your work gets found — a fork nobody knows the address of might as well not exist.

## 10. References

- GitHub's own "Hello World" guide — search `docs.github.com` for "Hello World" (their official first-timer walkthrough).
- GitHub Docs — "About forks" and "Fork a repo" (`docs.github.com`, search within their Pull Requests / Collaborating section).
- GitHub Docs — "Managing your personal access tokens" and "Connecting with SSH" (`docs.github.com`, under Authentication).
- Git's own reference — `git-scm.com/docs` — the authoritative command reference if this guide doesn't cover something you hit.
- "How to Write a Git Commit Message" by Chris Beams — the original source of the Seven Rules in Section 6; search for the title, it's one of the most widely cited posts on this topic.
- `conventionalcommits.org` — the full Conventional Commits specification, if you want to go deeper than the `feat:`/`fix:` basics shown here.
