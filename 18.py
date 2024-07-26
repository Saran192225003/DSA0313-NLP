class FOPCParser:
    def __init__(self):
        pass

    def parse(self, expression):
        tokens = self.tokenize(expression)
        tree = self.parse_expression(tokens)
        return tree

    def tokenize(self, expression):
        return expression.replace('(', ' ( ').replace(')', ' ) ').split()

    def parse_expression(self, tokens):
        if tokens[0] == '(':
            tokens.pop(0)
            operator = tokens.pop(0)
            args = []
            while tokens[0] != ')':
                args.append(self.parse_expression(tokens))
            tokens.pop(0)
            return (operator, args)
        else:
            return tokens.pop(0)

# Example usage:
parser = FOPCParser()
expression = "(and (or A B) (not C))"
parse_tree = parser.parse(expression)
print("Parse Tree:", parse_tree)
