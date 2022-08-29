from ParseIntoJSON import parse
from actions import *
import os

def createIEM():
    
    try:
        open('IEMList.json', 'r') #check if file exists
    except FileNotFoundError:
        if not os.path.exists('IEM.html'):
            open("IEM.html", "wb").write(get("https://www.crinacle.com/rankings/iems/").content)
        parse('IEM.html', 'IEMList.json')
        listSort('IEM', 'rank', False)
    

def createHeadphones():
    try:
        open('HeadphoneList.json', 'r') #check if file exists
    except FileNotFoundError:
        if not os.path.exists('Headphones.html'):
            open("Headphone.html", "wb").write(get("https://www.crinacle.com/rankings/headphones/").content)
        parse('Headphone.html', 'HeadphoneList.json')
        listSort('Headphones', 'rank', False)