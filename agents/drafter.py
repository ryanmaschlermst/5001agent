class DrafterAgent:

    def issue(self, instruction):

        return f"""
[Draft Issue]

Title: Proposed improvement

Description:
{instruction}

Steps to reproduce:
1. Identify the problem
2. Apply the requested improvement

Expected result:
System behaves correctly after fix.
"""

    def pr(self, diff):

        summary = "\n".join(diff.splitlines()[:10])

        return f"""
[Draft PR]

Summary:
Implements fixes identified during review.

Key Changes:
{summary}

Testing:
- Run unit tests
- Verify behavior locally
"""

    def improve_issue(self, text):

        return f"""
[Improved Issue]

Original description:
{text}

Improved version:
- Clearer explanation
- Structured problem description
- Defined expected behavior
"""

    def improve_pr(self, diff):

        summary = "\n".join(diff.splitlines()[:10])

        return f"""
[Improved PR]

Changes summarized more clearly.

Code evidence:
{summary}

Testing plan:
1. Run project tests
2. Validate functionality
"""
