class Token:
    def __init__(self, tokenName:str, tokenLine:str):
        self.name = tokenName
        self.type:str
        self.lineNum = tokenLine

def readFile(fileName: str):
    tokens = []
    try:
        f = open(fileName,"r")
    except OSError:
        print("Could not open", end=" ")
        print(fileName)
        return []
    data = f.read()
    word = ""
    line = 1
    for c in data:
        if c != ' ' and c != '\n':
            word += c
        else:
            if word:
                token = Token(word, line)
                tokens.append(token)
                word = ""
            if c == '\n':
                line += 1
    if word:
        token = Token(word, line)
        tokens.append(token)
    
    f.close()
    return tokens
    
tmp = readFile("a.txt")
for t in tmp:
    print(t.name, t.lineNum)
