import sys

def getCmd():
    try:
        return sys.argv[1]
    except IndexError:
        return '-h'

def getType():
    try:
        return sys.argv[2]
    except IndexError:
        print("No type specified. Choose either IEMS or Headphones.")
        sys.exit(1)

def getQuery():
    try:
        return sys.argv[3]
    except IndexError:
        print("No Query specified.")
        sys.exit(1)

def getSort():
    try:
        return sys.argv[3]
    except IndexError:
        print("No sort specified. Choose From: Rank, Price, Value, Model, Signature, Tone Grade, Technical Grade, or Setup.")
        sys.exit(1)

def getReversed():
    try:
        if sys.argv[4] == 'reverse':
            return True
        else:
            return False
    except IndexError:
        return False

def getQuerySearch():
    try:
        return sys.argv[4]
    except IndexError:
        return 'all'

def getSort2():
    try:
        return sys.argv[5]
    except IndexError:
        return 'rank'

def getReversed2():
    try:
        return bool(sys.argv[6])
    except IndexError:
        return False

def getStrict():
    try:
        return bool(sys.argv[7])
    except IndexError:
        return False
