from ParseIntoJSON import parse

def createIEM():
    try:
        open('IEMList.json', 'r') #check if file exists
    except FileNotFoundError:
        #print('IEMList.json not found. Creating...') #debug
        parse('IEM.html', 'IEMList.json')
    

def createHeadphones():
    try:
        open('HeadphoneList.json', 'r') #check if file exists
    except FileNotFoundError:
        #print('HeadphoneList.json not found. Creating...') #debug
        parse('Headphone.html', 'HeadphoneList.json')