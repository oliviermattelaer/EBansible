#! /usr/bin/env python
"""Simple script taking the inventory.db file created by setup.yml 
and create the inventory file needed to deploy foss.

python create_inventory.py PATH_TO_INVENTORY.DB PATH_TO_NEW_INVENTORY 
"""

import sys
import os 
# check sanity of the input:
if len(sys.argv) != 3 or '--help' in sys.argv:
    print "syntax: python create_inventory.py PATH_TO_INVENTORY.DB PATH_TO_NEW_INVENTORY"
    print " PATH_TO_INVENTORY.DB is the file create by setup.yml"
    sys.exit(1)

inputfile = sys.argv[1]
outputfile = sys.argv[2]

if not os.path.exists(inputfile):
    print 'The first argument should be the file created by setup.yml: file is missing'
    sys.exit(1)
if os.path.exists(outputfile):
    print 'Do not want to remove existing file for the output please remove it first if you want to overwrite'
    sys.exit(1)

groups = {'easybuild':[], 'arch_represent':[]}
config_set = set()

for line in open(inputfile):
    if not line or line.startswith('#'):
        continue
    hostname, specification = line.split(None, 1)
    groups['easybuild'].append(hostname)
    if specification not in config_set:
        print line
        config_set.add(specification)
        groups['arch_represent'].append(hostname)
    
# Now groups contains the list of machine for the inventory. Need to format the output file:
outfile = open(outputfile,'w')
text="""
[easybuild]
  %(easybuild)s

[arch_represent]
  %(arch_represent)s
"""

outfile.write(text % {'easybuild': '\n  '.join(groups['easybuild']),
                      'arch_represent': '\n  '.join(groups['arch_represent'])
                     })



