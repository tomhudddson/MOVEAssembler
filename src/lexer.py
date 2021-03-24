from enum import Enum

class Lexemes(Enum):
    # Single character tokens.
    HASH = 1,
    COMMA = 2,
    RIGHT_BRACE = 3,
    LEFT_BRACE = 4,
    SEMI_COLON = 5,
    HYPHEN = 6,
    DOLLAR = 7,

    # Literals
    IDENTIFIER = 8,
    STRING = 9,
    NUMBER = 10,

    # Keywords
    MOVE = 11

class Lexer:
    def __init__(self, src):
        self.src = src

        self.tokens = []

    def run(self):
        with open(self.src) as f:
            for self.line in f:    
                for self.i in range (0, len(self.line)):
                    self._scanToken(self.line[self.i])

        print(self.tokens)    
    
    def _scanToken(self, char):
        if char == "#": 
            self._addToken(Lexemes.HASH)
        elif  char == ",":
            self._addToken(Lexemes.COMMA)
        elif char == "{":
            self._addToken(Lexemes.LEFT_BRACE)
        elif  char == "}":
            self._addToken(Lexemes.RIGHT_BRACE)
        elif  char == ";":
            self._addToken(Lexemes.SEMI_COLON)
        elif char == "-":
            self._addToken(Lexemes.HYPHEN)
        elif char == "$":
            self._addToken(Lexemes.DOLLAR)
            

    def _addToken(self, type):
        self.tokens.append(type)

    def _advance(self):
        # TODO: check out of bounds here.
        self.i += 1
        return self.line[self.i]

    def _peek(self):
        pass
    