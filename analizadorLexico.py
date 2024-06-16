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
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MOD',
    'COMMA',
    'SEMICOLON',
    'PERIOD',
    'COLON',
    'EQUALS',
    'NOT_EQUALS',
    'LESSER',
    'GREATER',
    'LESSER_EQ',
    'GREATER_EQ',
    'ASSIGN',
    'PLUS_ASSIGN',
    'MINUS_ASSIGN',
    'TIMES_ASSIGN',
    'DIVIDE_ASSIGN',
    'MOD_ASSIGN',
    'AND',
    'OR',
    'NOT'
)+tuple(reserved.values())

#Tokens generales
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'\/'
t_MOD     = r'%'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COMMA   = r','
t_SEMICOLON = r';'
t_PERIOD  = r'\.'
t_COLON   = r':'

# Operadores de comparación
t_EQUALS     = r'=='
t_NOT_EQUALS = r'!='
t_LESSER     = r'<'
t_GREATER    = r'>'
t_LESSER_EQ  = r'<='
t_GREATER_EQ = r'>='

# Operadores de asignación
t_ASSIGN         = r'='
t_PLUS_ASSIGN    = r'\+='
t_MINUS_ASSIGN   = r'-='
t_TIMES_ASSIGN   = r'\*='
t_DIVIDE_ASSIGN  = r'\/='
t_MOD_ASSIGN     = r'%='

# Operadores lógicos
t_AND      = r'&&'
t_OR       = r'\|\|'
t_NOT      = r'!'



def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'VARIABLE')
    return t 

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_FLOAT(t):
    r'[-]?[0-9]*\.[0-9]*'
    t.value = float(t.value)
    return t

def t_BOOL(t):
    r'(true|false)'
    t.value = bool(t.value)
    return t



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

lexer = lex.lex()

algoritmo_Torres = """
use std::io; 

use std::io::Write; 

  

fn main() { 

    // Numero fijo de entradas que el usuario debe proporcionar 

    const NUM_ENTRADAS: usize = 5; 

  

    // Declaracion de un vector para almacenar los numeros 

    let mut numeros: Vec<i32> = Vec::new(); 

  

    println!("Introduce {} numeros enteros:", NUM_ENTRADAS); 

  

    // Leer numeros del usuario 

    for _ in 0..NUM_ENTRADAS { 

        print!("Numero: "); 

        io::stdout().flush().unwrap(); // Asegura que el mensaje se imprima antes de leer la entrada 

  

        let mut entrada = String::new(); 

        io::stdin().read_line(&mut entrada).expect("Error al leer la línea"); 

  

        let entrada = entrada.trim(); // Elimina espacios en blanco al principio y al final 

  

        // Intentar convertir la entrada en un numero entero 

        match entrada.parse::<i32>() { 

            Ok(numero) => numeros.push(numero), // Agregar el numero al vector si la conversion es exitosa 

            Err(_) => { 

                println!("Por favor, introduce un numero entero válido."); 

                return; // Termina el programa si la entrada no es valida 

            } 

        } 

    } 

  

    // Calcular la suma y el promedio de los numeros 

    let suma: i32 = numeros.iter().sum(); 

    let conteo: usize = numeros.len(); 

    let promedio: f64 = suma as f64 / conteo as f64; 

  

    // Mostrar los resultados 

    println!("Suma: {}", suma); 

    println!("Conteo: {}", conteo); 

    println!("Promedio: {:.2}", promedio); 

} 
"""

lexer.input(algoritmo_Torres)



# Tokenize

while True:
    tok = lexer.token()
    if not tok: 
        break    
    print(tok)