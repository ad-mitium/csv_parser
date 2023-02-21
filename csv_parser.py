#!/usr/bin/env python3
# Authored by Timothy Mui 4/4/2022

import csv
import argparse
from lib import version as ver
from lib import colors
from lib.action_description import action_description as act_desc
from lib.interactive import exit_on_error,continue_check


version_info = (0, 1, 2)
version = '.'.join(str(c) for c in version_info)

csv_data= []

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description=act_desc['desc']
    , 
    epilog=act_desc['end']
    )
parser.add_argument("input_file", help='''Enter input file ''')
parser.add_argument("output_file", help='''Enter output file ''')
parser.add_argument('-v','--version', action='version', version='%(prog)s {}'.format(version), 
                    help='show the version number and exit')
args = parser.parse_args()

#print(f"input:  {args.input_file!r}")
#print(f"output:  {args.output_file!r}")

input_file = args.input_file
output_file = args.output_file

try:
    with open(input_file, 'rt') as csvfile:
        csv_data_file = csv.reader(csvfile)
        next(csv_data_file)
        for col in csv_data_file:
            csv_cols = col[0].split(",")
            print(csv_cols)
            for i in csv_cols:
                csv_data.append(i) 
except FileNotFoundError as fnf_error:
        print(fnf_error)
except IOError:
    print("Unable to load "+input_file)

instances_counted = []
for i in csv_data:
    counted = csv_data.count(i)
    instances_counted.append((i,counted))    

with open(output_file,  'a+') as csvfile:
    csv_output = csv.writer(csvfile, delimiter=',')
    csv_output.writerow(instances_counted)
    
#output_file.write('\n')
#output_file.close()
#input_file.close()
