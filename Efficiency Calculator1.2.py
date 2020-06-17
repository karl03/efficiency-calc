totdist = 0
totdistavg = 0
totdistnow = 0
remdist = 0
remdistavg = 0
eff = 0
avgeff = 0
effneed = 0
dist = 0
cap = 0
ucap = 0
distout = 0
distfurth = 0
getback = False


#Efficiency = mAh / Km


while True: #Starting infinite loop
    
    cap = int(input("Battery capacity in mAh?")) #Getting total battery capacity
    
    while eff == 0:
        eff = int(input("What is current efficiency (mah/km)?"))
        if eff == 0:
            print("Please enter efficiency \n")

    dist = int(input("How many kilometres travelled?"))
    distout = int(input("How many kilometres out?"))
    ucap = int(input("Battery mAh used?"))

    if cap > 0 and eff > 0:
        totdist = cap / eff

    if cap - ucap > 0 and eff > 0:
        remdist = (cap - ucap) / eff

    if ucap > 0 and dist > 0:
        avgeff = ucap / dist
        
    if cap > 0 and avgeff > 0:
        totdistavg = cap / avgeff
        
    if cap - ucap > 0 and avgeff > 0:
        remdistavg = (cap - ucap) / avgeff
    
    if distout < remdist:
        getback = True
    else:
        getback = False
        print("Can you get back: " + str(getback))
        effneed = (cap - ucap) / distout

    print("Results: \n")
        
    print("Average efficiency so far is: " + str(avgeff) + "mAh/Km")
    print("Total distance under current efficiency is: " + str(totdist) + "km")
    print("Total distance under average efficiency is: " + str(totdistavg) + "km")
    print("Remaining distance under current efficiency is: " + str(remdist) + "km")
    print("Remaining distance under average efficiency is: " + str(remdistavg) + "km")

    if getback == True:
        distfurth = (remdist + distout) / 2

        print("You can go " + str(distfurth) + "km further. \n")

    else:
        print("You need efficiency lower than: " + str(effneed) + " to get back \n")

    eff = 0
