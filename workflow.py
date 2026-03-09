from agents.planner import PlannerAgent
from agents.reviewer import ReviewerAgent
from agents.drafter import DrafterAgent
from agents.reflector import ReflectorAgent

from tools.git_tools import get_diff
from tools.github_tools import fetch_issue
from tools.file_tools import read_files

import json


class Workflow:

    def __init__(self):
        self.planner = PlannerAgent()
        self.reviewer = ReviewerAgent()
        self.drafter = DrafterAgent()
        self.reflector = ReflectorAgent()

    def review(self, commit_range):

        diff = get_diff(commit_range)
        files = read_files()

        result = self.reviewer.review(diff, files)
        plan = self.planner.plan(result)

        print(plan)

        print("\n[Reviewer Findings]")
        for f in result["findings"]:
            print("-", f)

        print("\n[Evidence]")
        for e in result["evidence"]:
            print(e)

    def draft_issue(self, instruction):

        draft = self.drafter.issue(instruction)
        reflection = self.reflector.reflect_issue(draft)

        print(draft)
        print(reflection)

    def draft_pr(self, commit_range):

        diff = get_diff(commit_range)

        draft = self.drafter.pr(diff)
        reflection = self.reflector.reflect_pr(draft)

        print(draft)
        print(reflection)

    def approve(self, decision):

        if decision:
            print("[Human Approval] Approved")
        else:
            print("[Human Approval] Rejected")

    def improve_issue(self, number):

        issue = fetch_issue(number)

        try:
            issue = json.loads(issue)
            text = issue.get("body", "")
        except Exception:
            text = str(issue)

        improved = self.drafter.improve_issue(text)

        print(improved)

    def improve_pr(self, commit_range):

        diff = get_diff(commit_range)

        improved = self.drafter.improve_pr(diff)

        print(improved)
