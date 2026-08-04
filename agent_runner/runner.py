from agent_runner.loader import AgentLoader

from rag.context_builder import ContextBuilder

from llm.llm_client import LLMClient


class AgentRunner:

    def __init__(self):

        self.loader = AgentLoader()

        self.llm = LLMClient()

        self.builder = ContextBuilder()

    def run(

        self,

        agent_path,

        module,

        code,

        variables,

        dependencies,

        retrieved_context=""

    ):

        instruction = self.loader.load(

            agent_path

        )

        context = self.builder.build(

            module,

            code,

            variables,

            dependencies,

            retrieved_context

        )

        prompt = instruction + "\n\n" + context

        response = self.llm.ask(prompt)

        return response