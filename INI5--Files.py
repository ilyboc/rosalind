with open("INI5--Input.txt", "r") as f:
    lines = f.readlines()
    for i in range(1,len(lines),2):
        print(lines[i], end="")