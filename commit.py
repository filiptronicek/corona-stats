from time import sleep
import os

def commit():
    delay = 1200

    os.system("git add .")

    os.system('git commit -m "Data"')
    os.system("git push")

    sleep(delay)
    commit()
commit()