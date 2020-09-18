# DS 6/5/18
# Turn CD-HIT (or UCLUST) output into a tab-separated table
# [seqID]   [clusterID]


from optparse import OptionParser


options = OptionParser(usage='%prog -i [input] -o [output]',
                       description="Specify input and output files. Add --UC for uclust table")

options.add_option("-i","--infile",dest="inputfile",
                   help="input file (.clstr)")

options.add_option("-o","--outfile",dest="outputfile",
                   help="output file (.tsv)")

options.add_option("--UC", dest = "uclust",action="store_true", default = False)


#find string between two specified strings
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def process_CDHIT(infile, outfile):
    with open(infile) as f:
        lines = f.readlines()
        cluster = 0
        with open(outfile,'w') as g:
            for line in lines:
                if line[0] == ">":
                    cluster = str(int(line.split()[1])+1)
                else:
                    seqID = find_between(line, ">","...")
                    g.write(seqID+"\t"+cluster+"\n")
                    
def process_UC(infile, outfile):
    with open(infile) as f:
        lines = f.readlines()
        cluster = 0
        with open(outfile,'w') as g:
            for line in lines:
                if line[0] == "S" or line[0] == "H":
                    splitline = line.split()
                    cluster = str(int(splitline[1])+1)
                    seqID = splitline[8]
                    g.write(seqID+"\t"+cluster+"\n")
                else:
                    pass
                    

def main():
    opts, args = options.parse_args()
    infile = opts.inputfile
    outfile = opts.outputfile
    uc = opts.uclust

    if uc:
        process_UC(infile,outfile)
    else:
        process_CDHIT(infile, outfile)


if __name__ == '__main__':
    main()
