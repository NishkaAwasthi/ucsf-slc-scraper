import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Output file set up
def add_row(df, row_data):
    new_row_df = pd.DataFrame([row_data], columns=df.columns)
    df = pd.concat([df, new_row_df], ignore_index=True)
    return df

columns = [
    "GENE", "PDB ID", "RESOLUTION", "XRAY/EM", "METHOD", 
    "AGGREGATION STATE", "RECONSTRUCTION METHOD"
]
output_df = pd.DataFrame(columns=columns)

# Program start
print('Program starting')

# filename = 'all_slc_genes.csv' # use this to run on all genes
filename = 'subset_slc_genes.csv' # use this to run on a subset of genes
genes_df = pd.read_csv(filename)

driver = webdriver.Safari()
driver.maximize_window()

driver.get('https://www.rcsb.org/')

for index, row in genes_df.iterrows():
    gene = row.iloc[0]
    new_row = [gene]

    entry = driver.find_element(By.ID, 'search-bar-input')
    entry.send_keys(gene)
    time.sleep(1)
    entry.send_keys(Keys.RETURN)
    time.sleep(3)

    try:
        dropdown_option = driver.find_element(By.XPATH, "//option[text()='-- Tabular Report --']")
        dropdown = dropdown_option.find_element(By.XPATH, "..")

        entry_ids_option = dropdown.find_element(By.XPATH, "./option[@value='pdb_ids']")
        entry_ids_option.click()
        time.sleep(2)

        report_div = driver.find_element(By.CLASS_NAME, 'TabularReportResults')
        divs = report_div.find_elements(By.TAG_NAME, 'div')
        if len(divs) > 1:
            structure_ids_div = divs[1]
            structure_ids_text = structure_ids_div.text
        else:
            print(f"No structure IDs found for gene '{gene}'")
            continue 

        result = [item.strip() for item in structure_ids_text.split(',')]

        for structure in result:
            new_row = []

            print('\n\nGENE: ', gene)
            new_row.append(gene)

            print('STRUCTURE: ', structure)
            base_url = 'https://www.rcsb.org/structure/'
            driver.get(base_url + structure)
            time.sleep(3)  # Allow time for the new page to load
            
            # PDB ID            
            print('PDB ID:', structure)
            new_row.append(structure)

            try:
                # RESOLUTION
                li_element = driver.find_element(By.ID, 'exp_header_0_em_resolution')
                resolution_text = li_element.text
                resolution = resolution_text.split('Resolution:')[-1].strip()
                print('RESOLUTION:', resolution)
                new_row.append(resolution)
            except:
                print('RESOLUTION (EM): Not found')

                # RESOLUTION (from Diffraction)
                try:
                    # RESOLUTION
                    li_element = driver.find_element(By.ID, 'exp_header_0_diffraction_resolution')
                    resolution_text = li_element.text
                    resolution = resolution_text.split('Resolution:')[-1].strip()
                    print('RESOLUTION:', resolution)
                    new_row.append(resolution)
                except:
                    print('RESOLUTION (D): Not found')
                    new_row.append('')

            try:
                # XRAY/EM
                xray_element = driver.find_element(By.XPATH, "//strong[text()='Global Stoichiometry']/following-sibling::text()[1]")
                xray = xray_element.text.strip()
                print('XRAY/EM:', xray)
                new_row.append(xray)
            except:
                print('XRAY/EM: Not found')
                new_row.append('')

            try:
                # METHOD
                li_element = driver.find_element(By.ID, 'exp_header_0_method')
                method_text = li_element.text.split('Method:')[-1].strip()
                print('METHOD:', method_text)
                new_row.append(method_text)
            except:
                print('METHOD: Not found')
                new_row.append('')

            try:
                # AGGREGATION STATE
                li_element = driver.find_element(By.ID, 'exp_header_0_em_aggregationState')
                aggregation_text = li_element.text
                aggregation_state = aggregation_text.split('Aggregation State:')[-1].strip()
                print('AGGREGATION STATE:', aggregation_state)
                new_row.append(aggregation_state)
            except:
                print('AGGREGATION STATE: Not found')
                new_row.append('')

            try:
                # RECONSTRUCTION METHOD
                li_element = driver.find_element(By.ID, 'exp_header_0_em_reconstructionMethod')
                reconstruction_text = li_element.text
                reconstruction_method = reconstruction_text.split('Reconstruction Method:')[-1].strip()
                print('RECONSTRUCTION METHOD:', reconstruction_method)
                new_row.append(reconstruction_method)
            except:
                print('RECONSTRUCTION METHOD: Not found')
                new_row.append('')

            print(new_row)
            output_df = add_row(output_df, new_row)

    except:
        print("Something went wrong")

driver.quit()

output_filename = "raw_output_web_scraping.csv" # edit this filename for different output saving
output_df.to_csv(output_filename, index=False)
