class Token:
    def __init__(self, tokenName: str, tokenLine: int):
        self.name = tokenName
        self.type = ""
        self.lineNum = tokenLine

def printTokens(tokens: list, mode: bool):
    if mode:
        display = [["name","type","line"]]
        line = []
        for token in tokens:
            line.append(token.name)
            line.append(token.type)
            line.append(token.lineNum)
            display.append(line)
            line = []
        for line in display:
            print('{:>40} {:>30} {:>30}'.format(*line))
    else:
        for token in tokens:
            print("name:", token.name)
            print("type:", token.type)
            print("line:", token.lineNum)
            print()

def readFile(fileName: str):
    tokens = []
    try:
        f = open(fileName,"r")
    except OSError:
        print("Could not open", end=" ")
        print(fileName)
        return []
    data = f.read()
    name = ""
    line = 1
    inSequnece = None
    i = 0
    while i < data.__len__():
        if (data[i] == '\'' or data[i] =='\"') and not inSequnece:
            inSequnece = data[i]
            name += data[i]
            i += 1
            while i < data.__len__():
                name += data[i]
                if data[i] != inSequnece: i += 1
                else: break
            tokens.append(Token(name,line))
            name = ""
            inSequnece = None
            i += 1
            continue

        if data[i] != ' ' and data[i] != '\n':
            name += data[i]
        else:
            if name:
                tokens.append(Token(name,line))
                name = ""
            if data[i] == '\n':
                line += 1
        i += 1

    if name:
        token = Token(name, line)
        tokens.append(token)
    
    f.close()
    return tokens

tokens = readFile("a.txt")
printTokens(tokens, 1)


'''LEGACY
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
'''