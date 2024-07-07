import ply.yacc as yacc
from datetime import datetime
from analizadorLexico import tokens, algoritmo_Macias, algoritmo_Torres
import sys

def p_cuerpo(p):
    '''cuerpo : expressions
              | println
              | ifStatement
              | ifElseStatement
              | varStatement
              | variable
              | emptyString
              | arrayStatement
              | emptyFunctionSt
              | voidFunctionSt'''

def p_empty(p):
    'empty :'
    pass

def p_variable(p):
    '''variable : expression
                | number
                | logicExpressions
    '''

def p_expressions(p):
    '''expressions : expression
                    | expression operator expressions'''

def p_expression(p):
    '''expression : value operator value'''


def p_logicExpressions(p):
    '''logicExpressions : logicExpression
                        | logicExpression lConector logicExpressions'''
def p_logicExpression(p):
    'logicExpression : value compOperator value'

def p_lConector(p):
    '''lConector : AND
                 | OR
                 | NOT'''

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

def p_varStatement(p):
    '''varStatement : LET VARIABLE ASSIGN value SEMICOLON
                    | LET MUT VARIABLE ASSIGN value SEMICOLON'''

def p_ifStatement(p):
    'ifStatement : IF logicExpressions LLLAVE cuerpo RLLAVE SEMICOLON'

def p_ifElseStatement(p):
    'ifElseStatement : ifStatement elseStatement'

def p_elseStatement(p):
    '''elseStatement : ELSE LLLAVE cuerpo RLLAVE SEMICOLON
                     | ELSE IF logicExpressions LLLAVE cuerpo RLLAVE elseStatement SEMICOLON '''

def p_arrayStatementWOType(p):
    'arrayStatement : LET VARIABLE ASSIGN LBRACKET values RBRACKET SEMICOLON'

def p_emptyString(p):
    '''emptyString : LET VARIABLE ASSIGN SEMICOLON SEMICOLON NEW LPAREN RPAREN SEMICOLON
                   | LET MUT VARIABLE ASSIGN SEMICOLON SEMICOLON NEW LPAREN RPAREN SEMICOLON'''

def p_emptyFunctionSt(p):
    'emptyFunctionSt : FN VARIABLE LPAREN RPAREN LLLAVE RLLAVE'

def p_voidFunctionSt(p):
    'voidFunctionSt : FN VARIABLE LPAREN RPAREN LLLAVE cuerpo RLLAVE'





algoritmoCanarte = open ("algoritmos/algoritmo_canarte.txt")
algoritmoTorres = open ("algoritmos/algoritmo_torres.txt")
algoritmoMacias = open ("algoritmos/algoritmo_macias.txt")

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
#logOutput('JoseTorres2210', algoritmoTorres)
#logOutput('Ghost04102002', algoritmoMacias)