with open("HAMM--Input.txt", "r") as f:
    lines = f.readlines()
    count = 0
    for i in range(len(lines[1])):
        if lines[0][i] != lines[1][i]:
            count += 1
    print(count)        