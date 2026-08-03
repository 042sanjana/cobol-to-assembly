import os


class AssemblyParser:

    def __init__(self, filepath):

        self.filepath = filepath

    def read_file(self):

        with open(self.filepath, "r") as file:

            return file.readlines()