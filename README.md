
Get data
```
git clone https://github.com/cclab-brca/mutationalProfiles.git
```

Get Reference Genome
```
synapse get syn3241340
gunzip Homo_sapiens_assembly19.fasta.gz
samtools faidx Homo_sapiens_assembly19.fasta
```

Working environment
```
./shell.sh
```


MetaBric to MAF
```
./metabric_convert.py mutationalProfiles/Data/somaticMutations.txt > somaticMutations.maf
```


MAF2VCF
```
perl /opt/vcf2maf/maf2vcf.pl --input-maf somaticMutations.maf --output-dir out --ref-fasta Homo_sapiens_assembly19.fasta
```

Output
```
cat out/somaticMutations.vcf
```