import ply.yacc as yacc
from analizadorLexico import tokens

def p_cuerpo(p):
    "cuerpo: expresion"
    