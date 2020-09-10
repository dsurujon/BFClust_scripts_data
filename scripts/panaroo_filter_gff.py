from BCBio import GFF
import gffutils as gff
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from io import StringIO
from optparse import OptionParser
import re
import os


options = OptionParser(usage='%prog -i [inputdir] -o [outputdir]',
                       description="Specify input (for .gbk) and output (for .gff) directories")

options.add_option("-i","--indir",dest="inputdir",
                   help="input directory of gff3 files")
options.add_option("-o","--outdir",dest="outputdir",
                   help="output directory of panaroo-compatible gff3 files")


def process_gff(gff_file_name, out_file):

	#gff_file_name = "../GFF3/RefSeq/NC_018593.gff"
	gff_file = open(gff_file_name, 'r')
	#Split file and parse
	lines = gff_file.read().replace(',','')
	split = lines.split('##FASTA')
	gff_file.close()

	with StringIO(split[1]) as temp_fasta:
		sequences = list(SeqIO.parse(temp_fasta, 'fasta'))

	sequences_dict = {s.id:s for s in sequences}
	db = gff.create_db(gff_file_name, dbfn=":memory:")
	feature_list = list(db.all_features())

	i = 0

	while i<len(feature_list):
		entry = feature_list[i]
		mycontig = sequences_dict[entry.chrom].seq
		geneseq = mycontig[(entry.start-1):entry.stop]
		if entry.strand == "-":
			geneseq = geneseq.reverse_complement()
		translated = Seq.translate(geneseq)
		if len(geneseq)%3 !=0 or '*' in translated[:-1]:
			feature_list.pop(i)
		else: 
			i+=1

	#out_file = 'NC_018593_test.gff'
	newgff = list(sequences_dict.values())

	header = split[0].split('\n')[:2]
	with open(out_file, "w") as g:
		g.write(header[0]+'\n'+header[1]+'\n')
		for feature in feature_list:
			g.write(str(feature) + '\n')
		g.write("##FASTA\n")
		SeqIO.write(sequences, g, 'fasta')

def main():
    opts, args = options.parse_args()
    inputdir = opts.inputdir
    outputdir = opts.outputdir

    gfffiles = os.listdir(inputdir)
    gfffiles = [g for g in gfffiles if g[-4:]==".gff"]

    for infile in gfffiles:
        print("processing ", infile)
        
        try:
        	fullinputfile = os.path.join(inputdir, infile)
        	fulloutputfile = os.path.join(outputdir, infile)

        	process_gff(fullinputfile, fulloutputfile)
        except OverflowError: pass



if __name__ == '__main__':
    main()