class Token:
    def __init__(self, tokenName: str, inArr: bool, tokenLine:int, tokenType = ""):
        self.name = tokenName
        self.inArray = inArr
        self.lineNum = tokenLine
        self.type = tokenType

def printTokens(tokens: list, mode: int): #if mode = 1 or 2, display may have some bugs when a token has newline in its name
    print("Note: Byte error occurs when an element in byte array is not an interger.\n")
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
            print('{:>50} {:>30} {:>30}'.format(*line))
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
                for i in range (0, displayArr.__len__()):
                    line.append(displayArr[i])
                    if i != displayArr.__len__()-1:
                        line.append("x")
                        line.append("x")
                        line.append("x")
                        display.append(line)
                        line = []
                    else:
                        if token.inArray:
                            line.append("YES")
                        else:
                            line.append("NO")
                        line.append(token.type)
                        line.append(token.lineNum)
                        display.append(line)
                        line = []
                continue
            if token.inArray:
                line.append("YES")
            else: line.append("NO")
            line.append(token.type)
            line.append(token.lineNum)
            display.append(line)
            line = []
        for line in display:
            print('{:>50} {:>20} {:>20} {:>20}'.format(*line))

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
        if data[i] == '.' and not name and not inSequnece:
            tokens.append(Token(".", False, line, "STATEMENT SEPERATOR"))
            i += 1
            continue

        if data[i] == '[' and name != "#":
            if name:
                tokens.append(Token(name, False, line))
                name = ""
            tokens.append(Token('[', False, line, "LEFT SQU.BRACKET"))
            i += 1
            continue

        if data[i] == ']' and not name and not inSequnece:
            tokens.append(Token("]", False, line, "RIGHT SQU.BRACKET"))
            i += 1
            continue

        if data[i] == '(' and name != "#":
            if name:
                tokens.append(Token(name, False, line))
                name = ""
            tokens.append(Token('(', False, line, "LEFT PARENTHESE"))
            i += 1
            continue

        if data[i] == ')' and not name and not inSequnece:
            tokens.append(Token(")", False, line, "RIGHT PARENTHESE"))
            i += 1
            continue
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
                if data[i+1] == '\n': line += 1
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
                    sep = False
                    tokenType = "SYMBOL"
                    name += "#\'"
                    i += 2
                    while i < data.__len__():
                        name += data[i]
                        if data[i] == '.': break
                        if data[i] != '\'': i += 1
                        else: break
                    if i >= data.__len__():
                        tokenType = "ERROR"
                    if i+1 < data.__len__():
                        if data[i+1] == '.':
                            sep = True
                        elif data[i+1] != ' ' and data[i+1] != '\n' and data[i+1] != '.':
                            tokenType = "ERROR"
                        if data[i+1] == '\n': line += 1

                    if tokenType != "ERROR":
                        #if sep: name = name[0:name.__len__()-1]
                        tokens.append(Token(name, False, line, tokenType))
                        if sep: 
                            tokens.append(Token('.', False, line, 'STATEMENT SEPERATOR'))
                            i += 1
                        name = ""
                        inSequnece = None
                        tokenType = ""
                    i += 1
                    continue 

                elif data[i+1] == '[':
                    name += '#['
                    i += 2
                    while i < data.__len__():
                        name += data[i]
                        i += 1
                        if data[i-1] == '\n' or data[i-1] == ']': break
                    if data[i-1] == ']':
                        if i < data.__len__():
                            if data[i] == ' ' or data[i] == '\n' or data[i] == '.':
                                tokens.append(Token(name, False, line, "BYTE ARRAY"))
                                name = name[2:name.__len__()-1]
                                inspectArray(name, line, tokens, True)
                                name = ""
                                if data[i] == '\n': line += 1
                                if data[i] == '.': 
                                    tokens.append(Token('.', False, line, "STATEMENT SEPERATOR"))
                                    i += 1
                                    continue
                    if i > data.__len__() or data[i-1] == '\n':
                        subName = name
                        if data[i-1] == '\n':
                            subName = name[0:name.__len__()-1]
                        snArr = subName.split(sep = ' ')
                        for sn in snArr:
                            if sn:
                                tokens.append(Token(sn, False, line))
                        if data[i-1] == '\n': line += 1
                        name = ""
                    continue

                elif data[i+1] == '(':
                    bracketCount = 1
                    name += "#("
                    i += 2
                    sep = False
                    while i < data.__len__():
                        name += data[i]
                        i += 1
                        if data[i-1] == '(': bracketCount += 1
                        if data[i-1] == ')': bracketCount -= 1 
                        if data[i-1] == '\n': 
                            i -= 1
                            name = name[0:name.__len__()-1]
                            break
                        if bracketCount == 0: 
                            break
                    tokenType = "CONSTANT ARRAY"
                    if bracketCount != 0:
                        tokenType = ""
                    if i < data.__len__():
                        if data[i] != ' ' and data[i] != '\n' and data[i] != '.':
                            tokenType = ""
                        elif data[i] == '.':      
                            sep = True
                    if tokenType:             
                        tokens.append(Token(name, False, line, tokenType))
                        if i < data.__len__():
                            if data [i] == '\n': line += 1
                        name = name[2:name.__len__()-1]    
                        inspectArray(name, line, tokens)
                        name = ""
                        tokenType = ""
                        if sep:
                            tokens.append(Token(".", False, line, 'STATEMENT SEPERATE'))
                        i += 1
                    continue
                
        if data[i] != ' ' and data[i] != '\n':
            name += data[i]
        else:
            if name:
                tmpArr = []
                while name[name.__len__()-1] == '.' or name[name.__len__()-1] == ')' or name[name.__len__()-1] == ']':
                    tmpArr.append(name[name.__len__()-1])
                    name = name[0:name.__len__()-1]
                if '.' in name:
                    tmp = name.split(sep = '.')
                    if tmp.__len__() == 2:
                        if representsInt(tmp[0]) and representsInt(tmp[1]):
                            tokens.append(Token(name, False, line, "FLOAT"))
                            for t in reversed(tmpArr):
                                tokens.append(Token(t, False, line,))
                            name = ""
                            continue
                if ' ' in name:
                    snArr = name.split(sep = ' ')
                    for sn in snArr:
                        if sn:
                            tokens.append(Token(sn, False, line))
                    for t in reversed(tmpArr):
                                tokens.append(Token(t, False, line,))
                else: 
                    tokens.append(Token(name, False, line))
                    for t in reversed(tmpArr):
                                tokens.append(Token(t, False, line,))
                name = ""
                tokenType = ""
                if inSequnece: inSequnece = None
            if data[i] == '\n':
                line += 1
        i += 1

    if name:
        tmpArr = []
        while name[name.__len__()-1] == '.' or name[name.__len__()-1] == ')' or name[name.__len__()-1] == ']':
            tmpArr.append(name[name.__len__()-1])
            name = name[0:name.__len__()-1]
        if '.' in name:
            tmp = name.split(sep = '.')
            if tmp.__len__() == 2:
                if representsInt(tmp[0]) and representsInt(tmp[1]):
                    tokens.append(Token(name, False, line, "FLOAT"))
                    for t in reversed(tmpArr):
                        tokens.append(Token(t, False, line,))
                    name = ""
                    return 
        if ' ' in name:
            snArr = name.split(sep = ' ')
            for sn in snArr:
                if sn:
                    tokens.append(Token(sn, False, line))
            for t in reversed(tmpArr):
                tokens.append(Token(t, False, line,))
        else: 
            tokens.append(Token(name, False, line))
            for t in reversed(tmpArr):
                tokens.append(Token(t, False, line,))
    
    f.close()
    return tokens

