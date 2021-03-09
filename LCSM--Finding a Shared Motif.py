from Bio import SeqIO

with open('LCSM--Input.fasta') as f:
    strings = list(SeqIO.parse(f, 'fasta'))

def longest_substr(str1, str2, n):
    for i in range(n,0,-1):
        for offset in range(len(str2)-i+1):
            substr = str2[offset:offset+i]
            if substr in str1 and substr not in bad:
                return substr

lsubstr = str(strings[0].seq)
found = False
bad = []
while not found:
    found = True
    for fasta in strings:
        name, sequence = fasta.id, str(fasta.seq)
        if lsubstr not in sequence:
            found = False
            bad.append(lsubstr)
            lsubstr = longest_substr(sequence, str(strings[0].seq), len(lsubstr))
            break
    
print(lsubstr)
