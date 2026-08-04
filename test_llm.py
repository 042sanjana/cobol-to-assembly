from llm.llm_client import LLMClient

llm = LLMClient()

response = llm.ask(

    """
    Explain Assembly language in one paragraph.
    """

)

print(response)