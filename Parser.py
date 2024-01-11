#Falta ainda implementar o match em parse_term em relação à variáveis

from Node import Node

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.root = self.parse()

    def parse(self):
        try:
            return self.parse_expression()
        except IndexError:
            raise SyntaxError("Invalid expression")
        
    def parse_expression(self):
        left_operand = self.parse_term()

        while self.match(['and', 'or']):
            operator = self.previous()
            right_operand = self.parse_term()
            left_operand = Node(operator, [left_operand, right_operand])

        return left_operand

    def parse_term(self):
        if self.match(['True', 'False']):
            return Node(self.previous())
        elif self.match(['not']):
            operator = self.previous()
            operand = self.parse_term()
            return Node(operator, [operand])
        elif self.match(['(']):
            expression = self.parse_expression()
            self.consume(')')
            return expression
        else:
            raise SyntaxError("Invalid expression")

    def match(self, expected_tokens):
        if self.current < len(self.tokens):
            token = self.tokens[self.current]
            if token in expected_tokens:
                self.current += 1
                return True
        return False

    def consume(self, expected_token):
        if self.current < len(self.tokens):
            token = self.tokens[self.current]
            if token == expected_token:
                self.current += 1
                return True
        raise SyntaxError(f"Expected {expected_token}, but found {self.tokens[self.current]}")

    def previous(self):
        return self.tokens[self.current - 1] if self.current > 0 else None
    
    def display_tree(self):
        self.display_tree_recursive(self.root, 0)

    def display_tree_recursive(self, node, level):
        print("  " * level + str(node.value))
        for child in node.children:
            self.display_tree_recursive(child, level + 1)

    def get_root(self):
        return self.root
