import re


class VariableExtractor:

    keywords = {

        "LOAD",

        "STORE",

        "ADD",

        "SUB",

        "MULT",

        "MOVE"

    }

    def extract(self, lines):

        variables = set()

        for line in lines:

            tokens = re.findall(r"[A-Z_]+", line)

            for token in tokens:

                if token not in self.keywords:

                    variables.add(token)

        return sorted(list(variables))