class Token:
    def __init__(self, tokenName: str, inArr: bool, tokenLine:int, tokenType = ""):
        self.name = tokenName
        self.inArray = inArr
        self.lineNum = tokenLine
        self.type = tokenType

def printTokens(tokens: list, mode: int): #if mode = 1 or 2, display may have some bugs when a token has newline in its name
    if mode == 1:
        display = [["NAME", "TYPE", "LINE"]]
        line = []
        for token in tokens:
            line.append(token.name)
            line.append(token.type)
            line.append(token.lineNum)
            display.append(line)
            line = []
        for line in display:
            print('{:>40} {:>30} {:>30}'.format(*line))
    elif mode == 0:
        for token in tokens:
            print("NAME:", token.name)
            print("TYPE:", token.type)
            print("LINE:", token.lineNum)
            print()
    elif mode == 2: 
        display = [["NAME", "INSIDE ARRAY", "TYPE", "LINE"]]
        line = []
        for token in tokens:
            if '\n' not in token.name:
                line.append(token.name)
            else: 
                displayArr = token.name.split(sep = '\n')
                print(displayArr)
                for i in range (0, displayArr.__len__()):
                    line.append(displayArr[i])
                    if i != displayArr.__len__()-1:
                        line.append("")
                        line.append("")
                        line.append("")
                        display.append(line)
                        line = []
                    else:
                        line.append(token.inArray)
                        line.append(token.type)
                        line.append(token.lineNum)
                        display.append(line)
                        line = []
                continue
            line.append(token.inArray)
            line.append(token.type)
            line.append(token.lineNum)
            display.append(line)
            line = []
        for line in display:
            print('{:>40} {:>20} {:>20} {:>20}'.format(*line))

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
    tokenType = ""
    while i < data.__len__():
        if (data[i] == '\'' or data[i] =='\"') and not inSequnece and not name:
            inSequnece = data[i]
            if inSequnece == '\'':
                tokenType = "STRING"
            else:
                tokenType = "COMMENT"    
            name += data[i]
            i += 1
            while i < data.__len__():
                name += data[i]
                if data[i] != inSequnece: i += 1
                else: break
            if i >= data.__len__():
                tokenType = "ERROR"
            if i+1 < data.__len__():
                if data[i+1] != ' ' and data[i+1] != '\n':
                    tokenType = "ERROR"
            if tokenType != "ERROR":
                tokens.append(Token(name, False, line, tokenType))
                name = ""
                inSequnece = None
                tokenType = ""
            i += 1
            continue

        if (data[i] == '#') and not name:
            if i + 1 < data.__len__():
                if data[i+1] == '\'':
                    tokenType = "SYMBOL"
                    name += "#\'"
                    i += 2
                    while i < data.__len__():
                        name += data[i]
                        if data[i] != '\'': i += 1
                        else: break
                    if i >= data.__len__():
                        tokenType = "ERROR"
                    if i+1 < data.__len__():
                        if data[i+1] != ' ' and data[i+1] != '\n':
                            tokenType = "ERROR"
                    if tokenType != "ERROR":
                        tokens.append(Token(name, False, line, tokenType))
                        name = ""
                        inSequnece = None
                        tokenType = ""
                    i += 1
                    continue 

                elif data[i+1] == '(':
                    bracketCount = 1
                    name += "#("
                    i += 2
                    while i < data.__len__():
                        name += data[i]
                        i += 1
                        if data[i-1] == '(': bracketCount += 1
                        if data[i-1] == ')': bracketCount -= 1 
                        if data[i-1] == '\n': break
                        if bracketCount == 0: break
                    tokenType = "CONSTANT ARRAY"
                    if bracketCount != 0:
                        tokenType = "ERROR"
                    if i < data.__len__():
                        if data[i] != ' ' and data[i] != '\n':
                            tokenType = "ERROR"
                    if tokenType != "ERROR":
                        tokens.append(Token(name, False, line, tokenType))
                        name = name[2:name.__len__()-1]
                        #subNames = []
                        inspectArray(name, line, tokens)
                        #for sn in subNames:
                            #tokens.append(Token(sn, True, line))
                        name = ""
                        tokenType = ""
                        i += 1
                    continue
                
                elif data[i+1] == '[':
                    while i < data.__len__():
                        name += data[i]
                        i += 1


        if data[i] != ' ' and data[i] != '\n':
            name += data[i]
        else:
            if name:
                tokens.append(Token(name, False, line, tokenType))
                name = ""
                tokenType = ""
                if inSequnece: inSequnece = None
            if data[i] == '\n':
                line += 1
        i += 1

    if name:
        tokens.append(Token(name, False, line))
    
    f.close()
    return tokens

def inspectArray(array: str, line: int, ret: list):
    word = ""
    inSequnece = None
    i = 0
    bracketCount = 0
    while i < array.__len__():
        if array[i] == '\'' and not inSequnece and not word:
            inSequnece = array[i]
            word += array[i]
            i += 1
            while i < array.__len__():
                word += array[i]
                i += 1
                if array[i-1] == inSequnece: break
            #ret.append(word)
            ret.append(Token(word, True, line, "CONSTANT STRING"))
            word = ""
            inSequnece = None
            i += 1
            continue
        
        if array[i] == '(' and not word:
            while i < array.__len__():
                word += array[i]
                i += 1
                if array[i-1] == '(': bracketCount += 1
                if array[i-1] == ')': bracketCount -= 1
                if bracketCount == 0:
                    ret.append(Token(word, True, line, "CONSTANT ARRAY"))
                    inspectArray(word[1:word.__len__()-1], line, ret)
                    word = ""
                    break
                    i += 1 
            continue

        if array[i] != ' ':
            word += array[i]
        else:
            if word:
               #ret.append(word)
               ret.append(Token(word, True, line))
            word = ""     
        i += 1
    if word:
        ret.append(Token(word, True, line))        

tokens = readFile("a.txt")
printTokens(tokens, 2)


