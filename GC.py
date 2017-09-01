dna=raw_input("Enter sequence:")
g=dna.count('g')
c=dna.count('c')
dna_lenght=len(dna)
gc_percent=(c+g)*100.0/dna_lenght
print  "The DNA sequence's GC conent is", gc_percent ,"%" 
