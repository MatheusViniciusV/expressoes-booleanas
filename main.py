from Lexer import Lexer
from Parser import Parser

#Segue uma função que retorna o valor da expressão booleana caso essa não tenha variáveis
def evaluate_tree(node):
    if node.value == 'and':
        return evaluate_tree(node.children[0]) and evaluate_tree(node.children[1])
    elif node.value == 'or':
        return evaluate_tree(node.children[0]) or evaluate_tree(node.children[1])
    elif node.value == 'not':    
        return not evaluate_tree(node.children[0])
    elif node.value == 'True':
        return True
    elif node.value == 'False':
        return False

if __name__ == "__main__":

    expression = input("Digite a expressão booleana: ")

    lexer = Lexer(expression)
    lexer.check_expression()
    parser = Parser(lexer.get_tokens())
    value = evaluate_tree(parser.get_root())
    
    print("Expressão formatada: ")
    print(lexer.get_expression())

    print("Tokens da expressão: ")
    print(lexer.get_tokens())

    print("Árvore sintática da expressão: ")
    parser.display_tree()

    print("Valor da expressão: ")
    print(value)