with open("CONS--Input.txt", "r") as f:
    lines = f.readlines()
    lines.append(">dummy")
    profile = [[], [], [], []]
    consensus = []
    j = 0
    for line in lines:
        line = line.rstrip()
        if(line[0] == ">"):
            j = 0
        else:
            for pair in line:
                if j >= len(profile[0]):
                    for i in range(4):
                        profile[i].insert(j,0)
                if pair == "A":
                    profile[0][j] += 1
                elif pair == "C":
                    profile[1][j] += 1
                elif pair == "G":
                    profile[2][j] += 1
                elif pair == "T":
                    profile[3][j] += 1
                j += 1
    lines.pop()
    with open("CONS--Result.txt", "w") as f2: 
        
        bases = ["A", "C", "G", "T"]
        for j in range(len(profile[0])):
            imax = 0
            for i in range(4):
                if profile[i][j] > profile[imax][j]:
                    imax = i
            f2.write(bases[imax])
        f2.write("\n")
        for i in range(4):
            f2.write(bases[i]+": " + " ".join(map(str ,profile[i])) + "\n")
    
            