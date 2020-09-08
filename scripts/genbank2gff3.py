## Defne Surujon
## July 17, 2018

## Make a gff3 file from genbank

## Special case for annotated gbks containing multiple contigs



from Bio import SeqIO
from Bio import Seq
from optparse import OptionParser
import re
import os


options = OptionParser(usage='%prog -i [inputdir] -o [outputdir]',
                       description="Specify input (for .gbk) and output (for .gff) directories")

options.add_option("-i","--indir",dest="inputdir",
                   help="input directory of genbank files")
options.add_option("-o","--outdir",dest="outputdir",
                   help="output directory of gff3 files")


def make_gff_from_gbk(infile, outfile):
    mystrain=list(SeqIO.parse(infile,"genbank"))

    strainID = os.path.split(infile)[-1][:15]

    totallen = 0
    for contig in mystrain:
    	totallen += len(contig.seq)
    
    featuretable = []
    stranddict = {1:'+',-1:'-'}
    
    for contig in mystrain:
        for thisfeature in contig.features:
            if thisfeature.type=="CDS":
                try:
                    thisline = ["." for i in range(0,9)]
                    thisline[0] = contig.id
                    thisline[3] = str(int(thisfeature.location.start)+1)
                    thisline[4] = str(int(thisfeature.location.end))
                    thisline[6] = stranddict[thisfeature.location.strand]
                    thisline[2] = "CDS"
                    thisline[7] = "0"
                    thisline[8] = "ID="+thisfeature.qualifiers['locus_tag'][0]
                    
                    featuretable.append(thisline)
                except KeyError: pass

    
    with open(outfile,'w') as g:
        g.write("##gff-version 3\n")
        g.write("##sequence-region "+strainID+" 1 "+str(totallen)+"\n")
        #write all lines
        for line in featuretable:
            linestr = [str(i) for i in line]
            g.write("\t".join(linestr)+"\n")
        g.write("##FASTA\n")
        
        #write each contig separately
        for contig in mystrain:
            g.write(">"+contig.id+"\n")

            for i in range(0,len(contig.seq),60):
                g.write(str(contig.seq[i:i+60])+"\n")
    



def main():
    opts, args = options.parse_args()
    inputdir = opts.inputdir
    outputdir = opts.outputdir

    gbkfiles = os.listdir(inputdir)
    gbkfiles = [g for g in gbkfiles if g[-4:]==".gbk"]

    for infile in gbkfiles:
        print("processing ", infile)
        
        try:
        	fullinputfile = os.path.join(inputdir, infile)
        	outfile = '.'.join(infile.split('.')[:-1])+".gff"
        	fulloutputfile = os.path.join(outputdir, outfile)

        	make_gff_from_gbk(fullinputfile, fulloutputfile)
        except OverflowError: pass



if __name__ == '__main__':
    main()
