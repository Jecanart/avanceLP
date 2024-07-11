import ply.yacc as yacc
from analizadorLexico import tokens, lexical_errors

variables = {}
mutables = {}
syntactic_errors = []

loop_stack = []
valid_iterable_types = {'vector', 'linkedlist', 'range'}

# Regla principal
def p_program(p):
    '''program : statements'''

def p_statements(p):
    '''statements : statement
                  | statement statements'''

def p_statement(p):
    '''statement : expression SEMICOLON
                 | logicExpression SEMICOLON
                 | println
                 | tuple
                 | linkedlist
                 | vector
                 | breakStatement
                 | forLoop
                 | whileLoop
                 | ifStatement
                 | ifElseStatement
                 | varStatement
                 | assignmentStatement
                 | variable SEMICOLON
                 | arrayStatement
                 | emptyString
                 | emptyFunctionSt
                 | voidFunctionSt'''

def p_println(p):
    '''println : PRINTLN NOT LPAREN RPAREN SEMICOLON
               | PRINTLN NOT LPAREN STRING RPAREN SEMICOLON'''

def p_breakStatement(p):
    '''breakStatement : BREAK SEMICOLON'''
    if not loop_stack:
        syntactic_errors.append(f"Error semántico: 'break' fuera de un bucle en línea {p.lineno(1)}")

def p_forLoop(p):
    '''forLoop : FOR VARIABLE IN expression LLLAVE statements RLLAVE'''
    if not is_valid_iterable(p[4]):
        syntactic_errors.append(f"Error semántico: La expresión en 'for' no es una colección o rango válido en línea {p.lineno(3)}")
    loop_stack.append('for')
    p[0] = ('for', p[2], p[4], p[6])
    loop_stack.pop()

def is_valid_iterable(expression):
    if isinstance(expression, str) and expression in variables:
        var_type = variables[expression][0]
        return var_type in valid_iterable_types
    elif isinstance(expression, (list, range)):
        return True
    return False

def p_whileLoop(p):
    '''whileLoop : WHILE logicExpressions LLLAVE statements RLLAVE'''
    loop_stack.append('while')
    p[0] = ('while', p[2], p[4])
    loop_stack.pop()

def p_tuple(p):
    'tuple : LET VARIABLE ASSIGN LPAREN values RPAREN SEMICOLON'
    p[0] = (p[2], tuple(p[5]))

def p_linkedlist(p):
    '''linkedlist : LPAREN value linkedlist_tail RPAREN'''
    if p[3] is None:
        p[0] = (p[2],)
    else:
        p[0] = (p[2], p[3])

def p_linkedlist_tail(p):
    '''linkedlist_tail : COMMA value linkedlist_tail
                       | empty'''
    if len(p) == 2:
        p[0] = None
    else:
        if p[3] is None:
            p[0] = (p[2],)
        else:
            p[0] = (p[2], p[3])

def p_vector(p):
    '''vector : LET VARIABLE COLON VEC LESSER TYPE GREATER ASSIGN VEC NOT LPAREN elements RPAREN SEMICOLON
              | LET VARIABLE ASSIGN VEC NOT LBRACKET elements RBRACKET SEMICOLON'''
    if len(p) == 15:
        p[0] = (p[2], p[12])
    elif len(p) == 12:
        p[0] = (p[2], p[7])

