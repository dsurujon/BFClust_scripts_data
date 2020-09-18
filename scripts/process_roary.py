## DS 8/4/18
## format Roary presence-absence table, and turn into
## a long-form tsv

import os
import pandas as pd
from optparse import OptionParser

options = OptionParser(usage='%prog -i [input] -o [output]',
                       description="Specify input and output files. ")

options.add_option("-i","--infile",dest="inputfile",
                   help="input file (.cvs)")

options.add_option("-o","--outfile",dest="outputfile",
                   help="output file (.tsv)")


def process_roary(infilename, outfilename):
    roary = pd.read_csv(infilename)
    roary = roary.drop(['Non-unique Gene name', 'Annotation', 
       'No. sequences', 'Avg sequences per isolate', 'Genome Fragment',
       'Order within Fragment', 'Accessory Fragment',
       'Accessory Order with Fragment', 'QC', 'Min group size nuc',
       'Max group size nuc', 'Avg group size nuc', 'No. isolates'], axis=1)
    roary.Gene = [int(k.split('_')[1]) for k in roary.Gene]
    strain_columns = roary.columns[1:]
    roary_melt = pd.melt(roary, id_vars = ['Gene'], value_vars = strain_columns, var_name = 'strain', value_name='locus_tag')
    roary_clean = roary_melt.dropna()
    roary_out = roary_clean[['locus_tag', 'Gene']]
    roary_out.to_csv(outfilename, sep='\t', header=False, index=False)

def main():
    opts, args = options.parse_args()
    infile = opts.inputfile
    outfile = opts.outputfile

    process_roary(infile, outfile)


if __name__ == '__main__':
    main()
	
