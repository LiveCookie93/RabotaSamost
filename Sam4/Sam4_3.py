from datetime import datetime
import time
def taimer(a):
    count = 0
    while a >= count:
        now = datetime.now()
        newtime = now.strftime("%H:%M:%S")
        print("Текущее время ", newtime)
        time.sleep(1)
        count += 1

taimer(5)


