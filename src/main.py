from compiling.compiler import Compiler

compiler = Compiler()
user_input = input("Enter an arithmetic expression: ")
result = compiler.compile(user_input)
print(result)
