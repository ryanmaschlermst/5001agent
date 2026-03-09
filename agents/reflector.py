class ReflectorAgent:

    def reflect_issue(self, draft):

        checks = []

        checks.append(("Contains title", "Title:" in draft))
        checks.append(("Contains description", "Description:" in draft))
        checks.append(("Contains expected result", "Expected result" in draft))

        report = "[Reflection]\n"

        for name, ok in checks:
            status = "PASS" if ok else "FAIL"
            report += f"{name}: {status}\n"

        return report

    def reflect_pr(self, draft):

        checks = []

        checks.append(("Contains summary", "Summary" in draft))
        checks.append(("Contains testing plan", "Testing" in draft))
        checks.append(("No sensitive data", "password" not in draft.lower()))

        report = "[Reflection]\n"

        for name, ok in checks:
            status = "PASS" if ok else "FAIL"
            report += f"{name}: {status}\n"

        return report
