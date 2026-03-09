class PlannerAgent:

    def plan(self, review):

        evidence = review.get("evidence", [])

        if evidence:
            reason = f"Reviewer detected potential problems such as: {evidence[0]}"
        else:
            reason = "Reviewer did not detect major issues."

        plan = f"""
        [Planner]

        Plan:
        1. Analyze reviewer findings
        2. Decide whether to create Issue or PR
        3. Forward results to drafting stage

        Reason:
        {reason}
        """

        return plan
