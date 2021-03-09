inpt = input("n k: ")
n = int(inpt.split(" ")[0])
k = int(inpt.split(" ")[1])

fib = [1, 1]
while len(fib) != n:
    l = len(fib)
    fib.append(fib[l-1] + k*fib[l-2])
    
print(fib[len(fib)-1])
