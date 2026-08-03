from parser.assembly_parser import AssemblyParser
from parser.module_splitter import ModuleSplitter
from parser.variable_extractor import VariableExtractor
from parser.dependency_analyzer import DependencyAnalyzer

from services.module_service import ModuleService

from knowledge.embedding_service import EmbeddingService
from knowledge.chroma_manager import collection


class Preprocessor:

    def process(self, filepath):

        parser = AssemblyParser(filepath)

        lines = parser.read_file()

        splitter = ModuleSplitter()

        modules = splitter.split(lines)

        extractor = VariableExtractor()

        dependency = DependencyAnalyzer()

        module_service = ModuleService()

        embedder = EmbeddingService()

        result = {}

        for module_name, code in modules.items():

            variables = extractor.extract(code)

            dependencies = dependency.extract(code)

            # -----------------------------
            # Save metadata in SQLite
            # -----------------------------
            module_service.save(
                module_name,
                variables,
                dependencies
            )

            # -----------------------------
            # Convert module to text
            # -----------------------------
            module_code = "\n".join(code)

            # -----------------------------
            # Create embedding
            # -----------------------------
            vector = embedder.create_embedding(module_code)

            # -----------------------------
            # Store embedding in ChromaDB
            # -----------------------------
            collection.add(
                ids=[module_name],
                embeddings=[vector],
                documents=[module_code]
            )

            result[module_name] = {
                "variables": variables,
                "dependencies": dependencies,
                "code": code
            }

        return result