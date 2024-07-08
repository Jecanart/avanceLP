import ply.yacc as yacc
from datetime import datetime
from analizadorLexico import tokens, algoritmo_Macias, algoritmo_Torres
import sys

variables = {

}

def p_cuerpo(p):
    '''cuerpo : expression
              | println
              | ifStatement
              | ifElseStatement
              | varStatement
              | variable
              | emptyString
              | arrayStatement
              | emptyFunctionSt
              | voidFunctionSt'''

def p_println(p):
    '''println : PRINTLN NOT LPAREN RPAREN SEMICOLON
                | PRINTLN NOT LPAREN STRING RPAREN SEMICOLON'''

def p_varStatement(p):
    '''varStatement : LET VARIABLE ASSIGN value SEMICOLON
                    | LET MUT VARIABLE ASSIGN value SEMICOLON'''
    if len(p) == 6:
        variables[p[2]] = p[4]
    elif len(p) == 7:
        variables[p[3]] = p[5]

def p_ifStatement(p):
    'ifStatement : IF logicExpressions LLLAVE cuerpo RLLAVE SEMICOLON'

def p_ifElseStatement(p):
    'ifElseStatement : ifStatement elseStatement'

def p_elseStatement(p):
    '''elseStatement : ELSE LLLAVE cuerpo RLLAVE SEMICOLON
                     | ELSE IF logicExpressions LLLAVE cuerpo RLLAVE elseStatement SEMICOLON '''

def p_arrayStatementWOType(p):
    'arrayStatement : LET VARIABLE ASSIGN LBRACKET values RBRACKET SEMICOLON'
    variables[p[2]] = p[5]

def p_emptyString(p):
    '''emptyString : LET VARIABLE ASSIGN SEMICOLON SEMICOLON NEW LPAREN RPAREN SEMICOLON
                   | LET MUT VARIABLE ASSIGN SEMICOLON SEMICOLON NEW LPAREN RPAREN SEMICOLON'''

def p_emptyFunctionSt(p):
    'emptyFunctionSt : FN VARIABLE LPAREN RPAREN LLLAVE RLLAVE'

def p_voidFunctionSt(p):
    'voidFunctionSt : FN VARIABLE LPAREN RPAREN LLLAVE cuerpo RLLAVE'

def p_empty(p):
    'empty :'
    pass

def p_variable(p):
    '''variable : expression
                | value
                | logicExpressions
    '''

def p_expressions(p):
    '''expressions : expression
                    | expression operator expressions'''

def p_expression(p):
    '''expression : value operator value'''
    if not isinstance(p[1], str) or p[1] in variables:
        if isinstance(p[1], (int, float)):
            print(type(p[1]).__name__)
            pass
        else: 
            print(f"Semantic error, uncompatible type {type(p[1]).__name__}")
    else:
        print(f"Semantic error, variable {p[1]} has not been initialized")
        return
    if not isinstance(p[3], str) or p[3] in variables:
        if isinstance(p[3], (int, float)):
            print(type(p[3]).__name__)
            pass
        else: 
            print(f"Semantic error, uncompatible type {type(p[3]).__name__}")
    else:
        print(f"Semantic error, variable {p[3]} has not been initialized")


def p_logicExpressions(p):
    '''logicExpressions : logicExpression
                        | logicExpression lConector logicExpressions'''
def p_logicExpression(p):
    'logicExpression : value compOperator value'

def p_lConector(p):
    '''lConector : AND
                 | OR
                 | NOT'''

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
             | FLOAT
             | STRING
             | BOOL
             | STRING
             | BOLL'''
    if isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]]
    else:
        p[0] = p[1]
    
def p_values(p):
    '''values : value
            | value COMMA values'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


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
           
while True:
    try:
        s = input('')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)

#logOutput('jecanart', algoritmoCanarte)
#logOutput('JoseTorres2210', algoritmoTorres)
#logOutput('Ghost04102002', algoritmoMacias)