import json, math


def parse(source, output):
    file = open(source, 'r', encoding='utf-8')
    saveFile = open(output, 'w', encoding='utf-8')
    data = []
    for line in file:
        if line[:34] == '<td class="column-1"><span class="':
            dict = {}
            line = line.split('td')
            rank = line[1].split('>')[2].split('<')[0]
            stars = len(line[3].split('>')[1].split('<')[0])
            if line[5] == ' class="column-3"><a href="https://crinacle.com/graphs/iems/tiandirenhe-': #exception for the tiandireenhe because it's formatted differently
                name = 'Tiandirenhe TD1'
                price = '25'
                signature = 'V-shaped'
                comment = 'Generic V-shaped DD with alright midrange tonality and technicalities.'
                tone = 'C'
                technical = 'C'
                setup = 'DD'
                basedOn = 'Third party unit'
                noteWeight = ''
                graph = 'https://crinacle.com/graphs/iems/tiandirenhe-td1/'
                #saveFile.write(rank + ',' + str(stars) + ',' + name + ',' + price + ',' + signature + ',' + comment + ',' + tone + ',' + technical + ',' + setup + ',' + basedOn + ',' + noteWeight + '\n')
                dict['rank'] = rank
                dict['stars'] = stars
                dict['name'] = name
                dict['price'] = price
                dict['signature'] = signature
                dict['comment'] = comment
                dict['tone'] = tone
                dict['technical'] = technical
                dict['setup'] = setup
                dict['basedOn'] = basedOn
                dict['noteWeight'] = noteWeight
                dict['graph'] = graph
                data.append(dict)
                continue
            else:
                name = line[5].replace('/a>', '/').split("/<")[0].replace('<', '').split('>')[-1]
            graph = line[5].split('href="')[-1].split('\">')[0]
            if graph.split('//')[0] != 'https:':
                graph = ''
            price = line[7].split(' class="column-4">')[1].split('</')[0]
            signature = line[9].split(' class="column-5">')[1].split('</')[0]
            comment = line[11].split(' class="column-6">')[1].split('</')[0]
            tone = line[13].split(' class="column-7">')[1].split('</')[0]
            technical = line[15].split(' class="column-8">')[1].split('</')[0]
            setup = line[17].split(' class="column-9">')[1].split('</')[0]
            basedOn = line[19].split(' class="column-10">')[1].split('</')[0]
            noteWeight = line[21].split(' class="column-11">')[1].split('</')[0]
            dict['rank'] = rank
            dict['stars'] = stars
            dict['name'] = name
            dict['price'] = price
            dict['signature'] = signature
            dict['comment'] = comment
            dict['tone'] = tone
            dict['technical'] = technical
            dict['setup'] = setup
            dict['basedOn'] = basedOn
            dict['noteWeight'] = noteWeight
            dict['graph'] = graph
            data.append(dict)
            #saveFile.write(rank + ',' + str(stars) + ',' + name + ',' + price + ',' + signature + ',' + comment + ',' + tone + ',' + technical + ',' + setup + ',' + basedOn + ',' + noteWeight + '\n')

    data = data[math.ceil(len(data)/2):]
    #print(data) #debug
    json.dump(data, saveFile)
    file.close()
    saveFile.close()

def main():
    filePath = input('Enter the file path: ')
    saveLocation = input('Enter the save location: ')
    parse(filePath, saveLocation)

