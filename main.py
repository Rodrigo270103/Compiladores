# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# r'atring' -> r significa que la cadena es tradada sin caracteres de escape, 
# es decir r'\n' seria un \ seguido de n (no se interpretaria como salto de linea) 

 # List of token names.   This is always required
reserved = {
    'verdaredo': 'TYPE_BOOLEANO_V',
    'falso': 'TYPE_BOOLEANO_F',
    'para': 'TYPE_FOR',
    'si' : 'TYPE_IF',
    'mientras' : 'TYPE_WHILE',
    'definir' : 'TYPE_DEF',
    'en' : 'TYPE_IN',
    'sino': 'TYPE_ELSE',
    'imprimir': 'TYPE_PRINT',
    'rango': 'TYPE_RANGE',
    'retorna': 'TYPE_RETURN',
    'ingrese': 'TYPE_INPUT',
    'sino' : 'TYPE_ELSE',
  
}

tokens = [
    'ID',
    'NUM',
    'LITERAL',
    'BOOLEANO',
    'OP_SUMA',
    'OP_RESTA',
    'OP_IGUAL',
    'OP_MULTIPLICACION',
    'OP_DIVISION',
    'OPEN_PARENTESIS',
    'CLOSE_PARENTESIS',
    'OP_PUNTO',
    'OPEN_KEY',
    'CLOSE_KEY',
    'OPEN_BRACKET',
    'CLOSE_BRACKET',
    'OP_PYC',
    'OP_MAYOR',
    'OP_MENOR',
    'OP_MAYOR_IGUAL',
    'OP_MENOR_IGUAL',
    'OP_COMA',
    'OP_AMPERSAND',
    'OP_RESIDUO',
    'OP_IGUALDAD',
    'OP_DESIGUALDAD',
    'OP_MULT_IGUAL'
]+ list(reserved.values())

 # Regular expression rules for simple tokens
t_OP_SUMA    = r'\+'
t_OP_RESTA   = r'-'
t_OP_IGUAL   = r'\='
t_OP_MULTIPLICACION   = r'\*'
t_OP_DIVISION  = r'/'
t_OPEN_PARENTESIS  = r'\('
t_CLOSE_PARENTESIS  = r'\)'
t_BOOLEANO = r'verdadero|falso'
t_OP_PUNTO = r'\.'
t_OPEN_KEY = r'\{'
t_CLOSE_KEY = r'\}'
t_OPEN_BRACKET = r'\['
t_CLOSE_BRACKET = r'\]'
t_OP_PYC = r'\;'
t_OP_MAYOR = r'\>'
t_OP_MENOR = r'\<'
t_OP_MAYOR_IGUAL = r'\>='
t_OP_MENOR_IGUAL = r'\<='
t_OP_COMA = r'\,'
t_OP_AMPERSAND = r'\&'
t_OP_RESIDUO = r'\%'
t_OP_IGUALDAD = r'\=='
t_OP_DESIGUALDAD = r'\!='
t_OP_MULT_IGUAL = r'\*='



#t_LITERAL r'(\'[^\']*\'|\"[^\"]*\")'
def t_LITERAL(t):
  r'(\'[^\']*\'|\"[^\"]*\")'
  t.value = t.value[1:-1]  # Quita las comillas del inicio y el final
  return t

 # A regular expression rule with some action code

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)  # guardamos el valor del lexema  
    #print("se reconocio el numero")
    return t

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  t.type = reserved.get(t.value, 'ID')  # Check for reserved words
  return t


 # Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

 # Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
with open('main1.as', 'r') as archivo:
  contenido = archivo.read()

# Give the lexer some input
lexer.input(contenido)
# Tokenize
tokens_info = []

#--------------- Test it out--------------------------------------------------------

'''
definir factorial_iterativo(n){
resultado = 1
para i en rango(1, n+1){
resultado *= i
}
numero = 5
factorial = factorial_iterativo(numero)
imprimir ("El factorial es:")
imprimir(factorial)

'''


# Give the lexer some input
#lexer.input(data)
#-------------------------------------------------------------------------------------
class Token:
  def __init__(self, type, lexeme, line, column):
      self.type = type
      self.lexeme = lexeme
      self.line = line
      self.column = column

lista_tokens = []


while True:
  tok = lexer.token()
  if not tok: 
      break  

  
  t = Token(tok.type, tok.value, tok.lineno, tok.lexpos)
  lista_tokens.append(t)

for token in lista_tokens:
    print("Tipo:", token.type)
    print("Lexema:", token.lexeme)
    print("Línea:", token.line)
    print("Columna:", token.column)
    print("-----------------------")


