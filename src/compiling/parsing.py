from compiling.lexer import Lexer
from compiling.token import Token

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def eat(self, token_type: str) -> None:
        if self.current_token.token_type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise ValueError(f'Invalid syntax: expected {token_type}, but got {self.current_token.token_type}')
    
    def factor(self) -> int:
        token = self.current_token
        if token.token_type == 'INTEGER':
            self.eat('INTEGER')
            return token.value
        else:
            raise ValueError('Invalid syntax: expected an integer')
    
    def expr(self) -> int:
        result = self.factor()
        while self.current_token.token_type in ('PLUS', 'MINUS'):
            if self.current_token.token_type == 'PLUS':
                self.eat('PLUS')
                result += self.factor()
            elif self.current_token.token_type == 'MINUS':
                self.eat('MINUS')
                result -= self.factor()
        return result
