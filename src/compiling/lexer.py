from compiling.token import Token

class Lexer:
    def __init__(self, input_string: str):
        self.input_string = input_string
        self.position = 0
        self.current_char = self.input_string[self.position] if self.position < len(self.input_string) else None
        
    def advance(self):
        self.position += 1
        self.current_char = self.input_string[self.position] if self.position < len(self.input_string) else None
    
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
            
    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
    
    def get_next_token(self) -> Token:
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            if self.current_char.isdigit():
                return Token('INTEGER', self.integer())
            
            operator_tokens = {
                '+': Token('PLUS', '+'),
                '-': Token('MINUS', '-'),
            }
            if self.current_char in operator_tokens:
                token = operator_tokens[self.current_char]
                self.advance()
                return token
            
            raise ValueError(f'Invalid character: {self.current_char}')
        
        return Token('EOF', None)
