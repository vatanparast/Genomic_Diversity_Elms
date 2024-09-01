#!/usr/bin/env python3

import pandas as pd

# Load the .bim PLINK data
bim_file = './glabra-only_LD-pruned.bim'
bim_data = pd.read_csv(bim_file, delim_whitespace=True, header=None,
                       names=['CHR', 'SNP_ID', 'GEN_DIST', 'BP_POS', 'A1', 'A2'])

# Prepare DataFrame as required by CMplot R package
cmplot_data = bim_data[['SNP_ID', 'CHR', 'BP_POS']]
cmplot_data.columns = ['name', 'chromosome', 'position']

# Save the data to a CSV file or use the DataFrame directly in R
cmplot_data.to_csv('glabra-only_LD-pruned.bim.csv', index=False)


