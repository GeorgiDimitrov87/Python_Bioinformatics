dna=raw_input("Enter sequence:")
g=dna.count('g')
c=dna.count('c')
dna_lenght=len(dna)
gc_percent=(c+g)*100.0/dna_lenght
print  "The DNA sequence's GC conent is", gc_percent ,"%" 

def gc(dna) :
  'CG % computation'
  nbases=dna.count('n')+dna.count('N')
  gcpercent=float(dna.count('c')+dna.count('C')?dna.count('g')+dna.count('G'))*100.0/(dna)-nbases)
  return gcpercent

