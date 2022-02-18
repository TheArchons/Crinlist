import sys

def getCmd():
    try:
        #print(sys.argv[1]) #debug
        return sys.argv[1]
    except IndexError:
        return '-h'

def getType():
    try:
        return sys.argv[2]
    except IndexError:
        print("No type specified. Choose either IEMS or Headphones.")
        sys.exit(1)

def getModel():
    try:
        return sys.argv[3]
    except IndexError:
        print("No model specified.")
        sys.exit(1)

def getSort():
    try:
        return sys.argv[3]
    except IndexError:
        print("No sort specified. Choose From: Rank, Price, Value, Model, Signature, Tone Grade, Technical Grade, or Setup.")
        sys.exit(1)

def getReversed():
    try:
        return bool(sys.argv[4])
    except IndexError:
        return False