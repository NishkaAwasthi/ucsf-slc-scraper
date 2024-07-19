# ucsf-slc-scraper

To run subset of slc genes:
    - Edit `subset_slc_genes.csv` to contain the list of genes you would like to 
        run. Ensure that it has Genes or some sort of header.
    - Comment out line 25 in rcsb_scraper.py [# filename = 'all_slc_genes.csv']
    - Ensure line 26 is running [filename = 'subset_slc_genes.csv']

To run ALL slc genes:
    - Comment out line 26 in rcsb_scraper.py [# filename = 'subset_slc_genes.csv']
    - Ensure line 25 is running [filename = 'all_slc_genes.csv']

Renaming the output file: 
    - Edit line 246 so that filename is the name of the csv you want to generate.
    - WARN: If a csv of that name already exists, it will be OVERWRITTEN
