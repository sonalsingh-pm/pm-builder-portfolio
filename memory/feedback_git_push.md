---
name: feedback_git_push
description: Do not push to GitHub automatically. Only push when user explicitly says "push to GitHub" or "deploy."
metadata:
  type: feedback
---

Do not run `git push` automatically after committing changes.

**Why:** User wants control over when code goes to GitHub and Netlify. Automatic pushes after every change are too aggressive.

**How to apply:** Commit locally as needed. Only push when the user explicitly says "push to GitHub" or "deploy." These are the trigger phrases.
