import sys
from dateutil.parser import parse
fasta_fl = open(sys.argv[1])
gb_fl = sys.argv[2:]
output = open('hendra_edited.fasta', 'w')
gb_dict = {}
for fl in gb_fl:
    open_fl = open(fl)
    for line in open_fl:
        line = line.strip()
        if line.startswith('/collection_date'):
            date = parse(line.lstrip('/collection_date=').strip('"')).strftime('%Y-%m-%d')
            gb_dict[fl] = date
for line in fasta_fl:
    line = line.strip()
    if line.startswith('>'):
        items = line.split('/')
        ncbi_id = items[0].split(' ')[0].lstrip('>')
        country = items[1].lower()
        host = items[2].lower()
        year = items[3]
        town = items[4].split(' ')[0].rstrip(',').lower()
        output.write('>'+ncbi_id+'|'+'hendra|'+ncbi_id+'|'+gb_dict[ncbi_id+'.gb']+'|'+country+'|'+town+'|'+town+'|'+town+'|'+host+'\n')
    else:
        output.write(line+'\n')
