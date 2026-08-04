from backend.agent_runner.runner import SyntaxRunner

runner = SyntaxRunner()

code = """

LOGIN:

LOAD R1, CUSTOMER

CALL AUTH

"""

response = runner.run(

    module="LOGIN",

    code=code,

    variables=["CUSTOMER"],

    dependencies=["AUTH"]

)

print(response)