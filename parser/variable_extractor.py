import re


class VariableExtractor:

    def __init__(self):

        self.instructions = {

            "LOAD",
            "STORE",
            "CALL",
            "BR",
            "BNE",
            "BEQ",
            "ADD",
            "SUB",
            "MULT",
            "DIV",
            "COMPARE",
            "RETURN",
            "DISPLAY",
            "STOP",
            "END"

        }

    def extract(self, code):

        variables = []

        instructions = []

        registers = []

        for line in code:

            words = re.findall(r"[A-Z_][A-Z0-9_]*", line)

            for word in words:

                # Assembly instruction
                if word in self.instructions:

                    if word not in instructions:
                        instructions.append(word)

                # Register
                elif re.fullmatch(r"R\d+", word):

                    if word not in registers:
                        registers.append(word)

                # Variable
                else:

                    if word not in variables:
                        variables.append(word)

        return {

            "variables": variables,

            "instructions": instructions,

            "registers": registers

        }