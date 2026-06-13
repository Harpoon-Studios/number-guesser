# Extension Workflow — Git & GitHub Collaboration

**Audience:** Students who have finished the Number Guesser game  
**Goal:** Create your own extension, share it via GitHub, and play each other's creations

---

## Overview

| Step | What You'll Do | Why |
|------|----------------|-----|
| 1 | Pick an extension idea | Choose what new feature to add |
| 2 | Create a branch | A "sandbox" for your changes so the original stays untouched |
| 3 | Write your extension code | Make the game do something new |
| 4 | Commit your changes | Save a snapshot of your work |
| 5 | Push to GitHub | Upload your branch so others can see it |
| 6 | Open a Pull Request | Ask to have your code reviewed and merged |
| 7 | Review & play each other's PRs | See what everyone built and try their games |

---

## Section 1: Pick an Extension Idea

Look at **Section 10: Challenges** in `lesson_plan.md`. Pick one that
sounds interesting, or invent your own! Some ideas:

- Add a hint system ("very close", "warm", "cold")
- Add difficulty levels (Easy / Medium / Hard)
- Add a score or streak counter
- Add a two-player mode
- Add a timer

**Don't over-scope.** Pick something you can finish in one sitting.

---

## Section 2: Git Basics (What You Need to Know)

You only need **four** git commands for this whole workflow:

| Command | What It Does |
|---------|--------------|
| `git branch <name>` | Creates a new branch |
| `git checkout <name>` | Switches to that branch |
| `git commit` | Saves your changes as a snapshot |
| `git push` | Uploads your branch to GitHub |

Think of a **branch** like a separate save file in a video game.
The main save file (`main` or `master`) is the original game.
Your branch is your own copy where you can experiment freely.

---

## Section 3: Create Your Branch

Open a terminal in the project folder and run:

```bash
# Create a branch with your name or feature name
git branch my-extension

# Switch to your new branch
git checkout my-extension
```

Check that you're now on your branch:

```bash
git branch
```

The branch you're currently on will have an asterisk `*` next to it.

---

## Section 4: Write Your Extension

Open `number_guesser.py` in your editor and start coding your feature.

A few tips:

- **Don't delete the original code.** Add your new code alongside it.
- **Test your changes.** Run the game after each small change:
  ```bash
  python number_guesser.py
  ```
- **If you break something**, don't panic. You can always undo with
  `git checkout -- number_guesser.py` to restore the file.

---

## Section 5: Commit Your Changes

When you've finished a chunk of work (or reached a stopping point),
save it with a commit.

```bash
# See what files you changed
git status

# Stage the file(s) you want to save
git add number_guesser.py

# Commit with a message describing what you did
git commit -m "Add difficulty levels (Easy / Medium / Hard)"
```

**Writing good commit messages:**

| Good | Bad |
|------|-----|
| `"Add hint system: very close, warm, cold"` | `"stuff"` |
| `"Fix bug where negative numbers were accepted"` | `"fix"` |
| `"Add two-player mode with role swap"` | `"Update file"` |

A good message tells someone (including future you) what the change does.

---

## Section 6: Push Your Branch to GitHub

Push your branch to the shared repository:

```bash
git push origin my-extension
```

If this is your first time pushing this branch, git will tell you to set
the upstream. It will show you the exact command — just copy and paste it.

**What happens:** Your branch (with all your commits) gets uploaded to
GitHub. Now anyone with access to the repository can see it.

---

## Section 7: Open a Pull Request (PR)

A Pull Request is a way of saying "here are my changes — please review
them and merge them into the main project."

1. Go to the repository on GitHub in your browser
2. You'll see a yellow banner saying something like
   *"my-extension had recent pushes"* with a **Compare & pull request**
   button — click it
3. If you don't see the banner, click the **Pull requests** tab, then
   **New pull request**, and select your branch
4. Write a short description of what your extension does

**PR description template:**

```
## What I added

[Briefly describe your extension]

## How to test

1. Run `python number_guesser.py`
2. When prompted, choose "Hard" mode
3. You should see...

## Anything else?

[Optional: anything you want reviewers to know]
```

5. Click **Create pull request**

---

## Section 8: View & Review Each Other's PRs

Once everyone has opened their PRs, the whole class can look at them.

### Viewing the code changes

On the PR page, click the **Files changed** tab. You'll see:
- **Green lines** = new code that was added
- **Red lines** = code that was removed
- **Line numbers** on the left — click any line to leave a comment

### How to leave a review comment

1. Hover over a line of code and click the blue `+` icon
2. Type your comment or question
3. Click **Add single comment**

Example comments:
- "Nice use of the `abs()` function here!"
- "What happens if the player enters a letter here?"
- "I like how you reused the existing `check_guess` function"

### How to test someone else's extension

To actually run someone else's code on your own computer:

```bash
# Download their branch
git fetch origin

# Switch to their branch
git checkout their-branch-name

# Play their version
python number_guesser.py

# When you're done, go back to your own branch
git checkout my-extension
```

---

## Section 9: End-of-Week Celebration

At the end of the week:

1. **Browse all open PRs** on the GitHub repository
2. **Read the descriptions** to see what each person built
3. **Check out their branches** and play each game
4. **Leave comments** on things you liked or had questions about
5. **Vote for your favorites** (if your instructor sets up a way to do that)

---

## Reference: Quick Commands Cheat Sheet

```bash
# Create and switch to a new branch
git branch my-feature
git checkout my-feature

# Check what branch you're on
git branch

# See what files changed
git status

# Stage and commit
git add number_guesser.py
git commit -m "Description of your change"

# Push to GitHub
git push origin my-feature

# Pull someone else's branch and switch to it
git fetch origin
git checkout their-feature

# Switch back to main
git checkout main

# Undo changes to a file (restore to last commit)
git checkout -- number_guesser.py
```

---

## Common Problems & Solutions

| Problem | Likely Cause | Fix |
|---------|--------------|-----|
| `git push` says "no upstream" | First time pushing this branch | Use the command git suggests, or `git push -u origin your-branch` |
| `git checkout` says "pathspec did not match" | Typo in branch name | Run `git branch` to list branches, then check the spelling |
| Can't see your PR on GitHub | PR wasn't opened or was closed | Go to Pull Requests tab and check "Closed" tab if needed |
| Merge conflict when pulling | Someone else changed the same lines | Ask the instructor for help resolving it |
