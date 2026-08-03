import re


class ModuleSplitter:

    def split(self, lines):

        modules = {}

        current_module = "GLOBAL"

        modules[current_module] = []

        for line in lines:

            text = line.strip()

            if re.match(r'^[A-Z0-9_]+:$', text):

                current_module = text.replace(":", "")

                modules[current_module] = []

                continue

            modules[current_module].append(text)

        return modules