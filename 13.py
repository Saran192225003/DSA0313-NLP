class TopDownParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.tokens = []
        self.current_token_index = 0

    def parse(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        tree = self.parse_symbol('E')
        if tree and self.current_token_index == len(tokens):
            return tree
        else:
            return None

    def parse_symbol(self, symbol):
        for rule in self.grammar.get(symbol, []):
            start_index = self.current_token_index
            subtrees = []
            for token in rule:
                if token in self.grammar:  # Non-terminal
                    subtree = self.parse_symbol(token)
                    if subtree is None:
                        self.current_token_index = start_index
                        break
                    subtrees.append(subtree)
                else:  # Terminal
                    if self.match_token(token):
                        subtrees.append(token)
                    else:
                        self.current_token_index = start_index
                        break
            else:
                return (symbol, subtrees)
        return None

    def match_token(self, token):
        if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index] == token:
            self.current_token_index += 1
            return True
        return False

def print_tree(tree, level=0):
    if isinstance(tree, tuple):
        symbol, children = tree
        print('  ' * level + symbol)
        for child in children:
            print_tree(child, level + 1)
    else:
        print('  ' * level + tree)

# Example usage:
grammar = {
    'E': [['T'], ['T', '+', 'E']],
    'T': [['F'], ['F', '*', 'T']],
    'F': [['(', 'E', ')'], ['id']]
}

parser = TopDownParser(grammar)

# Testing with a valid input string: "id + id * id"
tokens = ['id', '+', 'id', '*', 'id']
parse_tree = parser.parse(tokens)
if parse_tree:
    print("The input string is valid according to the grammar.")
    print("Parse Tree:")
    print_tree(parse_tree)
else:
    print("The input string is not valid according to the grammar.")

# Testing with an invalid input string: "id + * id"
tokens = ['id', '+', '*', 'id']
parse_tree = parser.parse(tokens)
if parse_tree:
    print("The input string is valid according to the grammar.")
    print("Parse Tree:")
    print_tree(parse_tree)
else:
    print("The input string is not valid according to the grammar.")
