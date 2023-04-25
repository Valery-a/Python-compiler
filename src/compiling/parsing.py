from lexer import Lexer
from token import Token

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.next_token()
    
    def eat(self, token_type: str) -> None:
        if self.current_token.type == token_type:
            self.current_token = self.lexer.next_token()
        else:
            raise Exception("Invalid syntax")
    
    def factor(self) -> int:
        token = self.current_token
        if token.type == "NUMBER":
            self.eat("NUMBER")
            return token.value
        else:
            raise Exception("Invalid syntax")
    
    def expr(self) -> int:
        result = self.factor()
        while self.current_token.type in ("PLUS", "MINUS"):
            if self.current_token.type == "PLUS":
                self.eat("PLUS")
                result += self.factor()
            elif self.current_token.type == "MINUS":
                self.eat("MINUS")
                result -= self.factor()
        return result
