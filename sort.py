#
# Takes in the JSON from "scraper.py" and condenses the list.
#
#
#
#

import json

with open('output.json') as json_file:
    data = json.load(json_file)

output = {"stepcharts":[]}


for i in data['stepcharts']:
    songNameInOutput = [songName['song_name'] for songName in output['stepcharts']]

    if i['song_name'] not in songNameInOutput:
        addSong = {"song_name": i['song_name'], "song_artist": i['song_artist'], "single":[], "double":[], "coop":[], "jacket": i['jacket']}
        print("whats this " + i['style'])
        if i['style'] == 's':
            addSong['single'] = [(i['difficulty'], 0)]
        elif i['style'] == 'd':
            addSong['double'] = [(i['difficulty'], 0)]
        elif i['style'] == 'c':
            addSong['coop'] = [(i['difficulty'], 0)]
        
        output['stepcharts'] += [addSong]

    elif i['song_name'] in songNameInOutput:
        print("Already in " + i['song_name'])
        if i['style'] == 's':
            output['stepcharts'][list(songNameInOutput).index(i['song_name'])]['single'] += [(i['difficulty'], 0)]
        elif i['style'] == 'd':
            output['stepcharts'][list(songNameInOutput).index(i['song_name'])]['double'] += [(i['difficulty'], 0)]
        elif i['style'] == 'c':
            output['stepcharts'][list(songNameInOutput).index(i['song_name'])]['coop'] += [(i['difficulty'], 0)]

print(output)

with open('sorted.json', 'w') as f:
    json.dump(output, f)
f.close
