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
        printList()
    elif cmd == "-s" or cmd == "--sort":
        sort(getType(), getSort())
    elif cmd == "-f" or cmd == "--find":
        find(getType(), getModel())
    