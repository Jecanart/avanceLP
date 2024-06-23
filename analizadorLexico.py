import ply.lex as lex
from datetime import datetime

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
            "while": "WHILE",
            "string":"STRING",
            "println":"PRINTLN"
             }

tokens = (
    "PRINTSTRING",
    "VARIABLE",
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
    'LLLAVE',
    'RLLAVE',
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
    'NOT',
    "COMMENT",
    "MULTILINE_COMMENT",
)+tuple(reserved.values())

#Tokens generales
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'\/'
t_MOD     = r'%'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
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

def t_FLOAT(t):
    r'(\d+\.\d*|\d*\.\d+)'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_BOOL(t):
    r'(true|false)'
    t.value = bool(t.value)
    return t

def t_PRINTSTRING(t):
    r'"([^\\\n]|(\\.))*?{([a-zA-Z_][a-zA-Z0-9_]*)*}+([^\\\n]|(\\.))*?"'

def t_STRING(t):
    r'"([^\\\n]|(\\.))*?"'
    t.value = bool(t.value)
    return t

#los comentarios deben ser ignorados
def t_COMMENT(t):
    r'//.*'
    pass  

def t_MULTILINE_COMMENT(t):
    r'/\*([^*]|\*+[^*/])*\*+/'
    pass  




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

algoritmo_Canarte = """
use std::io; // Importa el módulo std::io para manejar la entrada y salida estándar 

  

fn main() { 

    println!("Calculadora de área de triángulo"); 

  

    // Solicitar la base del triángulo al usuario 

    println!("Ingrese la base del triángulo:"); 

    let mut entrada_base = String::new(); // Crear una nueva cadena vacía 

    io::stdin().read_line(&mut entrada_base).expect("Error al leer la entrada"); // Leer la entrada del usuario 

    let base: f64 = entrada_base.trim().parse().expect("Por favor ingrese un número válido"); // Convertir la entrada a un número de coma flotante 

  

    // Solicitar la altura del triángulo al usuario 

    println!("Ingrese la altura del triángulo:"); 

    let mut entrada_altura = String::new(); // Crear una nueva cadena vacía 

    io::stdin().read_line(&mut entrada_altura).expect("Error al leer la entrada"); // Leer la entrada del usuario 

    let altura: f64 = entrada_altura.trim().parse().expect("Por favor ingrese un número válido"); // Convertir la entrada a un número de coma flotante 

  

    // Calcular el área del triángulo 

    let area = calcular_area_triangulo(base, altura); 

  

    // Mostrar el resultado 

    println!("El área del triángulo con base {} y altura {} es: {}", base, altura, area); 

} 

  

// Función para calcular el área del triángulo 

fn calcular_area_triangulo(base: f64, altura: f64) -> f64 { 

    (base * altura) / 2.0  

} 
"""

algoritmo_Macias = """
use std::io; // Importa el módulo std::io para manejar la entrada y salida estándar

fn main() {
    println!("Identificador de tipo de triángulo");

    // Solicitar el primer lado del triángulo al usuario
    println!("Ingrese el primer lado del triángulo:");
    let lado1 = leer_entrada();

    // Solicitar el segundo lado del triángulo al usuario
    println!("Ingrese el segundo lado del triángulo:");
    let lado2 = leer_entrada();

    // Solicitar el tercer lado del triángulo al usuario
    println!("Ingrese el tercer lado del triángulo:");
    let lado3 = leer_entrada();

    // Determinar el tipo de triángulo
    let tipo = determinar_tipo_triangulo(lado1, lado2, lado3);

    // Mostrar el resultado
    println!(
        "El triángulo con lados {}, {}, {} es: {}",
        lado1, lado2, lado3, tipo
    );
}

// Función para leer y convertir la entrada del usuario a un número de coma flotante
fn leer_entrada() -> f64 {
    let mut entrada = String::new(); // Crear una nueva cadena vacía
    io::stdin()
        .read_line(&mut entrada)
        .expect("Error al leer la entrada"); // Leer la entrada del usuario
    entrada.trim().parse().expect("Por favor ingrese un número válido") // Convertir la entrada a un número de coma flotante
}

// Función para determinar el tipo de triángulo
fn determinar_tipo_triangulo(lado1: f64, lado2: f64, lado3: f64) -> &'static str {
    if lado1 == lado2 && lado2 == lado3 {
        "Equilátero"
    } else if lado1 == lado2 || lado1 == lado3 || lado2 == lado3 {
        "Isósceles"
    } else {
        "Escaleno"
    }
}
"""

def logOutput(user, a_input):
    lexer.input(a_input)
    datime = datetime.now()
    timeStamp = datime.strftime("%d%m%Y-%Hh%M")
    dirString = "logs/lexico-"+user+"-"+timeStamp+".txt"
    f = open(dirString, "w")
    while True:
        tok = lexer.token()
        if not tok: 
            break    
        linea = str(tok) 
        f.write(linea+"\n")

#logOutput("Jecanart", algoritmo_Canarte)


