from agent_runner.runner import AgentRunner

runner = AgentRunner()

response = runner.run(

    agent_path="agents/syntax/agent.md",

    module="LOGIN",

    code="""

LOGIN:

LOAD R1, CUSTOMER

CALL AUTH

""",

    variables=["CUSTOMER"],

    dependencies=["AUTH"]

)

print(response)