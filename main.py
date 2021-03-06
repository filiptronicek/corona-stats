import requests
import re
import time
from datetime import datetime
import json
import os

from release import newRls

DAY = 86400
DELAY = 600

ratio = DAY / DELAY

date = datetime.now()

def get_sick():
    r = requests.get('https://corona.lmao.ninja/v2/all')
    return r.json()['cases']

def main():    
        last_sick = get_sick()
        totalLoops = 0
        loops = 0
        gained_total = 0
        while True:
            now = datetime.now()
            time.sleep(DELAY)
            if totalLoops % int(ratio) == 0:
                version = newRls()
                os.system('git tag -a v'+version+' -m "Data version '+version+'"')
                os.system('git push --tags')
            sick_now = get_sick()
            #print(trees_now)
            loops += 1
            totalLoops += 1

            WriteData = open("data/"+now.strftime("%Y.%m.%d")+"-count.csv", "a")   
            WriteData.write(str(sick_now)+","+now.strftime("%Y-%m-%d %H:%M:%S")+"\n")
            WriteData.close()

            if sick_now > last_sick:
                totalLoops += 1
                loops += 1

                diff = sick_now - last_sick
                gained_total += diff
                goal = 7660000000 - sick_now
                rate = round(diff/(loops*DELAY), 2)
                rate_total = round(gained_total/(totalLoops*DELAY), 2)
                preditction = (goal/rate_total)/60/60/24

                WriteRate = open("data/"+now.strftime("%Y.%m.%d")+"-rate.csv", "a")   
                WriteRate.write(str(rate)+","+now.strftime("%Y-%m-%d %H:%M:%S")+"\n")
                WriteRate.close()    

                if(preditction < 2):
                    print('\n\nNumbers are running at ${} / second. That would mean we will be done in {} hours! Now the rate is: {} / second \n+{} in {} seconds'.format(rate_total, round(preditction * 24), rate, diff, round(loops*DELAY, 2)))
                else:
                    print('\n\nNumbers are running at ${} / second. That would mean we will be done in {} days! Now the rate is: {} / second \n+{} in {} seconds'.format(rate_total, round(preditction), rate, diff, round(loops*DELAY, 1)))

                loops = 0
                last_sick = sick_now

if __name__ == '__main__':
    main()
