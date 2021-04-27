from readfile import *

keywords = [
    "nil", "true", "false", "self", "super", "thisContext"
]

def processToken(tokens: list):
    for token in tokens:
        if token.name in keywords:
            token.type = "KEYWORD"
'''
tmp = readFile("a.txt")
for t in tmp:
    print(t.name, t.lineNum)
'''