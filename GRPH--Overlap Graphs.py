import itertools

# reading fasta data to dict
strings = {}
with open("GRPH--Input.fasta", "r") as f:
    lines = f.readlines()
    string = ""
    for line in lines:
        line = line.rstrip()
        if (line[0] == ">"):
            string = line[1:] 
            strings[string] = ""
        else:
            strings[string] += line

k = 3
with open("GRPH--Output.txt","w") as f:
    for i,j in itertools.combinations(strings, 2):
        if strings[i][:k] == strings[j][-k:]:
            f.write(j + " " + i + "\n")
        if strings[j][:k] == strings[i][-k:]:
            f.write(i + " " + j + "\n")

