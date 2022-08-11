import time
j = 0
while True:
    for j in range(6):
        print("[",j*" ","=",(6-j)*" ","]",end="\r", sep="")
        time.sleep(0.2)
    for j in range(6):
        print("[",(6-j)*" ", "=",(j)*" ","]",end="\r", sep="")
        time.sleep(0.2)