from Bio import SeqIO
from Bio import Entrez
import sys
Entrez.email="##############"
for i in open(sys.argv[1]):
    record_id = i.strip()
    new_handle = Entrez.efetch(db="nucleotide", id=record_id, rettype="gb", retmode="genbank")
    seq_record = SeqIO.read(new_handle, "genbank")
    print(record_id)
    SeqIO.write(seq_record, record_id+'.gb', "genbank")
