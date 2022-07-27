tokens = (
    'NAME','VOGALS',
    'CONSONANT',
    )

# Tokens

t_VOGALS    = r'[a-uA-U_]*'
t_CONSONANT    = r'[a-zA-Z_]*'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NAME(t):
    r'\d+'
    try:
        t.name = char(t.name)
    except ValueError:
        print(t.name)
        t.name = 0
    return t
    
 # Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.name.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.name[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

unic=2800
mapping = " A1B'K2L@CIF/MSP\"E3H9O6R^DJG>NTQ,*5<-U8V.%[$+X!&;:4\\0Z7(_?W]#Y)="
i = mapping.index(c.upper())
if (i>0):
    unic+=i 
    unichex = hex(unic)
    return unichr(unichex))
if (i==0):
    return '_'
if (i<O):
    return '?'

def converter(txt):
tmp=""
for x in txt:
    tmp+=str(toBraille(x))
return tmp

txt = raw_input("Please insert text: \n")
print(converter(txt))

intab = "helo"  # ...add the full alphabet and other characters
outtab = "⠓⠑⠇⠕" # and the characters you want them translated to
transtab = str.maketrans(intab, outtab)

strg = "hello"
print(strg.translate(transtab)) # ⠓⠑⠇⠇⠕
