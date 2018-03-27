# nonconfig
Code and queries to measure non-configurational properties in Ancient Greek and Latin

## Setup: data and softwares

- Download the relevant treebanks from [PROIEL](https://proiel.github.io/)

- Convert the treebanks from the ```.conll``` format to the ```.pml``` format using the script [conll2pml.pl](scripts/conll2pml.pl)
```
./conll2pml.pl -r -p <out_dirname> <in_filename>
```

- Install [TrEd Tree Editor](https://ufal.mff.cuni.cz/tred/) and its extension [PML Tree Query](https://ufal.mff.cuni.cz/pmltq/)


## Estimate the correlations
Run the following lines on R:

```r
library(Hmisc)
rcorr(as.matrix(<values>), type="pearson")
```
