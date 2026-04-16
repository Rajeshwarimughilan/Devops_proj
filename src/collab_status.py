"""Utility to summarize collaboration workflow status."""

from dataclasses import dataclass


@dataclass
class WorkflowSummary:
    open_issues: int
    open_prs: int
    merged_prs: int

    def completion_rate(self) -> float:
        total = self.open_prs + self.merged_prs
        if total == 0:
            return 0.0
        return round((self.merged_prs / total) * 100, 2)


def build_status_message(summary: WorkflowSummary) -> str:
    return (
        f"Open issues: {summary.open_issues} | "
        f"Open PRs: {summary.open_prs} | "
        f"Merged PRs: {summary.merged_prs} | "
        f"PR completion: {summary.completion_rate()}%"
    )


if __name__ == "__main__":
    demo = WorkflowSummary(open_issues=3, open_prs=1, merged_prs=2)
    print(build_status_message(demo))
