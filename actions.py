import json
import termcolor
import math

def determineColor(rank):
    switchDict = {
        "S+" : "red",
        "S" : "red",
        "S-" : "red",
        "A+" : "yellow",
        "A" : "yellow",
        "A-" : "yellow",
        "B+" : "green",
        "B" : "green",
        "B-" : "green",
        "C+" : "cyan",
        "C" : "cyan",
        "C-" : "cyan",
        "D+" : "blue",
        "D" : "blue",
        "D-" : "blue",
        "E" : "magenta",
        "F" : "magenta"
    }
    return switchDict[rank]

def rankNumber(rank):
    if rank == "S+":
        return 1
    elif rank == "S":
        return 2
    elif rank == "S-":
        return 3
    elif rank == "A+":
        return 4
    elif rank == "A":
        return 5
    elif rank == "A-":
        return 6
    elif rank == "B+":
        return 7
    elif rank == "B":
        return 8
    elif rank == "B-":
        return 9
    elif rank == "C+":
        return 10
    elif rank == "C":
        return 11
    elif rank == "C-":
        return 12
    elif rank == "D+":
        return 13
    elif rank == "D":
        return 14
    elif rank == "D-":
        return 15
    elif rank == "E":
        return 16
    elif rank == "F":
        return 17
    else:
        return 0

def printHelp():
    print("CrinList - A CLI for crinacle.com")
    print("Usage: python CrinList.py [OPTION]")
    print("Options:")
    print("-h   --help      Display this help message")
    print("-l   --list      List all rankings")
    print("-s   --sort      Sort rankings by type")
    print("-se  --search    Search rankings by model")
    print("-f   --filter    Filter rankings by type")

def intSort(val):
    try:
        return int(val)
    except:
        return -1*math.inf

def stringSort(val):
    return len(val)

def printList(musicType):
    if musicType == "IEM":
        file = json.loads(open("IEMList.json").read())
        for iem in file:
            stars = iem['stars']*"*"
            #print(iem['rank']) #debug
            print(termcolor.colored(iem['rank'] + " " + stars + " " + iem['name'], color=determineColor(iem['rank'])), end=" ")
            print(iem['price'] + " " + iem['signature'] + " " + iem['comment'] + " " + iem['tone'] + " " + iem['technical'] + " " + iem['graph'] + " " + iem['setup'] + " " + iem['basedOn'] + " " + iem["noteWeight"], end="\n\n")
    elif musicType == "Headphones":
        pass
    
def sort(musicType, sort, reverse):
    if musicType == "IEM":
        file = json.loads(open("IEMList.json").read())
        if sort == "rank" or sort == "tone" or sort == "technical":
            file.sort(key=lambda x: rankNumber(x[sort]), reverse=not reverse)
        elif sort == "stars":
            file.sort(key=lambda x: x['stars'], reverse=reverse)
        elif sort == "name" or sort == "model":
            file.sort(key=lambda x: x['name'], reverse=not reverse)
        elif sort == "price" or sort == "noteWeight":
            file.sort(key=lambda x : intSort(x[sort]), reverse=reverse)
        elif sort == "signature" or sort == "comment" or sort == "setup" or sort == "basedOn":
            file.sort(key=lambda x: stringSort(x[sort]), reverse=reverse)
        
        json.dump(file, open("IEMList.json", "w"))
    else:
        pass
    pass

def find(musicType, model):
    pass