def p_elements(p):
    '''elements : element
                | element COMMA elements'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        if type(p[1]) != type(p[3][0]):
            raise SyntaxError(f"Error de tipo: Elementos de diferentes tipos en vector en línea {p.lineno(1)}")
        p[0] = [p[1]] + p[3]

def p_element(p):
    '''element : INTEGER
               | FLOAT
               | STRING
               | vector'''
    p[0] = p[1]

def p_varStatement(p):
    '''varStatement : LET VARIABLE ASSIGN value SEMICOLON
                    | LET MUT VARIABLE ASSIGN value SEMICOLON
                    | LET VARIABLE ASSIGN expressions SEMICOLON
                    | LET MUT VARIABLE ASSIGN expressions SEMICOLON'''
    if len(p) == 6:
        if p[2] in variables:
            syntactic_errors.append(f"Semantic error: Variable '{p[2]}' is already initialized at line {p.lineno(2)}")
        else:
            variables[p[2]] = p[4]
            mutables[p[2]] = False
    elif len(p) == 7:
        if p[3] in variables:
            syntactic_errors.append(f"Semantic error: Variable '{p[3]}' is already initialized at line {p.lineno(3)}")
        else:
            variables[p[3]] = p[5]
            mutables[p[3]] = True

def p_assignmentStatement(p):
    '''assignmentStatement : VARIABLE ASSIGN value SEMICOLON'''
    if p[1] in variables:
        if mutables[p[1]]:
            variables[p[1]] = p[3]
        else:
            syntactic_errors.append(f"Semantic error: Variable '{p[1]}' is not mutable at line {p.lineno(1)}")
    else:
        syntactic_errors.append(f"Semantic error: Variable '{p[1]}' is not initialized at line {p.lineno(1)}")

def p_ifStatement(p):
    'ifStatement : IF logicExpressions LLLAVE statements RLLAVE SEMICOLON'

def p_ifElseStatement(p):
    'ifElseStatement : ifStatement elseStatement'

def p_elseStatement(p):
    '''elseStatement : ELSE LLLAVE statements RLLAVE SEMICOLON
                     | ELSE IF logicExpressions LLLAVE statements RLLAVE elseStatement SEMICOLON'''

def p_arrayStatement(p):
    'arrayStatement : LET VARIABLE ASSIGN LBRACKET values RBRACKET SEMICOLON'
    if p[2] in variables:
        syntactic_errors.append(f"Semantic error: Variable '{p[2]}' is already initialized at line {p.lineno(2)}")
    else:
        variables[p[2]] = p[5]
        mutables[p[2]] = False

def p_emptyString(p):
    '''emptyString : LET VARIABLE ASSIGN SEMICOLON SEMICOLON NEW LPAREN RPAREN SEMICOLON
                   | LET MUT VARIABLE ASSIGN SEMICOLON SEMICOLON NEW LPAREN RPAREN SEMICOLON'''
    if len(p) == 10:
        if p[2] in variables:
            syntactic_errors.append(f"Semantic error: Variable '{p[2]}' is already initialized at line {p.lineno(2)}")
        else:
            variables[p[2]] = ""
            mutables[p[2]] = False
    elif len(p) == 11:
        if p[3] in variables:
            syntactic_errors.append(f"Semantic error: Variable '{p[3]}' is already initialized at line {p.lineno(3)}")
        else:
            variables[p[3]] = ""
            mutables[p[3]] = True

def p_emptyFunctionSt(p):
    'emptyFunctionSt : FN VARIABLE LPAREN RPAREN LLLAVE RLLAVE'

def p_voidFunctionSt(p):
    'voidFunctionSt : FN VARIABLE LPAREN RPAREN LLLAVE statements RLLAVE'

def p_empty(p):
    'empty :'
    pass

def p_variable(p):
    '''variable : VARIABLE'''

def p_expressions(p):
    '''expressions : expression
                   | expression operator expressions'''

def p_expression(p):
    '''expression : value operator value'''
    if isinstance(p[1], str) and p[1] not in variables:
        syntactic_errors.append(f"Semantic error, variable {p[1]} has not been initialized at line {p.lineno(1)}")
        return
    if isinstance(p[3], str) and p[3] not in variables:
        syntactic_errors.append(f"Semantic error, variable {p[3]} has not been initialized at line {p.lineno(3)}")
        return
    if isinstance(p[1], str):
        p[1] = variables[p[1]]
    if isinstance(p[3], str):
        p[3] = variables[p[3]]
    if type(p[1]).__name__ == "int" or type(p[1]).__name__ == "float":
        pass
    else:
        syntactic_errors.append(f"Semantic error, uncompatible type: {type(p[1]).__name__} at line {p.lineno(1)}")
        return
    if type(p[3]).__name__ == "int" or type(p[3]).__name__ == "float":
        pass
    else:
        syntactic_errors.append(f"Semantic error, uncompatible type: {type(p[3]).__name__} at line {p.lineno(3)}")
        return

def p_logicExpressions(p):
    '''logicExpressions : logicExpression
                        | logicExpression lConector logicExpressions'''

def p_logicExpression(p):
    'logicExpression : value compOperator value'
    if isinstance(p[1], str) and p[1] not in variables:
        syntactic_errors.append(f"Semantic error, variable {p[1]} has not been initialized at line {p.lineno(1)}")
        return
    if isinstance(p[3], str) and p[3] not in variables:
        syntactic_errors.append(f"Semantic error, variable {p[3]} has not been initialized at line {p.lineno(3)}")
        return
    if isinstance(p[1], str):
        p[1] = variables[p[1]]
    if isinstance(p[3], str):
        p[3] = variables[p[3]]
    if type(p[1]) == type(p[3]):
        pass
    else:
        syntactic_errors.append(f"Semantic error, uncompatible types: {type(p[1]).__name__} and {type(p[3]).__name__} at line {p.lineno(1)}")
        return

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
             | BOOL'''
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

def p_error(p):
    if p:
        syntactic_errors.append(f"Syntax error at '{p.value}' on line {p.lineno}")
    else:
        syntactic_errors.append("Syntax error at EOF")

parser = yacc.yacc()
