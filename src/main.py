class Token:
    def __init__(self, type: str, value: any):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self, input: str):
        self.input = input
        self.pos = 0
    
    def next_token(self) -> Token:
        if self.pos >= len(self.input):
            return Token("EOF", None)
        
        if self.input[self.pos].isnumeric():
            token_value = ""
            while self.pos < len(self.input) and self.input[self.pos].isnumeric():
                token_value += self.input[self.pos]
                self.pos += 1
            return Token("NUMBER", int(token_value))
        
        elif self.input[self.pos] == "+":
            self.pos += 1
            return Token("PLUS", "+")
        
        elif self.input[self.pos] == "-":
            self.pos += 1
            return Token("MINUS", "-")
        
        else:
            raise Exception("Invalid input")


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


class Compiler:
    def compile(self, input):
        lexer = Lexer(input)
        parser = Parser(lexer)
        result = parser.expr()
        return result

compiler = Compiler()
user_input = input("Enter an arithmetic expression: ")
result = compiler.compile(user_input)
print(result)