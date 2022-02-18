import json
import termcolor

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

def printHelp():
    print("CrinList - A CLI for crinacle.com")
    print("Usage: python CrinList.py [OPTION]")
    print("Options:")
    print("-h   --help      Display this help message")
    print("-l   --list      List all rankings")
    print("-s   --sort      Sort rankings by type")
    print("-se  --search    Search rankings by model")
    print("-f   --filter    Filter rankings by type")

def printList(musicType):
    if musicType == "IEM":
        file = json.loads(open("IEMList.json").read())
        for iem in file:
            stars = iem['stars']*"*"
            #print(iem['rank']) #debug
            print(termcolor.colored(iem['rank'] + " " + stars + " " + iem['name'], color=determineColor(iem['rank'])), end="")
            print(iem['price'] + " " + iem['signature'] + " " + iem['comment'] + " " + iem['tone'] + " " + iem['technical'] + " " + iem['graph'] + " " + iem['setup'] + " " + iem['basedOn'] + " " + iem["noteWeight"], end="\n\n")
    elif musicType == "Headphones":
        pass
def sort(musicType, sort):
    pass

def find(musicType, model):
    pass