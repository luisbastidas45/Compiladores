import ply.lex as lex
import sys

# lista de tokens
tokens = (
    # Reserverd words
    'ABSOLUTE',
    'ARRAY',
    'BEGIN', 
    'CONST',
    'DESTRUCTOR',
    'DIV',
    'DOWNTO',
    'END',
    'FOR',
    'FUNTION',
    'IF',
    'IN',
    'INTERFACE',
    'LABEL',
    'NIL', 
    'OBJECT',
    'OR',
    'PRIVATE',
    'PROGRAM',
    'REPEAT',
    'SHL',
    'STRING',
    'TO',
    'UNIT',
    'USES',
    'VIRTUAL',
    'WITH',
    'AND',
    'ASM',
    'CASE',
    'CONSTRUCTOR',
    'EXTERNAL',
    'DO',
    'ELSE',
    'FILE',
    'FORWARD',
    'GOTO',
    'IMPLEMENTATION',
    'INLINE',
    'INTERRUPT',
    'MOD',
    'NOT',
    'OF',
    'PACKED',
    'PROCEDURE',
    'RECORD',
    'SET',
    'SHR',
    'THEN',
    'TYPE',
    'UNTIL',
    'VAR',
    'WHILE',
    'XOR',
   
    # Symbols
    'PLUS',
    'PLUSPLUS',
    #'PLUSEQUAL',
    'MINUS',
    'MINUSMINUS',
    #'MINUSEQUAL',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'ASSING',
    'DEQUAL',
    'DISTINT',
    'ISEQUAL',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'HASHTAG',
    'DOT',
    

    # Others   
    'ID', 
    'NUMBER',
)

# Regular expressions rules for a simple tokens 
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_ASSING = r':='
t_DISTINT = r'!'
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'


def t_ABSOLUTE(t):
    r'absolute'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_BEGIN(t):
    r'begin'
    return t

def t_CONST(t):
    r'const'
    return t

def t_DESTRUCTOR(t):
    r'destructor'
    return t

def t_DIV(t):
    r'div'
    return t


def t_DOWNTO(t):
    r'downto'
    return t

def t_END(t):
    r'end'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_IF(t):
    r'if'
    return t

def t_IN(t):
    r'in'
    return t

def t_INTERFACE(t):
    r'interface'
    return t

def t_LABEL(t):
    r'label'
    return t

def t_NIL(t):
    r'nil'
    return t

def t_OBJECT(t):
	r'object'
	return t

def t_OR(t):
    r'or'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_PROGRAM(t):
	r'program'
	return t

def t_REPEAT(t):
    r'repeat'
    return t

def t_SHL(t):
	r'shl'
	return t
	
def t_STRING(t):            
	r"'[\w\.\d\,\:\" ]*'"
	return t

def t_TO(t):
	r'to'
	return t

def t_UNIT(t):
	r'unit'
	return t

def t_USES(t):
	r'uses'
	return t

def t_VIRTUAL(t):
	r'virtual'
	return t

def t_WITH(t):
	r'with'
	return t

def t_AND(t):
	r'and'
	return t

def t_ASM(t):
	r'asm'
	return t

def t_CASE(t):
	r'case'
	return t

def t_CONSTRUCTOR(t):
	r'constructor'
	return t

def t_EXTERNAL(t):
	r'external'
	return t

def t_DO(t):
	r'do'
	return t

def t_ELSE(t):
	r'else'
	return t

def t_FILE(t):
	r'file'
	return t

def t_FORWARE(t):
	r'forware'
	return t

def t_GOTO(t):
	r'goto'
	return t

def t_IMPLEMENTATION(t):
	r'implementation'
	return t

def t_INLINE(t):
	r'inline'
	return t

def t_INTERRUPT(t):
	r'interrupt'
	return t

def t_MOD(t):
	r'mod'
	return t

def t_NOT(t):
	r'not'
	return t

def t_OF(t):
	r'of'
	return t

def t_PACKED(t):
	r'packed'
	return t

def t_PROCEDURE(t):
	r'procedure'
	return t

def t_RECORD(t):
	r'record'
	return t

def t_SET(t):
	r'set'
	return t

def t_SHR(t):
	r'shr'
	return t

def t_THEN(t):
	r'then'
	return t

def t_TYPE(t):
	r'type'
	return t

def t_UNTIL(t):
	r'ultil'
	return t    

def t_VAR(t):
	r'var'
	return t

def t_WHILE(t):
	r'while'
	return t

def t_XOR(t):
	r'xor'
	return t




def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):  
    r'\w+(_\d\w)*'
    return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'!='
	return t

def t_ISEQUAL(t):
	r'=='
	return t
    
def t_MINUSMINUS(t):
	r'--'
	return t

def t_PLUSPLUS(t):
	r'\+\+'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    print ("new line")

t_ignore = ' \t'

def t_comments(t):
    r"{(.)*}"
    t.lexer.lineno += t.value.count('\n')
    print (t) 

def t_comments_C99(t):      
    r'\(\*(.)*\*\)'
    t.lexer.lineno += 1

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba2.pas'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	#input()

