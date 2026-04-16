# Collaborative GitHub Workflow Documentation

## 1. Repository Initialization
Already completed:

```bash
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Rajeshwarimughilan/Devops_proj.git
git push -u origin main
```

## 2. Configure Branch Protection (`main`)
In GitHub:
1. Open repository -> **Settings** -> **Branches**.
2. Under **Branch protection rules**, click **Add rule**.
3. Branch name pattern: `main`.
4. Enable:
   - `Require a pull request before merging`
   - `Require approvals` (set to `1` or `2`)
   - `Dismiss stale pull request approvals when new commits are pushed`
   - `Require status checks to pass before merging`
   - Select check: `PR Basic Validation`
   - `Restrict who can push to matching branches` (optional but recommended)
5. Save changes.

## 3. Issue Creation and Task Tracking
Use templates under `.github/ISSUE_TEMPLATE/`.
- Create issues for each task/feature/bug.
- Add labels and assignees.
- Use milestones if needed.

Example issue titles:
- `Task: Add API health endpoint`
- `Bug: Fix dashboard rendering on mobile`
- `Feature: Implement JWT auth`

## 4. Pull Request Flow
1. Create issue.
2. Create feature branch.
3. Implement changes and push branch.
4. Open PR using template.
5. Assign reviewer.
6. Reviewer approves or requests changes.
7. After approval + checks, merge PR.

Example branch and PR linkage:

```bash
git checkout -b feature/jwt-auth
# make changes
git add .
git commit -m "feat: implement JWT auth (closes #12)"
git push -u origin feature/jwt-auth
```

In PR description: `Closes #12`.

## 5. Demonstration Plan for Evaluation
Create at least 3 issues and 3 PRs:
1. `docs` change PR
2. `feature` change PR
3. `bugfix` change PR

For each PR, ensure:
- reviewer assigned
- at least 1 approval
- successful check
- merged into `main`

This creates clear evidence of collaborative workflow.

## 6. Evidence to Submit
- Repository URL
- Screenshot or export of branch protection rule
- PR list showing review/approval/merge
- Issues list with status and labels
- This workflow documentation
