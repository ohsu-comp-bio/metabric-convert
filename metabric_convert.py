#!/usr/bin/env python

import sys
import csv

MAF_HEADER = [
    "Hugo_Symbol", 
    "Entrez_Gene_Id",
    "Center",
    "NCBI_Build",
    "Chromosome",
    "Start_Position",
    "End_Position",
    "Strand",
    "Variant_Classification",
    "Variant_Type",
    "Reference_Allele",
    "Tumor_Seq_Allele1",
    "Tumor_Seq_Allele2",
    "dbSNP_RS",
    "dbSNP_Val_Status",
    "Tumor_Sample_Barcode",
    "Matched_Norm_Sample_Barcode",
    "Match_Norm_Seq_Allele1",
    "Match_Norm_Seq_Allele2",
    "Tumor_Validation_Allele1",
    "Tumor_Validation_Allele2",
    "Match_Norm_Validation_Allele1",
    "Match_Norm_Validation_Allele2",
    "Verification_Status",
    "Validation_Status",
    "Mutation_Status",
    "Sequencing_Phase",
    "Sequence_Source",
    "Validation_Method",
    "Score",
    "BAM_File",
    "Sequencer",
    "Tumor_Sample_UUID",
    "Matched_Norm_Sample_UUID",
    "Amino_Acid_Change"
]


snp_variant_type_mapping = {
    "missense SNV" : "Missense_Mutation",
    "nonsense SNV" : "Nonsense_Mutation",
    "stoploss" : "stoploss",
    "synonymous SNV" : "Silent",
}

del_variant_type_mapping = {
    "frameshift indel" : "Frame_Shift_Del",
    "inframe indel" : "In_Frame_Del",
}

ins_variant_type_mapping = {
    "frameshift indel" : "Frame_Shift_Ins",
    "inframe indel" : "In_Frame_Ins",
}


"""
MAF Types:

Frame_Shift_Del
Frame_Shift_Ins
In_Frame_Del
In_Frame_Ins
Missense_Mutation
Nonsense_Mutation
Silent
Splice_Site
stoploss
"""


def variant_type(row):
    if row['location'].count("splicing") > 0:
        return "Splice_Site"
    else:
        if len(row['refAllele']) == len(row["altAllele"]):
            return snp_variant_type_mapping[row['mutationType']]
        if  len(row['refAllele']) > len(row["altAllele"]):
            return del_variant_type_mapping[row['mutationType']]
        if  len(row['refAllele']) < len(row["altAllele"]):
            return ins_variant_type_mapping[row['mutationType']]
        
        
def fix_chr(row):
    return row["chr"].replace("chr", "")

def fix_start(row):
    return "%s" % (int(row['start']))

def fix_end(row):
    return "%s" % (int(row['end']))


MAPPING = {
    "Tumor_Sample_Barcode" : "sample",
    "Chromosome" : fix_chr,
    "Start_Position" : fix_start, #"start",
    "End_Position" : fix_end, #"end",
    "Reference_Allele" : "refAllele",
    "Tumor_Seq_Allele1" : "altAllele",
    "Tumor_Seq_Allele2" : "altAllele",
    "Hugo_Symbol" : "gene",
    
    "Variant_Classification" : variant_type
    #"vaf"
    #"reads"
    #"location"
    #"exon"
    #"codon"
    #"mutationType"
    #"oldCodon"
    #"newCodon"
}

with open(sys.argv[1]) as handle:
    print "\t".join(MAF_HEADER)
    reader = csv.DictReader(handle, delimiter="\t")
    for line in reader:
        data = {}
        for k,v in MAPPING.items():
            if isinstance(v, basestring):
                data[k] = line[v]
            else:
                data[k] = v( line )
        
        print "\t".join( list( data.get(i, "") for i in MAF_HEADER ) )
