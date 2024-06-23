import ply.yacc as yacc
from datetime import datetime
from analizadorLexico import tokens, algoritmo_Canarte, algoritmo_Macias, algoritmo_Torres

def p_cuerpo(p):
    '''cuerpo : expresion
              | println'''

def p_expresion(p):
    'expresion : number operator number'

def p_number(p):
    '''number : INTEGER
              | FLOAT'''

def p_operator(p):
    '''operator : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MOD'''

def p_println(p):
    '''println : PRINTLN NOT LPAREN RPAREN
                | PRINTLN NOT LPAREN STRING RPAREN'''

def p_value(p):
    '''value : VARIABLE
            | INTEGER
            | FLOAT'''
    
def p_values(p):
    '''values : value
            | value COMMA values'''





# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)