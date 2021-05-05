from lexer import *

print("Enter input file's name:", end = " ")
fileName = input()
fileName = str(fileName)
#fileName = "a2.txt"
tokens, varList = readFile(fileName)
for index, token in enumerate(tokens):
    if token.type != "": continue
    if isId(token.name):
        next = index + 1
        if (next < len(tokens) and tokens[next].name == ":="):
            token.type = "VARIABLE"
            tokens[next].type = "ASSIGNMENT"
            token = tokens[next]
        else:    
            token.type = "ID"
    elif isRadixFloat(token.name) or isInt(token.name) or isFloat(token.name):
        token.type = "NUMBER"
    elif isMessID(token.name):
        token.type = "MESSAGE"
processTokens(tokens)
printTokens(tokens, 2)