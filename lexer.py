from readfile import *

keywords = [
    "nil", "true", "false", "self", "super"
]
operators = [
    "+", "-", "*", "/", "//", "\\"
]
logicalOperators = [
    'not', '&', '|', 'and', 'or', 'eqv', 'xor'
]
bitWiseOperators = [
    'bitAnd:', 'bitOr:', 'bitXor:', 'bitInvert:', 'bitShift:'
]
comparisonOperators = [
    '=', '~=', '==', '~~', '>', '>=', '<', '<='
]
messages = [
	"thisContext", "Transcript", "clear",
	"show:", "nextPutAll:", "nextPut:", "space", "tab", "cr", "printOn:", "storeOn:",
	"endEntry", "Object", "new:", "class", "superclass", "Integer", "allInstances",
	"allSuperclasses", "hash", "copy", "shallowCopy", "deepCopy", "veryDeepCopy",
	"not", "isNil", "isZero", "positive", "strictlyPositive", "negative", "even",
	"odd", "isLiteral", "isInteger", "isFloat", "isNumber", "isUppercase", "isLowercase",
	"sign", "negated", "integerPart", "fractionPart", "reciprocal", "squared", "sqrt",
	"exp", "abs", "rounded", "truncated", "floor", "ceiling", "factorial", "ln", "log",
	"degreesToRadians", "radiansToDegrees", "sin", "cos", "tan", "arcSin", "arcCos",
	"arcTan", "Float", "pi", "e", "infinity", "nan", "Random", "new", "next", "yourself",
	"atRandom", "highbit", "bitAt",
	"allMask:", "anyMask:", "noMask:", "and:", "or", "eqv", "xor", "between", "isKindOf:",
	"isMemberOf:", "respondsTo:", "raisedTo:", "raisedToInteger", "roundTo", "truncateTo",
	"quo:", "rem:", "gcd:", "lcm:", "floorLog", "asInteger", "asFraction", "asFloat", "asCharacter",
	"asciiValue", "printString", "storeString", "radix:", "printStringBase:", "storeStringBase:",
	"argOne", "argTwo", "ifTrue", "ifFalse", "switch", "at:", "put:", "timesRepeat",
	"isLetter", "isDigit", "isAlphaNumeric", "isSeparator", "isVowel", "digitValue",
	"asLowercase", "asUppercase", "asString", "max:", "min:", "isEmpty", "size", "copyFrom:",
	"to", "indexOf:", "ifAbsent:", "occurrencesOf:", "conform:", "select:", "reject:", "collect:",
	"detect:", "ifNone:", "inject:", "shuffled", "asArray", "asByteArray", "asWordArray",
	"asOrderedCollection", "asSortedCollection", "asBag", "asSet", "SortedCollection",
	"sortBlock:", "addFirst:", "removeFirst:", "addLast:", "removeLast:", "addAll:", "removeAll:",
	"remove:", "isEmpty", "first", "last", "includes:", "Dictionary", "keyAtValue",
	"removeKey:", "includesKey", "keys", "values", "value:", "keysDo", "associationsDo:", "keysAndValuesDo:",
	"Smalltalk", "CMRGlobal", "CMRDictionary", "ReadStream", "peek", "contents", "atEnd",
	"ReadWriteStream", "position", "nextLine", "FileStream", "newFileNamed", "oldFileNamed",
	"close", "Date", "today", "dateAndTimeNow", "readFromString:", "newDay", "fromDays",
	"dayOfWeek", "indexOfMonth", "daysInMonth", "daysInYear", "nameOfDay", "nameOfMonth",
	"leapYear", "weekday", "previous", "dayOfMonth", "day", "firstDayOfMonth", "monthName",
	"monthIndex", "daysInMonth", "year", "daysInYear", "daysLeftInYear", "asSeconds",
	"addDays:", "subtractDays:", "subtractDate:", "printFormat:", "Time", "dateAndTimeNow",
	"fromSeconds:", "millisecondClockValue", "totalSeconds", "seconds", "minutes", "hours",
	"addTime:", "subtractTime", "millisecondsToRun:", "dotProduct:", "Rectangle", "Display",
	"restoreAfter:", "fillWhite", "Pen", "squareNib", "color:", "home", "up", "down", "north",
	"turn", "direction", "go", "location", "goto", "place:", "print", "extent", "withFont",
	"width", "height", "perform:", "evaluate", "name", "category", "comment", "kindOfSubclass",
	"definition", "instVarNames", "allInstVarNames", "classVarNames", "allClassVarNames",
	"sharedPools", "allSharedPools", "selectors", "sourceCodeAt", "withAllSuperclasses",
	"subclasses", "allSubclasses", "withAllSubclasses", "instSize", "isFixed", "isVariable",
	"isPointers", "isBits", "isBytes", "isWords", "inspect", "browse", "confirm", "halt",
	"notify", "error", "doesNotUnderstand", "shouldNotImplement", "subclassResponsibility",
	"errorImproperStore", "errorNonIntegerIndex", "errorSubscriptBounds", "primitiveFailed",
	"become", "FillInTheBlank", "whileTrue:", "whileFalse:", "timesRepeat:", "do:", "with:", "to:", "into:"
]

def processTokens(tokens: list):
    for token in tokens:
        if token.name in keywords:
            token.type = "KEYWORD"
        elif token.name in messages:
            token.type = "MESSAGE"
        elif token.name in operators:
            token.type = "OPERATOR"
        elif token.name in logicalOperators:
            token.type = "LOGICAL OPERATOR"
        elif token.name in bitWiseOperators:
            token.type = "BIT-WISE OPERATOR"
        elif token.name in comparisonOperators:
            token.type = "COMPARISON OPERATOR"
        else:
            pass
