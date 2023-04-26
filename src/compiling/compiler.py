import token
from lexer import Lexer
from parsing import Parser
from typing import Any

class Compiler:
    def __init__(self):
        self.vars = {}
    
    def compile(self, input: str) -> Any:
        lexer = Lexer(input)
        parser = Parser(lexer)
        result = parser.expr()
        return result
    
    def execute(self, input: str) -> Any:
        result = self.compile(input)
        return self.interpret(result)
    
    def interpret(self, result: Any) -> Any:
        if isinstance(result, token):
            if result.type == 'INTEGER':
                return result.value
            else:
                raise Exception('Invalid token')
        elif isinstance(result, int):
            return result
        elif isinstance(result, str):
            return self.vars.get(result)
        else:
            raise Exception('Invalid result type')
    
    def set_variable(self, var_name: str, value: int) -> None:
        self.vars[var_name] = value
