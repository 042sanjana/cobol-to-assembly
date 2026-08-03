import re


class DependencyAnalyzer:

    def extract(self, lines):

        calls = []

        for line in lines:

            match = re.search(r'CALL\s+([A-Z0-9_]+)', line)

            if match:

                calls.append(match.group(1))

        return calls