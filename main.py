from lexer import *

print("Enter input file's name:", end = " ")
fileName = input()
fileName = str(fileName)
#fileName = "a2.txt"
tokens, varList = readFile(fileName)
#processTokens(tokens, varList)
printTokens(tokens, 2)
