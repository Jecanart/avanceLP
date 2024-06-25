import ply.yacc as yacc
from datetime import datetime
from analizadorLexico import tokens, algoritmo_Macias, algoritmo_Torres
import sys

def p_cuerpo(p):
    '''cuerpo : expresion
              | println
              | ifStatement
              | ifElseStatement
              | variable
              | comment'''

def p_empty(p):
    'empty :'
    pass

def p_variable(p):
    '''variable :  expression
                | number
                | logicexpression
    '''

def p_expresion(p):
    'expresion : number operator number'


def p_logicexpresion(p):
    'logicexpression: value compOperator value'


def p_number(p):
    '''number : INTEGER
              | FLOAT'''

def p_operator(p):
    '''operator : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MOD'''

def p_compOperator(p):
    '''compOperator : EQUALS
                    | NOT_EQUALS
                    | LESSER
                    | GREATER
                    | LESSER_EQ
                    | GREATER_EQ'''

def p_value(p):
    '''value : VARIABLE
            | INTEGER
            | FLOAT'''
    
def p_values(p):
    '''values : value
            | value COMMA values'''

def p_println(p):
    '''println : PRINTLN NOT LPAREN RPAREN
                | PRINTLN NOT LPAREN STRING RPAREN SEMICOLON'''

def p_ifStatement(p):
    'ifStatement : IF logicexpression LLLAVE cuerpo RLLAVE SEMICOLON'

def p_ifElseStatement(p):
    'ifElseStatement : ifStatement elseStatement'

def p_elseStatement(p):
    '''elseStatement : ELSE LLLAVE cuerpo RLLAVE SEMICOLON
                     | ELSE IF logicexpression LLLAVE cuerpo RLLAVE elseStatement SEMICOLON '''

def p_comment(p):
    'comment :  COMMENT'





algoritmoCanarte = open ("algoritmos/algoritmo_canarte.txt")
algoritmoTorres = open ("algoritmos/algoritmo_torres.txt")

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

def logOutput(user, algoritmo):
    datime = datetime.now()
    timeStamp = datime.strftime("%d%m%Y-%Hh%M")
    dirString = "logs/sintactico-"+user+"-"+timeStamp+".txt"
    sys.stdout = open(dirString, 'w')
    for line in algoritmo:
        try:
            sentence = line.strip()
            sentence = sentence.strip("\n")
            s = sentence
        except EOFError:
            break
        if not s: 
            continue
        print(sentence)
        result = parser.parse(s)
    sys.stdout.close()
           
       

logOutput('jecanart', algoritmoCanarte)
