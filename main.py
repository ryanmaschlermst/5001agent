import argparse
from workflow import Workflow


def main():
    parser = argparse.ArgumentParser(prog="agent")
    sub = parser.add_subparsers(dest="command", required=True)

    # review
    review = sub.add_parser("review")
    review.add_argument("--range", required=True)

    # draft
    draft = sub.add_parser("draft")
    draft_sub = draft.add_subparsers(dest="kind", required=True)

    issue = draft_sub.add_parser("issue")
    issue.add_argument("--instruction", required=True)

    pr = draft_sub.add_parser("pr")
    pr.add_argument("--range", required=True)

    # approve
    approve = sub.add_parser("approve")
    group = approve.add_mutually_exclusive_group(required=True)
    group.add_argument("--yes", action="store_true")
    group.add_argument("--no", action="store_true")

    # improve
    improve = sub.add_parser("improve")
    improve_sub = improve.add_subparsers(dest="kind", required=True)

    issue_imp = improve_sub.add_parser("issue")
    issue_imp.add_argument("--number", required=True)

    pr_imp = improve_sub.add_parser("pr")
    pr_imp.add_argument("--range", required=True)

    args = parser.parse_args()
    workflow = Workflow()

    if args.command == "review":
        workflow.review(args.range)

    elif args.command == "draft":
        if args.kind == "issue":
            workflow.draft_issue(args.instruction)
        else:
            workflow.draft_pr(args.range)

    elif args.command == "approve":
        workflow.approve(args.yes)

    elif args.command == "improve":
        if args.kind == "issue":
            workflow.improve_issue(args.number)
        else:
            workflow.improve_pr(args.range)


if __name__ == "__main__":
    main()
