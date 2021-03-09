inpt = input("n m: ")
n = int(inpt.split(" ")[0])
m = int(inpt.split(" ")[1])

mature = [0]
nonmature = [1]

for i in range(n-1):
    nonmature.insert(i+1, mature[i])
    for j in range(1,m):
        try:
            mature[i+j] += nonmature[i]
        except:
            mature.insert(i+j, nonmature[i])

print(nonmature[n-1]+mature[n-1])