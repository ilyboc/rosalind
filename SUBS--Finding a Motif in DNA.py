s = input("DNA: ")
t = input("Motif: ")

ind = 0
while True:
    try:
        ind = s.index(t, ind)
        print(ind+1, end=" ")
        ind += 1
    except ValueError:
        break
