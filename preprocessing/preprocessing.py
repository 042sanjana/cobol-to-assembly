from parser.assembly_parser import AssemblyParser
from parser.module_splitter import ModuleSplitter
from parser.variable_extractor import VariableExtractor
from parser.dependency_analyzer import DependencyAnalyzer

from services.module_service import ModuleService

from knowledge.embedding_service import EmbeddingService
from knowledge.chroma_manager import collection


class Preprocessor:

    def process(self, filepath, upload_id):

        parser = AssemblyParser(filepath)
        lines = parser.read_file()

        splitter = ModuleSplitter()
        modules = splitter.split(lines)

        extractor = VariableExtractor()
        dependency = DependencyAnalyzer()

        module_service = ModuleService()

        embedder = EmbeddingService()

        analysis = {}

        for module_name, code in modules.items():

            parsed = extractor.extract(code)

            variables = parsed["variables"]
            instructions = parsed["instructions"]
            registers = parsed["registers"]

            dependencies = dependency.extract(code)

            # Save module metadata
            module_service.save(
                upload_id=upload_id,
                module_name=module_name,
                variables=variables,
                dependencies=dependencies
            )

            module_code = "\n".join(code)

            vector = embedder.create_embedding(module_code)

            collection.add(
                ids=[module_name],
                embeddings=[vector],
                documents=[module_code]
            )

            analysis[module_name] = {
                "variables": variables,
                "instructions": instructions,
                "registers": registers,
                "dependencies": dependencies,
                "code": code
            }

        return analysis