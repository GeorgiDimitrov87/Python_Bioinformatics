#running blast over the internet
import Bio
print(Bio.__versiom__)

from Bio.Blast import NCBIWWW
fasta_string = open("myseq.fa").read()
result_handle = NCBIWWW.qblast("blastn" , "nt" , fast_string)

#the blast record
from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)


#parsing blast output

len(blast_record.alignments)

E_VALUE_THRESH = 0.01
for alignment in blast_record.alignments:
    for hsp in alignmenthsps:
        if hsp.expect < E_VALUE_THRESH:
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('lenght', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query)
            print(hsp.match)
            print(hsp.sbjct)
    