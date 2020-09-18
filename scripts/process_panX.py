## DS 8/7/18
## format panX output - a tsv with each cluster in a
## separate row, and each cell containing [strain]|[locustag]
## into a two-column table with ID (locustag) and cluster
## and names this new file [inputfilename]_long.tsv

from optparse import OptionParser
import os

options = OptionParser(usage='%prog -i [input] -o [output]',
                       description="Specify input file and output file")

options.add_option("-i","--infile",dest="infile",
                   help="input filename")
options.add_option("-o","--outfile",dest="outfile",
                   help="output filename")

def long_table(infile, outfilename):
    with open(infile) as f:
        lines = [line.split() for line in f.readlines()]
    cluster = 0

    with open(outfilename,'w') as g:
        for line in lines:
            for element in line:
                locustag = element.split('|')[1]
                g.write(locustag+'\t'+str(cluster)+'\n')
            cluster+=1

def main():
    opts, args = options.parse_args()
    infilename = opts.infile
    outfilename = opts.outfile
    long_table(infilename, outfilename)

if __name__ == '__main__':
    main()
