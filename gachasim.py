import numpy as np
pullcount = 40
pullcount_exedra = 40
tries = 1000000
print("### ---------------------------------------")
print(f"### f2p scenario genshin ({pullcount})")
import random
pulls = pullcount
mavuikapulls = np.array([3191, 3329, 3249, 3218, 3273, 3168, 3009, 3081, 3043, 3083, 3089, 2989, 3004, 2917, 2975, 2761, 2813, 2886, 2797, 2809, 2784, 2706, 2787, 2619, 2779, 2655, 2653, 2665, 2586, 2595, 2446, 2592, 2546, 2560, 2564, 2432, 2500, 2457, 2490, 2412, 2389, 2387, 2387, 2392, 2384, 2369, 2327, 2318, 2188, 2366, 2377, 2260, 2146, 2270, 2356, 2203, 2201, 2079, 2199, 2133, 2120, 2138, 2117, 2193, 2128, 2171, 2105, 2103, 2086, 2075, 2042, 2108, 2088, 21877, 39097, 50355, 53966, 50631, 42379, 31376, 20287, 11947, 6038, 2653, 975, 273, 71, 20, 1, 2])
totalpulls = np.sum(mavuikapulls)
array = mavuikapulls
normalized_array = array / totalpulls
fv = []
fvgot = []
counter = 0
hadfive = 0
pullsreal = 0
fifty = 0
radiance = 0
won5050prev = 0
radiancescounter = 0
radianceresetcounter = 0
for j in range(tries):
    pullie = max(pulls, pullsreal)
    for i in range(pullie):
        pullsreal = 0
        counter+=1
        if counter >= 90: #hard pity
            fifty = max(int(random.random() > 0.5),fifty)#50/50 gate 
            if fifty == 1: #won
                if won5050prev == 1:
                    radianceresetcounter+=1
                    radiance = 0
                won5050prev = 1
                fifty = 0 #next is 50/50
                fv.append(counter) #in which pull we get the character
                hadfive += 1 #got limited wanted 5 star
                pullsreal = pullie + pulls - i #save the rest of the pulls for next try
                counter = 0 #reset pity
                break #do not continue pulling
            else:
                won5050prev = 0
                radiance += 1
                if radiance >= 4 or random.random() < 0.00018: #base or 3 consecutive 50/50 losses
                    radiancescounter+=1 #stats
                    radiance = 0  #reset radiance
                    fv.append(counter)
                    fifty = 0
                    hadfive += 1
                    pullsreal = pullie + pulls - i
                    counter = 0
                    break
                fifty = 1 #next is 100%
                counter = 0 #reset pity
                #no break, continue pulling
            continue
        if random.random() < normalized_array[counter]: #accounting soft pity
            fifty = max(int(random.random() > 0.5),fifty) #50/50 gate 
            if fifty == 1: #won
                if won5050prev == 1:
                    radianceresetcounter+=1
                    radiance = 0
                won5050prev = 1
                fv.append(counter) #in which pull we get the character
                fifty = 0 #next is 50/50
                hadfive += 1 #got limited wanted 5 star
                pullsreal = pullie + pulls - i #save the rest of the pulls for next try
                #pulls is const (you get 40 on avg for each banner)
                # pullie is (pulls + saved from prev banner)
                #i is (pullie - done pulls)
                counter = 0 #reset pity
                break #do not continue pulling
            else:
                won5050prev = 0
                radiance += 1
                if radiance >= 4 or random.random() < 0.00018: #base or 3 consecutive 50/50 losses
                    radiancescounter += 1 #for stats
                    radiance = 0 #reset radiance
                    fv.append(counter)
                    fifty = 0
                    hadfive += 1
                    pullsreal = pullie + pulls - i
                    counter = 0
                    break
                fifty = 1 #next is 100%
                counter = 0 #reset pity
                #no break, continue pulling
    if hadfive==1:
        hadfive=0
        fvgot.append(1) #have got wanted limited 5*
    else:
        fvgot.append(0) #have not got wanted limited 5*

