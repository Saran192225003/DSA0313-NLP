grammar = {
    'E': [['T'], ['T', '+', 'E']],
    'T': [['F'], ['F', '*', 'T']],
    'F': [['(', 'E', ')'], ['id']]
}
class TopDownParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.tokens = []
        self.current_token_index = 0

    def parse(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        return self.parse_symbol('E')

    def parse_symbol(self, symbol):
        for rule in self.grammar.get(symbol, []):
            if self.match_rule(rule):
                return True
        return False

    def match_rule(self, rule):
        saved_index = self.current_token_index
        for token in rule:
            if token in self.grammar:  # Non-terminal
                if not self.parse_symbol(token):
                    self.current_token_index = saved_index
                    return False
            else:  # Terminal
                if not self.match_token(token):
                    self.current_token_index = saved_index
                    return False
        return True

    def match_token(self, token):
        if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index] == token:
            self.current_token_index += 1
            return True
        return False

# Example usage:
parser = TopDownParser(grammar)

# Testing with a valid input string: "id + id * id"
tokens = ['id', '+', 'id', '*', 'id']
if parser.parse(tokens):
    print("The input string is valid according to the grammar.")
else:
    print("The input string is not valid according to the grammar.")

# Testing with an invalid input string: "id + * id"
tokens = ['id', '+', '*', 'id']
if parser.parse(tokens):
    print("The input string is valid according to the grammar.")
else:
    print("The input string is not valid according to the grammar.")
