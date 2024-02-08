# Not the most efficient "scraper"
# This is more of a formatter then a scraper.
# 
# Goal: Take the chart popularity table (assumed to have all the songs and all the charts including their difficulties)
# https://www.piugame.com/leaderboard/top_steps.php?mode=full&date=202401
#
# And extract each one to a readable format.
#

f = open("table-formated.html")
g = open("output.json", "w")

isDouble = ''
firstDigit = True
difficulty = 0


entry = '{'


for line in f:
    if('<div class="profile_img"><div class="resize"><div class="re bgfix" style="background-image:url' in line):
        print(line[96:-23])
        entry += '"jacket":"' + line[96:-23] + '",'
        continue
    elif('<p class="t1">' in line):
        print(line[14:-5])
        entry += '"song_name":"' + line[14:-5] + '",'
        continue
    elif('<p class="t2">' in line):
        print(line[14:-5])
        entry += '"song_artist":"' + line[14:-5] + '",'
        continue
    elif('<div class="stepBall_in flex vc col hc wrap bgfix cont" style="background-image:url' in line):
        print(line[125:-12])
        isDouble = line[125:-12]
        entry += '"style":"' + line[125:-12] + '",'
        continue
    elif('<div class="imG"><img src=' in line):
        if(isDouble == 'c' and firstDigit == True):
            g.write(entry +'"difficulty":"X"' + "},\n")
            entry = '{'
            firstDigit = False
            continue
        if(isDouble == 'c' and firstDigit == False):
            firstDigit = True
            continue
        if(firstDigit == True):
            difficulty = int(line[73:-20])*10
            #print("First digit " + str(difficulty))
            firstDigit = False
        elif(firstDigit == False):
            firstDigit = True
            difficulty += int(line[73:-20])
            print("Difficulty " + str(difficulty))
            entry += '"difficulty":' + str(difficulty) + '}'
            difficulty = 0


            g.write(entry + ",\n")
            entry = '{'
        continue

f.close
g.close

