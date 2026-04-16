# Collaborative GitHub Workflow (Phase-Wise)

This repository demonstrates a collaborative development workflow using GitHub for team-based contribution, review, and quality control.

## Objective
Implement a GitHub-based workflow with:
- Repository setup
- Branch protection rules
- Pull request-based code reviews
- Reviewer assignment and approved merges
- Task tracking with GitHub Issues

## Repository
- Remote: https://github.com/Rajeshwarimughilan/Devops_proj
- Default branch: `main`

## Phase-Wise Implementation

### Phase 1: Repository Setup
1. Initialize repository and push `main`.
2. Add workflow documentation and templates.
3. Add contribution guidelines.

### Phase 2: Branching Strategy
1. Keep `main` as protected production branch.
2. Develop features/fixes in short-lived branches:
   - `feature/<name>`
   - `bugfix/<name>`
   - `docs/<name>`

### Phase 3: Quality Gates and Branch Protection
1. Protect `main` with rules:
   - Pull request required before merge
   - At least 1 approving review
   - Dismiss stale approvals on new commits
   - Require status checks to pass
   - Restrict direct pushes to `main`
2. Use CI check from `.github/workflows/pr-check.yml`.

### Phase 4: Pull Request Review Workflow
1. Developer creates branch and commits changes.
2. Open PR into `main` using PR template.
3. Assign reviewers.
4. Reviewer requests changes or approves.
5. Merge only after approval and passing checks.

### Phase 5: Issue-Driven Task Tracking
1. Create tasks as GitHub Issues using templates.
2. Add labels (`bug`, `enhancement`, `task`, `documentation`).
3. Link PRs to issues using `Closes #<issue-number>`.
4. Track progress in Issues and PR timeline.

## Example Git Workflow Commands

```bash
git checkout -b feature/add-workflow-docs
git add .
git commit -m "docs: add collaboration workflow and templates"
git push -u origin feature/add-workflow-docs
```

Create PR on GitHub targeting `main`, assign reviewer(s), and merge after approval.

## Deliverables Mapping
- GitHub repository demonstrating collaboration: this repo and branch strategy
- Pull request history: feature branches merged via reviewed PRs
- Documentation explaining workflow: `README.md`, `CONTRIBUTING.md`, `docs/WORKFLOW.md`

## Suggested Team Roles
- Developer A: raises issues and opens PRs
- Developer B: reviews PRs and approves
- Maintainer: merges approved PRs and manages branch rules

## Next Action
Follow `docs/WORKFLOW.md` to configure branch protection and run the end-to-end demo.
