from dateutil.parser import parse
import sys
fasta_fl = open('hendra_genome.fasta')
gb_fl = open('filelist.txt')
output = open('hendra_edited.fasta', 'w')
gb_dict = {}
strain = 'Hendra henipavirus'
for file in gb_fl:
    open_fl = open(file.strip())
    for line in open_fl:
        line = line.strip()
        if line.startswith('/collection_date'):
            date = parse(line.lstrip('/collection_date=').strip('"')).strftime('%Y-%m-%d')
            print(date)
for line in fasta_fl:
    line=line.strip()
    if line.startswith('>'):
        items = line.split('/')
        ncbi_id = items[0].split(' ')[0].lstrip('>')
        country = items[1].lower()
        host = items[2].lower()
        year = items[3]
        town = items[4].split(' ')[0].rstrip(',').lower()
        output.write('>'+strain+'|'+'hendra|'+ncbi_id+'|'+gb_dict[ncbi_id+'.gb']+'|'+country+'|'+town+'|'+town+'|'+town+'\n')
    else:
        output.write(line+'/n')
