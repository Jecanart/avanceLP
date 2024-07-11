import ply.lex as lex

reserved = {
    "as": "AS", "async": "ASYNC", "await": "AWAIT", "break": "BREAK",
    "const": "CONST", "continue": "CONTINUE", "crate": "CRATE", "dyn": "DYN",
    "else": "ELSE", "enum": "ENUM", "extern": "EXTERN", "false": "FALSE",
    "fn": "FN", "for": "FOR", "if": "IF", "impl": "IMPL", "in": "IN",
    "let": "LET", "loop": "LOOP", "match": "MATCH", "move": "MOVE",
    "mut": "MUT", "pub": "PUB", "ref": "REF", "return": "RETURN",
    "self": "SELF", "static": "STATIC", "struct": "STRUCT", "super": "SUPER",
    "trait": "TRAIT", "true": "TRUE", "type": "TYPE", "unsafe": "UNSAFE",
    "use": "USE", "where": "WHERE", "while": "WHILE", "string": "STRING",
    "println": "PRINTLN", "linkedlist": "LINKEDLIST", "vec": "VEC", "new": "NEW",
    'i8': 'I8', 'i16': 'I16', 'i32': 'I32', 'i64': 'I64', 'i128': 'I128', 'u8': 'U8',
    'u16': 'U16', 'u32': 'U32', 'u64': 'U64', 'u128': 'U128', 'f32': 'F32', 'f64': 'F64',
    'char' : 'T_CHAR', 'bool' : 'BOOL' 
}

tokens = (
    "VARIABLE", "FLOAT", "INTEGER", "CHAR", "BOOLEAN", "CPOINTER", "REFERENCE",
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'LLLAVE', 'RLLAVE',
    'LBRACKET', 'RBRACKET', 'RPAREN', 'MOD', 'COMMA', 'SEMICOLON', 'PERIOD',
    'COLON', 'EQUALS', 'NOT_EQUALS', 'LESSER', 'GREATER', 'LESSER_EQ',
    'GREATER_EQ', 'ASSIGN', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'TIMES_ASSIGN',
    'DIVIDE_ASSIGN', 'MOD_ASSIGN', 'AND', 'OR', 'NOT', "COMMENT",
    "MULTILINE_COMMENT",
) + tuple(reserved.values())

# Tokens generales
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_MOD = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'
t_PERIOD = r'\.'
t_COLON = r':'

# Operadores de comparación
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_LESSER = r'<'
t_GREATER = r'>'
t_LESSER_EQ = r'<='
t_GREATER_EQ = r'>='

# Operadores de asignación
t_ASSIGN = r'='
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_TIMES_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'\/='
t_MOD_ASSIGN = r'%='

# Operadores lógicos
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'!'

lexical_errors = []

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

def t_FLOAT(t):
    r'(\d+\.\d*|\d*\.\d+)'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_BOOLEAN(t):
    r'(true|false)'
    t.value = bool(t.value)
    return t

def t_STRING(t):
    r'"([^\\\n]|(\\.))*?"'
    t.value = t.value
    return t

def t_COMMENT(t):
    r'\/\/.*'
    pass

def t_MULTILINE_COMMENT(t):
    r'/\*([^*]|\*+[^*/])*\*+/'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_eof(t):
    t.lexer.lineno = 1

t_ignore = ' \t'

def t_error(t):
    lexical_errors.append(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
