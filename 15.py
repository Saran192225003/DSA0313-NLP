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
                if token in self.grammar:
                    subtree = self.parse_symbol(token)
                    if subtree is None:
                        self.current_token_index = start_index
                        break
                    subtrees.append(subtree)
                else:
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

class ProbabilisticTopDownParser(TopDownParser):
    def __init__(self, grammar):
        super().__init__(grammar)
        self.probabilities = grammar['probabilities']

    def parse(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        tree, prob = self.parse_symbol('E')
        if tree and self.current_token_index == len(tokens):
            return tree, prob
        else:
            return None, 0

    def parse_symbol(self, symbol):
        best_tree = None
        best_prob = 0
        for rule in self.grammar.get(symbol, []):
            start_index = self.current_token_index
            subtrees = []
            total_prob = self.probabilities.get((symbol, tuple(rule)), 1)
            for token in rule:
                if token in self.grammar:
                    subtree, prob = self.parse_symbol(token)
                    if subtree is None:
                        self.current_token_index = start_index
                        break
                    subtrees.append(subtree)
                    total_prob *= prob
                else:
                    if self.match_token(token):
                        subtrees.append(token)
                    else:
                        self.current_token_index = start_index
                        break
            else:
                if total_prob > best_prob:
                    best_tree = (symbol, subtrees)
                    best_prob = total_prob
        return best_tree, best_prob

# Example usage:
grammar = {
    'E': [['T'], ['T', '+', 'E']],
    'T': [['F'], ['F', '*', 'T']],
    'F': [['(', 'E', ')'], ['id']],
    'probabilities': {
        ('E', ('T',)): 0.6,
        ('E', ('T', '+', 'E')): 0.4,
        ('T', ('F',)): 0.7,
        ('T', ('F', '*', 'T')): 0.3,
        ('F', ('(', 'E', ')')): 0.2,
        ('F', ('id',)): 0.8
    }
}

parser = ProbabilisticTopDownParser(grammar)
tokens = ['id', '+', 'id', '*', 'id']
parse_tree, prob = parser.parse(tokens)
if parse_tree:
    print("The input string is valid according to the grammar with probability", prob)
    print("Parse Tree:")
    print_tree(parse_tree)
else:
    print("The input string is not valid according to the grammar.")
