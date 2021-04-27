from readfile import *

keywords = [
    "nil", "true", "false", "self", "super", "thisContext"
]
operators = [
    "+", "-", "*", "/", "//", "\\"
]
logicalOperators = []
bitWiseOperators = []
comparisonOperators = []

def processToken(tokens: list):
    for token in tokens:
        if token.name in keywords:
            token.type = "KEYWORD"
        elif token.name in operators:
            token.type = "OPERATOR"
        elif token.name in logicalOperators:
            token.type = "LOGICAL OPERATOR"
        elif token.name in bitWiseOperators:
            token.type = "BIT-WISE OPERATOR"
        elif token.name in comparisonOperators:
            token.type = "COMPARISON OPERATOR"
        else:
            exit(0)
'''
tmp = readFile("a.txt")
for t in tmp:
    print(t.name, t.lineNum)
'''