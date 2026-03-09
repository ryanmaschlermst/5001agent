class ReviewerAgent:

    def review(self, diff, files):

        findings = []

        if "TODO" in diff:
            findings.append("Found TODO comment in diff")

        if "password" in diff.lower():
            findings.append("Possible password exposure")

        if "except:" in diff:
            findings.append("Bare except detected")

        added_lines = [l for l in diff.splitlines() if l.startswith("+")]
        evidence = added_lines[:5]

        return {
            "findings": findings,
            "evidence": evidence,
            "file_samples": files[:2]
        }
