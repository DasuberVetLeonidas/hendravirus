from __future__ import print_function
import os, sys
# we assume (and assert) that this script is running from the virus directory, i.e. inside H7N9 or zika
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import base.prepare
from base.prepare import prepare
from datetime import datetime
from base.utils import fix_names
import argparse

def collect_args():
    """Returns a Hendra-specific argument parser.
    """
    parser = base.prepare.collect_args()
    parser.set_defaults(
        viruses_per_month=1,
        file_prefix="hendra"
    )
    return parser

# dropped_strains = [
# ]

config = {
    "dir": "hendra",
    "file_prefix": "hendra",
    "title": "Real-time tracking of Hendra virus transmission",
    "maintainer": ["Matt and Leo", ""],
    "input_paths": ["hendra_edited.fasta"],
    "header_fields": { 0:'strain', 3:'date', 4:'country', 5:'town', 8: 'host',
                       },
    # "filters": (
    # ),
    # "subsample": {
    #     "category": lambda x:(x.attributes['date'].year, x.attributes['date'].month, x.attributes['town']),
    # },
    "colors": ["authors", "country", "town", "host"],
    "color_defs": ["./colors.tsv"],
    "lat_longs": ["country", "town"],
    "auspice_filters": ["accession", "country", "town", "host"],
    "reference": {
        "path": "./hendra.gb",
        "metadata": {
            'strain': "Hendra henipavirus", "accession": "NC_001906", "date": "07-AUG-2013",
            'host': "horse", 'country': "australia"
        },
        "include": 2,
        "genes": ['N', 'P/V/C', 'M', 'F', 'G', 'L']
    }
}

if __name__=="__main__":
    parser = collect_args()
    params = parser.parse_args()
    # if params.viruses_per_month == 0:
    #     config["subsample"] = False
    # else:
    #     config["subsample"]["threshold"] = params.viruses_per_month
    #
    if params.sequences is not None:
        config["input_paths"] = params.sequences

    if params.file_prefix is not None:
        config["file_prefix"] = params.file_prefix

    runner = prepare(config)
    runner.load_references()
    print('runner.load_reference finished')
    # runner.applyFilters()
    runner.ensure_all_segments()
    print('runner.ensure_all_segments finished')
    runner.subsample()
    print('runner.subsample finished')
    runner.colors()
    runner.latlongs()
    runner.write_to_json()
