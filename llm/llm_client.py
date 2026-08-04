import ollama


class LLMClient:

    def __init__(self):

        self.model = "gemma3-local"

    def ask(self, prompt):

        response = ollama.chat(

            model=self.model,

            messages=[

                {

                    "role": "user",

                    "content": prompt

                }

            ]

        )

        return response["message"]["content"]