from readfile import *

def processTokens(tokens: list, varList: list):
	len = tokens.__len__()
	for i in range(0, len):
		if not tokens[i].type:
			tl = tokens[i].name.__len__()
			if tokens[i].name == "." and not tokens[i].inArray:
				tokens[i].type = "STATEMENT SEPERATOR"
			elif tokens[i].name == ";" and not tokens[i].inArray:
				tokens[i].type = "MESSAGE SEPERATOR"
			elif tokens[i].name == ':=' and not tokens[i].inArray:
				tokens[i].type = "ASSIGNMENT OPERATOR"
			elif tokens[i].name == ']' and not tokens[i].inArray:
				tokens[i].type = "RIGHT SQU.BRACKET"
			elif tokens[i].name == ')' and not tokens[i].inArray:
				tokens[i].type = "RIGHT PARENTHESE"

			elif tokens[i].name in keywords:
				tokens[i].type = "KEYWORD"
			elif tokens[i].name in messages:
				tokens[i].type = "PREBUILT MESSAGE"
			elif tokens[i].name in operators:
				if tokens[i].inArray:
					tokens[i].type = "SYMBOL"
				else: tokens[i].type = "OPERATOR"
			elif tokens[i].name in logicalOperators:
				if tokens[i].inArray:
					tokens[i].type = "SYMBOL"
				else: tokens[i].type = "LOGICAL OPERATOR"
			elif tokens[i].name in bitWiseOperators and not tokens[i].inArray:
				tokens[i].type = "BIT-WISE OPERATOR"
			elif tokens[i].name in comparisonOperators:
				if tokens[i].inArray:
					tokens[i].type = "SYMBOL"
				else: tokens[i].type = "COMPARISON OPERATOR"
			elif representsInt(tokens[i].name): 
				tokens[i].type = "INTEGER"
			elif isFloat(tokens[i].name): 
				tokens[i].type = "FLOAT"
			elif isRadixNum(tokens[i].name): 
				tokens[i].type = "RADIX INTEGER"
			elif isRadixFloat(tokens[i].name): 
				tokens[i].type = "RADIX FLOAT"
			elif isConsChar(tokens[i].name):
				tokens[i].type = "CONST CHAR"
			elif isSymbol(tokens[i].name):
				tokens[i].type = "SYMBOL"
			elif tokens[i].name in varList:
				tokens[i].type = "VARIABLE"
			elif canBeSymbol(tokens[i].name) and tokens[i].inArray:
				tokens[i].type = "SYMBOL"
			elif isId(tokens[i].name):
				if i + 1 < len:
					if tokens[i+1].name == ":=":
						tokens[i].type = "VARIABLE"
						tokens[i+1].type = "ASSIGNMENT OPERATOR"
						varList.append(tokens[i].name)
						continue
			elif tl > 1:
				if tokens[i].name[0] == tokens[i].name[tl-1]:
					if tokens[i].name[0] == '\'':
						tokens[i].type = "STRING"
					elif token[i].name[0] == '\"':
						tokens[i].type = "COMMENT"
				elif tokens[i].name[tl-1] == ':' and isId(tokens[i].name[0:tl-1]):
					tokens[i].type = "KEYWORD MESSAGE"
	for t in tokens:
		if not t.type:
			t.type = "ERROR"

	for i in range(0, tokens.__len__()):
		if i - 1 > 0:
			if tokens[i-1].type: 
				if tokens[i-1].type in ["BIT-WISE OPERATOR", "LOGICAL OPERATOR", "COMPARISON OPERATOR"]:
					tokens[i].type += " AS PARAM" 
				elif tokens[i-1] in messages and tokens[i-1].name.__len__()>1:
					if tokens[i-1].name[tokens[i-1].name.__len__()-1] == ':':
						tokens[i].type += " AS PARAM"
				elif tokens[i-1].type == "KEYWORD MESSAGE":
					tokens[i].type += " AS PARAM"
						

					
