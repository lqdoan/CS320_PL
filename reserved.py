def representsInt(s: str):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def isId(s: str):
    if s:
        if s[0].isalpha():
            for i in range (1, s.__len__()):
                if not s[i].isalnum(): return False
            return True
    return False

def isInt(s: str):
    if 'e' in s:
        tmp = s.split(sep = 'e')
        if not isInt(tmp[0]): return False
        if not isInt(tmp[1]): return False
        return True
    if s[0] == "-":
        return representsInt(s[1:s.__len__()])
    else: return representsInt(s)

def isFloat(s: str):
    if isInt(s): return True
    if '.' in s:
        tmpF = s.split(sep = '.')
        if not isInt(tmpF[0]): return False
        if 'e' in tmpF[1]:
            tmpE = tmpF[1].split(sep = 'e')
            if not isInt(tmpE[0]): return False
            if not isInt(tmpE[1]): return False  
        elif not isInt(tmpF[1]): return False
    return True

def isRadixNum(s: str):
    tmps = s + ""
    if 'r' in tmps:
        tmp = tmps.split(sep = 'r')
        if tmp.__len__()==2:
            if representsInt(tmp[0]):
                tmp[0] = int(tmp[0])
                for t in tmp[1]:
                    if t.isdigit(): 
                        if int(t) > tmp[0]: return False 
                    elif t.isalpha():
                        if ord(t) < 65: 
                            print("invoke")
                            return False
                        if ord(t) - 55 > tmp[0]: return False
                    else: return False
            else: return False
        else: return False
    else: return False
    return True

def isRadixFloat(s: str):
    if isRadixNum(s): return True
    tmps = s + ""
    if 'e' in tmps:
        tmp0 = tmps.split(sep = 'e')
        if tmp0.__len__() == 2:
            tmps = tmp0[0]
            if not representsInt(tmp0[1]): return False
        else: False
    if isRadixNum(tmps): return True
    if '.' in tmps:
        tmp = tmps.split(sep = '.')
        if tmp.__len__() == 2:
            if not isRadixNum(tmp[0]): return False
            tmp2 = tmp[0].split(sep = 'r')[0]
            tmp2 += "r"
            tmp2 += tmp[1]
            if not isRadixNum(tmp2): return False
        else: return False    
    else: return False
    return True

class Token:
    def __init__(self, tokenName: str, inArr: bool, tokenLine:int, tokenType = ""):
        self.name = tokenName
        self.inArray = inArr
        self.lineNum = tokenLine
        self.type = tokenType

def printTokens(tokens: list, mode: int): #if mode = 1 or 2, display may have some bugs when a token has newline in its name
    print("Note: BYTE ERROR occurs when an element in byte array is not an interger.\n")
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
