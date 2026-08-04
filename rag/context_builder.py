class ContextBuilder:

    def build(

        self,

        module,

        code,

        variables,

        dependencies,

        retrieved_context=""

    ):

        prompt = f"""

Module

{module}

Variables

{variables}

Dependencies

{dependencies}

Assembly Code

{code}

"""

        if retrieved_context:

            prompt += f"""

Previous Knowledge

{retrieved_context}

"""

        return prompt