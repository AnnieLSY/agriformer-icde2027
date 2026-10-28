# Third-party data sources and licenses

Raw datasets are not included by default. Each downloaded file must be checked
against `data/checksums.tsv`. This register distinguishes upstream-source
licenses from the license of a processed distribution.

| Dataset | Source | License status | Release handling |
|---|---|---|---|
| AUS-Wheat 2015 | Figshare DOI `10.25909/5becfa45c176f` | CC BY 4.0 | Download by DOI; derived analysis-ready file may be redistributed with attribution and change notice, but is omitted by default. |
| Ward wheat | Figshare DOI `10.6084/m9.figshare.7700012.v1` | CC BY 4.0 | Download by DOI; derived file omitted by default. |
| GABI wheat genotype | Dryad DOI `10.5061/dryad.n02v6wwzc` | CC0 | Download by DOI. |
| GABI wheat phenotype | e!DAL DOI `10.5447/ipk/2022/18` | CC BY 4.0 | Download by DOI; cite and identify modifications. |
| EasyGeSe processed data | Zenodo DOI `10.5281/zenodo.15348871` | CC BY 4.0 | Download processed X/Y/Z files; cite EasyGeSe and each upstream study. |
| Lentil upstream study | DOI `10.1002/tpg2.20002` | Independent upstream data license not declared in the verified record | Do not redistribute upstream raw files; use the CC BY 4.0 EasyGeSe processed layer. |
| Pine upstream study | DOI `10.1534/genetics.111.137026` | Independent upstream data license not verified | Do not redistribute upstream raw files; use the CC BY 4.0 EasyGeSe processed layer. |
| Rice upstream study | DOI `10.1038/ncomms1467` | Independent dataset license not verified; article license is not a dataset license | Do not redistribute upstream raw files; use the CC BY 4.0 EasyGeSe processed layer. |
| wheatG | Same GABI sources plus EasyGeSe processed layer | CC0 / CC BY 4.0 as above | Download by DOI and retain required attribution. |

No software license in this repository overrides a dataset or dependency
license. Before public release, every URL and license statement must be checked
again against its official landing page.

