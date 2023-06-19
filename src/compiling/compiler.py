from compiling.lexer import Lexer
from compiling.parsing import Parser
from compiling.token import Token


class Compiler:
    def __init__(self):
        self.vars = {}
    
    def compile(self, input_string: str) -> any:
        lexer = Lexer(input_string)
        parser = Parser(lexer)
        result = parser.expr()
        return result
    
    def execute(self, input_string: str) -> any:
        result = self.compile(input_string)
        return self.interpret(result)
    
    def interpret(self, result: any) -> any:
        if isinstance(result, Token):
            if result.token_type == 'INTEGER':
                return result.value
            else:
                raise ValueError('Invalid token')
        elif isinstance(result, int):
            return result
        elif isinstance(result, str):
            return self.vars.get(result)
        else:
            raise TypeError('Invalid result type')
    
    def set_variable(self, var_name: str, value: int) -> None:
        self.vars[var_name] = value
