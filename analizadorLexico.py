import ply.lex as lex

reserved = {"as": "AS",
            "async" : "ASYNC",
            "await" : "AWAIT",
            "break" : "BREAK",
            "const" : "CONST",
            "continue": "CONTINUE",
            "crate" : "CRATE",
            "dyn" : "DYN",
            "else" : "ELSE",
            "enum" : "ENUM",
            "extern" : "EXTERN",
            "false" : "FALSE",
            "fn" : "FN",
            "for" : "FOR",
            "if" : "IF",
            "impl" : "IMPL",
            "in" : "IN",
            "let" : "LET",
            "loop" : "LOOP",
            "match" : "MATCH",
            "mod" : "MOD",
            "move" : "MOVE",
            "mut" : "MUT",
            "pub" : "PUB",
            "ref" : "REF",
            "return" : "RETURN",
            "self" : "SELF",
            "static" : "STATIC",
            "struct" : "STRUCT",
            "super" : "SUPER",
            "trait" : "TRAIT",
            "true" : "TRUE",
            "type" : "TYPE",
            "unsafe" : "UNSAFE",
            "use" : "USE",
            "where" : "WHERE",
            "while": "WHILE"
             }

tokens = (
    "FLOAT",
    "INTEGER",
    "CHAR",
    "BOOL",
    "CPOINTER",
    "REFERENCE",
)+tuple(reserved.values())

#Definicion token INTEGER John Cañarte
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'VARIABLE')
    return t 

def t_FLOAT(t):
    r'[-]?[0-9]*\.[0-9]*'
    t.value = float(t.value)
    return t

lexer = lex.lex()

data = "12"

lexer.input(data)



#Reglas generales
# Saltos de linea

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espacios y TAB

t_ignore  = ' \t'

# Errores

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Tokenize

while True:
    tok = lexer.token()
    if not tok: 
        break    
    print(tok)