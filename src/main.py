class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Lexer:
    def __init__(self, input):
        self.input = input
        self.pos = 0
    
    def next_token(self):
        if self.pos >= len(self.input):
            return Token("EOF", None)
        
        if self.input[self.pos].isdigit():
            token_value = ""
            while self.pos < len(self.input) and self.input[self.pos].isdigit():
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
