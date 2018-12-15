import time as t
while True:
    now=t.localtime()
    #check if the date is the 25th of the month at 11:00
    #if so, breaks the while loop
    if now[2]==25 and now[3]==11:
        print("done")
        break
    #if not print how many days till the 25th
    else:
        print(25-now[2])
    #wait 4 seconds till you start the loop over again
    t.sleep(4)
