class Grammar:
    def __init__(self, rules):
        self.rules = rules
        self.start_symbol = list(rules.keys())[0]

    def productions_for(self, nonterminal):
        return self.rules.get(nonterminal, [])


class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, tokens):
        n = len(tokens)
        # S[i] will hold the set of states at position i in the input
        S = [set() for _ in range(n + 1)]
        # Adding the initial state
        S[0].add((self.grammar.start_symbol, 0, 0))

        for i in range(n + 1):
            states = list(S[i])
            for state in states:
                lhs, dot, start = state
                if dot < len(self.grammar.productions_for(lhs)[0]):
                    next_symbol = self.grammar.productions_for(lhs)[0][dot]
                    if next_symbol in self.grammar.rules:
                        self.predict(S, i, next_symbol)
                    elif i < n and next_symbol == tokens[i]:
                        self.scan(S, i, next_symbol, state)
                else:
                    self.complete(S, i, state)

        # Check if the initial state is in the final set
        for state in S[n]:
            if state == (self.grammar.start_symbol, 1, 0):
                return True
        return False

    def predict(self, S, i, nonterminal):
        for production in self.grammar.productions_for(nonterminal):
            S[i].add((nonterminal, 0, i))

    def scan(self, S, i, terminal, state):
        lhs, dot, start = state
        S[i + 1].add((lhs, dot + 1, start))

    def complete(self, S, i, state):
        lhs, dot, start = state
        for st in S[start]:
            st_lhs, st_dot, st_start = st
            if st_dot < len(self.grammar.productions_for(st_lhs)[0]):
                if self.grammar.productions_for(st_lhs)[0][st_dot] == lhs:
                    S[i].add((st_lhs, st_dot + 1, st_start))

# Example usage:
grammar = Grammar({
    'E': [['T'], ['T', '+', 'E']],
    'T': [['F'], ['F', '*', 'T']],
    'F': [['(', 'E', ')'], ['id']]
})

parser = EarleyParser(grammar)

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
