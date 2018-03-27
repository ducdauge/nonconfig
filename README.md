# nonconfig: Non-configurationality in diachrony

This is an open source implementation of our measures and queries described in the following paper:

Edoardo Maria Ponti, Silvia Luraghi. To appear. **[Non-configurationality in diachrony: Correlations in local and global networks of Ancient Greek and Latin](https://www.academia.edu/35553047/Non-configurationality_in_diachrony_Correlations_in_local_and_global_networks_of_Ancient)**. In *Diachronica*.

If you use this software for academic research, please cite the paper in question:
```
@article{ponti2018non,
  author    = {Ponti, Edoardo Maria  and  Luraghi, Silvia},
  title     = {Non-configurationality in diachrony: Correlations in local and global networks of Ancient Greek and Latin},
  journal   = {Diachronica},
  year      = {To appear}
}
```

## Requirements

- Python
- R
- Perl

## Setup: data and softwares

- Download the relevant treebanks from [PROIEL](https://proiel.github.io/)

- Convert the treebanks from the ```.conll``` format to the ```.txt``` format using the script [conll2txt.py](scripts/conll2txt.py)
```
python conll2txt.py <in_filename>
```
- Convert the treebanks from the ```.txt``` format to the ```.pajek``` format using the software [txt2pajek](http://www.pfeffer.at/txt2pajek/)

- Convert the treebanks from the ```.conll``` format to the ```.pml``` format using the script [conll2pml.pl](scripts/conll2pml.pl)
```
./conll2pml.pl -r -p <out_dirname> <in_filename>
```

- Install [TrEd Tree Editor](https://ufal.mff.cuni.cz/tred/) and its extension [PML Tree Query](https://ufal.mff.cuni.cz/pmltq/)

## Spectrum analysis

Substitute the ```.pajek``` filename into the script [spectrum_analysis.R](spectrum_analysis.R) and run it in an R console.

## Queries on treebanks

Run a query on ```.pml``` files with TrEd to count and list:

- discontinuous constituents: [article-noun.pmltq](scripts/article-noun.pmltq), [adjective-noun.pmltq](scripts/adjective-noun.pmltq), or [verb-noun.pmltq](scripts/verb-noun.pmltq)

- pronominal objects of coordinated verbs: [pron_coord_verb.pmltq](scripts/pron_coord_verb.pmltq)

## Estimate the correlations
Run the following lines on R:

```r
library(Hmisc)
rcorr(as.matrix(<values>), type="pearson")
```

## License

Licensed under the terms of the GNU General Public License, either version 3 or (at your option) any later version. A full copy of the license can be found in LICENSE.txt.
