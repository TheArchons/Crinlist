import json
import termcolor
import math
import re

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

    elif musicType == "Headphones":
        pass
    else:
        file = json.loads(open(musicType).read())
    for device in file:
        stars = device['stars']*"*"
        #print(device['rank']) #debug
        print(termcolor.colored(device['rank'] + " " + stars + " " + device['name'], color=determineColor(device['rank'])), end=" ")
        print(device['price'] + " " + device['signature'] + " " + device['comment'], end=" ")
        print(termcolor.colored(device['tone'], color=determineColor(device['tone'])), end=" ")
        print(termcolor.colored(device['technical'], color=determineColor(device['technical'])), end=" ")
        print(termcolor.colored(" " + device['graph'], color="blue"), end=" ")
        print(device['setup'] + " " + device['basedOn'] + " " + device["noteWeight"], end="\n\n")
    
def listSort(musicType, sort, reverse):
    if musicType == "IEM":
        file = json.loads(open("IEMList.json").read())
    elif musicType == "Headphones":
        pass
    else:
        file = json.loads(open(musicType).read())

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

def find(musicType, query, type, sort, reverse):
    query = query.lower()
    output = []
    #print(query) #debug
    if musicType == "IEM":
        file = json.loads(open("IEMList.json").read())
        for iem in file:
            if type == 'all': #search all fields if type isn't specified
                if query in iem['rank'].lower() or query in iem['name'].lower() or query in iem['signature'].lower() or query in iem['comment'].lower() or query in iem['tone'].lower() or query in iem['technical'].lower() or query in iem['graph'].lower() or query in iem['setup'].lower() or query in iem['basedOn'].lower():
                    output.append(iem)
            else:
                #print(iem[type]) #debug
                if query in iem[type].lower():
                    output.append(iem)
    json.dump(output, open("searchResults.json", "w"))
    #print(musicType, sort, reverse) #debug
    listSort('searchResults.json', sort, reverse)
    printList("searchResults.json")