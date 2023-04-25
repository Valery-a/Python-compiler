from lexer import Lexer
from parsing import Parser
from typing import Any

class Compiler:
    def compile(self, input: str) -> Any:
        lexer = Lexer(input)
        parser = Parser(lexer)
        result = parser.expr()
        return result
