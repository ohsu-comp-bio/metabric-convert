
Get data
```
git clone https://github.com/cclab-brca/mutationalProfiles.git
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
perl /opt/vcf2maf/maf2vcf.pl --input-maf somaticMutations.maf --output-dir out --ref-fasta Homo_sapiens.GRCh37.75.dna.primary_assembly.fa.gz
```

