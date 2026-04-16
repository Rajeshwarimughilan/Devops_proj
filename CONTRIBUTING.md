# Contributing Guide

## Branch Naming
- `feature/<short-description>`
- `bugfix/<short-description>`
- `docs/<short-description>`

## Commit Message Format
Use concise, scoped messages:
- `feat: add login endpoint`
- `fix: resolve null pointer in parser`
- `docs: update setup instructions`

## Pull Request Rules
1. Every change must come through a PR.
2. PR must reference an Issue.
3. PR must pass all status checks.
4. At least 1 reviewer approval is mandatory.
5. Do not merge your own PR unless explicitly allowed.

## PR Checklist
- [ ] Linked to issue (`Closes #<id>`)
- [ ] Tests/checks passing
- [ ] Documentation updated if required
- [ ] Reviewer assigned

## Code Review Expectations
- Keep PRs small and focused.
- Review for correctness, readability, and regressions.
- Request changes for unresolved issues.

## Merge Strategy
Use **Squash and merge** for clean history unless team agrees otherwise.
