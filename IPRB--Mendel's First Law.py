from math import comb

inpt = input("k m n: ")
k = int(inpt.split(" ")[0])
m = int(inpt.split(" ")[1])
n = int(inpt.split(" ")[2])

kC1 = comb(k, 1)
kC2 = comb(k, 2)
mC1 = comb(m, 1)
mC2 = comb(m, 2)
nC1 = comb(n, 1)
kmnC2 = comb(k+m+n, 2)

proba = (1*(kC1*mC1) + 1*kC2 + 1*(kC1*nC1) + 0.75*mC2 + 0.5*(mC1*nC1))/kmnC2
print(round(proba,5))