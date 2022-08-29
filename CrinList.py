from get import *
from create import *
from actions import *

def main():
    createIEM() #creates JSON of IEM if it doesn't exist
    createHeadphones() #creates JSON of headphones if it doesn't exist
    cmd = getCmd()
    if cmd == "-h" or cmd == "--help":
        printHelp()
    elif cmd == "-l" or cmd == "--list":
        printList(getType())
    elif cmd == "-s" or cmd == "--sort":
        listSort(getType(), getSort(), getReversed())
    elif cmd == "-se" or cmd == "--search":
        find(getType(), getQuery(), getQuerySearch(), getSort2(), getReversed2(), getStrict())
    elif cmd == "-u" or cmd == "--update":
        update(getType())

main()