print(f"radiances: {radiancescounter}, radiance resets: {radianceresetcounter}")
average = np.median(fv)
print(f"The average pulls to get 5star is: {average}")
average = np.mean(fvgot)
print(f"Characters per banner is: {average}")

print("### ---------------------------------------")
print("### 700eur scenario genshin")
import random
pulls = 6480*7//160
print(pulls)
fv = []
fvgot = []
counter = 0
hadfive = 0
pullsreal = 0
fifty = 0
radiance = 0
won5050prev = 0
radiancescounter = 0
radianceresetcounter = 0
for i in range(tries):
    pullie = max(pulls, pullsreal)
    for i in range(pullie):
        pullsreal = 0
        counter+=1
        if counter >= 90:
            fifty = max(int(random.random() > 0.5),fifty)
            if fifty == 1:
                if won5050prev == 1:
                    radianceresetcounter+=1
                    radiance = 0
                won5050prev = 1
                fv.append(counter)
                fifty = 0
                hadfive += 1
                #not stopping, spending everything on each banner
            else:
                won5050prev = 0
                radiance += 1
                fifty = 1
                if radiance >= 4 or random.random() < 0.00018: #base or 3 consecutive 50/50 losses
                    radiancescounter += 1 #for stats
                    radiance = 0 #reset radiance
                    fv.append(counter)
                    fifty = 0
                    hadfive += 1
                    pullsreal = pullie + pulls - i
                    counter = 0
            counter = 0
            continue

        if random.random() < normalized_array[counter]:
            fifty = max(int(random.random() > 0.5),fifty)
            if fifty == 1:
                if won5050prev == 1:
                    radianceresetcounter+=1
                    radiance = 0
                won5050prev = 1
                fv.append(counter)
                fifty = 0
                hadfive += 1
                #not stopping, spending everything on each banner
            else:
                won5050prev = 0
                radiance += 1
                fifty = 1
                if radiance >= 4 or random.random() < 0.00018: #base or 3 consecutive 50/50 losses
                    radiancescounter += 1 #for stats
                    radiance = 0 #reset radiance
                    fv.append(counter)
                    fifty = 0
                    hadfive += 1
                    pullsreal = pullie + pulls - i
                    counter = 0
            counter = 0
    if hadfive>=1:
        fvgot.append(hadfive)
        hadfive=0
    else:
        fvgot.append(0)

print(f"radiances: {radiancescounter}, radiance resets: {radianceresetcounter}")
average = np.median(fv)
print(f"The average pulls to get 5star is: {average}")
average = np.mean(fvgot)
print(f"avg characters per banner is: {average}")
print("### ---------------------------------------")
print(f"### f2p scenario exedra ({pullcount})")
import random
pulls = pullcount_exedra
print(pulls)
fv = []
fvgot = []
counter = 0
hadfive = 0
pullsreal = 0
for j in range(tries):
    pullie = max(pulls, pullsreal)
    counter = 0
    for i in range(pullie):
        pullsreal = 0
        counter += 1
        if counter >= 200 or random.random() < 0.0075:
            fv.append(counter)
            pullsreal = pullie + pulls - i #save the rest of the pulls for next 
            counter = 0 #reset pity
            hadfive += 1 #got wanted limited 5*
            break #do not continue pulling

    if hadfive>=1:
        fvgot.append(hadfive)
        hadfive=0
    else:
        fvgot.append(0)
        
average = np.median(fv)
print(f"The average pulls to get 5star is: {average}")
average = np.mean(fvgot)
print(f"Characters per banner is: {average} ")

print("### ---------------------------------------")
print("### 700eur scenario exedra")
import random
pulls = 100000//300
print(pulls)
fv = []
fvgot = []
counter = 0
hadfive = 0
pullsreal = 0
for i in range(tries):
    pullie = max(pulls, pullsreal)
    counter = 0
    for i in range(pullie):
        pullsreal = 0
        counter+=1
        if counter >= 200 or random.random() < 0.0075:
            fv.append(counter)
            counter = 0
            hadfive += 1
            #no stopping, spending all
    counter=0
    if hadfive>=1:

        fvgot.append(hadfive)
        hadfive=0
    else:
        fvgot.append(0)

