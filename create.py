from ParseIntoJSON import parse
from actions import *

def createIEM():
    
    try:
        open('IEMList.json', 'r') #check if file exists
    except FileNotFoundError:
        parse('IEM.html', 'IEMList.json')
        listSort('IEM', 'rank', False)
    

def createHeadphones():
    try:
        open('HeadphoneList.json', 'r') #check if file exists
    except FileNotFoundError:
        parse('Headphone.html', 'HeadphoneList.json')
        listSort('Headphones', 'rank', False)