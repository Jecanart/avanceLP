import tkinter as tk
from tkinter import scrolledtext
from analizadorLexico import lexer, lexical_errors
from analizadorSintactico import parser, syntactic_errors, variables, mutables

def analyze_code():
    code = code_input.get("1.0", "end-1c")
    
    # Reiniciar las variables
    variables.clear()
    mutables.clear()

    # Reiniciar los errores
    lexical_errors.clear()
    syntactic_errors.clear()
    
    # Análisis léxico
    lexer.input(code)

    #Mostrar Tokens
    error_output.delete("1.0", "end")
    error_output.insert("end", f"\n")
    error_output.insert("end", f"Tokens encontrados:\n")
    error_output.insert("end", f"\n")

    while True:
        tok = lexer.token()
        if not tok:
            break
        error_output.insert("end", f"Token('{tok.type}', '{tok.value}')\n")

    # Análisis sintáctico
    parser.parse(code)
    
    # Mostrar errores
    if lexical_errors or syntactic_errors:
        if lexical_errors:
            error_output.insert("1.0", "Errores Léxicos:\n" + "\n".join(lexical_errors) + "\n")
        if syntactic_errors:
            error_output.insert("1.0", "Errores Sintácticos:\n" + "\n".join(syntactic_errors)+ "\n")
    else:
        error_output.insert("1.0", "No se han detectado problemas\n")

root = tk.Tk()
root.title("Análisis léxico, semántico y sintáctico de código en Rust")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

code_label = tk.Label(frame, text="Ingrese su código aquí:")
code_label.pack(anchor='w')

code_input = scrolledtext.ScrolledText(frame, height=20, width=80)
code_input.pack()

analyze_button = tk.Button(frame, text="Analizar", command=analyze_code)
analyze_button.pack(pady=10)

error_label = tk.Label(frame, text="Análisis:")
error_label.pack(anchor='w')

error_output = scrolledtext.ScrolledText(frame, height=10, width=80)
error_output.pack()

root.mainloop()