average = np.median(fv)
print(f"The average pulls to get 5star is: {average}")
average = np.mean(fvgot)
print(f"Characters per banner is: {average} (accounting trader)")
print("### ---------------------------------------")
print(f"### saving scenario exedra ({pullcount}) ")
import random
pulls = pullcount_exedra
print(pulls)
fv = []
fvgot = []
counter = 0
hadfive = 0
pullsreal = 0
for j in range(tries):
    pullie = max(pulls, pullsreal)
    #print(pullie)
    counter = 0
    for i in range(pullie):
        if pullie<200:
            pullsreal = pullie + pulls - i
            break
        pullsreal = 0
        counter += 1
        if counter >= 200 or random.random() < 0.0075:
            fv.append(counter)
            pullsreal = pullie + pulls - i #save the rest of the pulls for next
            counter = 0 #reset pity
            hadfive += 1 #got wanted limited 5*
            break #do not continue pulling

    if hadfive>=1:
        fvgot.append(hadfive)
        hadfive=0
    else:
        fvgot.append(0)
        
average = np.median(fv)
print(f"The average pulls to get 5star is: {average}")
average = np.mean(fvgot)
print(f"Characters per banner is: {average} (accounting trader)")
print("### ---------------------------------------")
print(f"### f2p scenario wuwa ({pullcount})")
import random
pulls = pullcount
camellyapulls = np.array([1913, 1959, 1894, 1786, 1791, 1698, 1786, 1726, 1673, 1607, 1600, 1537, 1601, 1585, 1614, 1583, 1577, 1511, 1492, 1539, 1525, 1502, 1513, 1414, 1463, 1389, 1389, 1513, 1434, 1409, 1378, 1379, 1355, 1377, 1361, 1252, 1344, 1314, 1235, 1261, 1324, 1242, 1235, 1219, 1232, 1219, 1219, 1165, 1204, 1172, 1145, 1106, 1151, 1150, 1091, 1131, 1091, 1134, 1149, 1149, 1151, 1174, 1187, 1160, 1214, 5833, 9835, 12778, 14595, 14943, 16147, 14915, 11338, 7503, 3910, 1863, 615, 123, 19, 9])
totalpulls = np.sum(camellyapulls)
#print(totalpulls)
array = camellyapulls
normalized_array = array / totalpulls
#print(normalized_array)
fv = []
fvgot = []
counter = 0
hadfive = 0
pullsreal = 0
fifty = 0
for j in range(tries):
    pullie = max(pulls, pullsreal)
    for i in range(pullie):
        pullsreal = 0
        counter+=1
        if counter >= 80: #hard pity
            fifty = max(int(random.random() > 0.5),fifty)#50/50 gate 
            if fifty == 1: #won
                fifty = 0 #next is 50/50
                fv.append(counter) #in which pull we get the character
                hadfive += 1 #got limited wanted 5 star
                pullsreal = pullie + pulls - i #save the rest of the pulls for next try
                counter = 0 #reset pity
                break #do not continue pulling
            else:
                fifty = 1 #next is 100%
                counter = 0 #reset pity
                #no break, continue pulling
            continue
        if random.random() < normalized_array[counter]: #accounting soft pity
            fifty = max(int(random.random() > 0.5),fifty) #50/50 gate 
            if fifty == 1: #won
                fv.append(counter) #in which pull we get the character
                fifty = 0 #next is 50/50
                hadfive += 1 #got limited wanted 5 star
                pullsreal = pullie + pulls - i #save the rest of the pulls for next try
                #pulls is const (you get 40 on avg for each banner)
                # pullie is (pulls + saved from prev banner)
                #i is (pullie - done pulls)
                counter = 0 #reset pity
                break #do not continue pulling
            else:
                fifty = 1 #next is 100%
                counter = 0 #reset pity
                #no break, continue pulling
    if hadfive==1:
        hadfive=0
        fvgot.append(1) #have got wanted limited 5*
    else:
        fvgot.append(0) #have not got wanted limited 5*
average = np.median(fv)
print(f"The average pulls to get 5star is: {average}")
average = np.mean(fvgot)
print(f"Characters per banner is: {average}")