def inspectArray(array: str, line: int, ret: list, inByteArr = False):
    word = ""
    inSequnece = None
    i = 0
    bracketCount = 0
    while i < array.__len__():
        if array[i] == '#' and not inByteArr:
            word += '#'
            i += 1
            continue
        if array[i] == '\'' and not inSequnece and (not word or word == '#') and not inByteArr:
            inSequnece = array[i]
            word += array[i]
            i += 1
            while i < array.__len__():
                word += array[i]
                i += 1
                if array[i-1] == inSequnece: break
            if word[0] != '#':
                ret.append(Token(word, True, line, "STRING"))
            else: ret.append(Token(word, True, line, "SYMBOL"))
            word = ""
            inSequnece = None
            i += 1
            continue

        if array[i] == '[' and (not word or word[0] == '#') and not inByteArr:
            tokenType = "BYTE ARRAY"
            while i < array.__len__():
                word += array[i]
                i += 1
                if array[i-1] == ']': break
            if i >= array.__len__():
                tokenType = "ERROR"
                ret.append(Token(word, True, line, tokenType))
            if tokenType != "ERROR":
                ret.append(Token(word, True, line, tokenType))
                if word[0] != '#':
                    inspectArray(word[1:word.__len__()-1], line, ret, True)
                else:
                    inspectArray(word[2:word.__len__()-1], line, ret, True)
                word = ""
            continue

        if array[i] == '(' and (not word or word == '#') and not inByteArr:
            while i < array.__len__():
                word += array[i]
                i += 1
                if array[i-1] == '(': bracketCount += 1
                if array[i-1] == ')': bracketCount -= 1
                if bracketCount == 0:
                    ret.append(Token(word, True, line, "CONSTANT ARRAY"))
                    if word[0] != '#':
                        inspectArray(word[1:word.__len__()-1], line, ret)
                    else:
                        inspectArray(word[2:word.__len__()-1], line, ret)
                    word = ""
                    break
                    i += 1 
            continue

        if array[i] != ' ':
            word += array[i]
        else:
            if word:
                if not inByteArr:
                    ret.append(Token(word, True, line))
                else:
                    if representsInt(word):
                        ret.append(Token(word, True, line, "INTEGER"))
                    else:
                        ret.append(Token(word, True, line, "BYTE ERROR"))
            word = ""     
        i += 1

    if word:
        if not inByteArr:
            ret.append(Token(word, True, line))
        else:
            if representsInt(word):
                ret.append(Token(word, True, line, "INTEGER"))
            else:
                ret.append(Token(word, True, line, "BYTE ERROR"))      

def representsInt(s: str):
    try: 
        int(s)
        return True
    except ValueError:
        return False

tokens = readFile("a3.txt")
printTokens(tokens, 2)

for token in tokens:
    print(token.name + ' ' + token.type)

tokens = readFile("a.txt")
printTokens(tokens, 2)

for token in tokens:
    print(token.name + ' ' + token.type)

tokens = readFile("a2.txt")
printTokens(tokens, 2)

for token in tokens:
    print(token.name + ' ' + token.type)