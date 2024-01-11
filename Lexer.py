#Falta ainda fazer a função de verificação de símbolos válidos.
#Neste caso: operadores, paretentêses, valores e variáveis.

class Lexer:
    def __init__(self, expression):
        self.expression = expression
        self.format_expression()
        self.tokens = self.expression.split()

    def get_expression(self):
        return self.expression

    def get_tokens(self):
        return self.tokens
    
    def check_expression(self):
        #self.check_symbols()
        self.check_parentheses()
        self.check_operator_scopes()
        self.check_consecutive_values()

    def format_expression(self):
        formatted_expression = self.expression.replace("(", " ( ").replace(")", " ) ")
        formatted_expression = formatted_expression.replace("not", " not ")
        formatted_expression = formatted_expression.replace("and", " and ")
        formatted_expression = " ".join(formatted_expression.split())
        self.expression = formatted_expression

    #def check_symbols(self):

    def check_parentheses(self):
        stack = []
        for token in self.tokens:
            if token == "(":
                stack.append("(")
            elif token == ")":
                if not stack:
                    raise SyntaxError("Mismatched parentheses")
                stack.pop()
        if stack:
            raise SyntaxError("Mismatched parentheses")

    def check_operator_scopes(self):
        for i, token in enumerate(self.tokens):
            if token.lower() == "not":
                if i == len(self.tokens) - 1 or self.tokens[i + 1].lower() in ["and", "or"]:
                    raise SyntaxError(f"Invalid scope for {token} operator")
            elif token.lower() in ["and", "or"] and (i == 0 or i == len(self.tokens) - 1):
                raise SyntaxError(f"Invalid scope for {token} operator")


    def check_consecutive_values(self):
        for i in range(len(self.tokens) - 1):
            current_token = self.tokens[i]
            next_token = self.tokens[i + 1]
            if current_token.lower() in ["true", "false"] and next_token.lower() in ["true", "false"]:
                raise SyntaxError("Consecutive values without operator")
