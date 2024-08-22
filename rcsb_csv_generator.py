import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import time
import os 

#? Program start
print('\n\nProgram starting')

#? Output file set up
def add_row(df, row_data):
    new_row_df = pd.DataFrame([row_data], columns=df.columns)
    df = pd.concat([df, new_row_df], ignore_index=True)
    return df

# filename = 'all_slc_genes.csv' # use this to run on all genes
filename = 'subset_slc_genes.csv' # use this to run on a subset of genes
genes_df = pd.read_csv(filename)
skipped_genes = []

for index, row in genes_df.iterrows():
    gene = row.iloc[0]
    new_row = [gene]

    #? Start Web Driver
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.get('https://www.rcsb.org/')
    time.sleep(5)  # Wait for the page to fully load

    entry = driver.find_element(By.ID, 'search-bar-input')
    entry.send_keys(gene)
    time.sleep(1)
    print('inputting gene', gene)
    entry.send_keys(Keys.RETURN)
    time.sleep(1)

    if True:
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//option[text()='-- Tabular Report --']"))
            )
            dropdown_option = driver.find_element(By.XPATH, "//option[text()='-- Tabular Report --']")
            dropdown = dropdown_option.find_element(By.XPATH, "..")
            
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(dropdown))
            print("Dropdown found and clickable.")
            
            dropdown.click()
            time.sleep(1)

            custom_report_option = dropdown.find_element(By.XPATH, "./option[@value='create_custom_report']")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(custom_report_option))
            custom_report_option.click()
            time.sleep(5)

            # STRUCTURE AUTHOR
            structure_author_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='entry.audit_author.name']"))
            )
            if not structure_author_checkbox.is_selected():
                structure_author_checkbox.click()
                print("Checkbox for Structure Author selected.")

            # PDB ID
            pdb_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='entry.rcsb_entry_container_identifiers.entry_id']"))
            )
            if not pdb_checkbox.is_selected():
                pdb_checkbox.click()
                print("Checkbox for PDB ID selected.")

            # RESOLUTION
            resolution_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='entry.rcsb_entry_info.diffrn_resolution_high.value']"))
            )
            if not resolution_checkbox.is_selected():
                resolution_checkbox.click()
                print("Checkbox for Resolution selected.") 

            # CRYSTAL GROWTH
            crystal_growth_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='entry.exptl_crystal_grow.pdbx_details']"))
            )
            if not crystal_growth_checkbox.is_selected():
                crystal_growth_checkbox.click()
                print("Checkbox for Crystal Growth Procedure selected.") 

            # Structural genomics project center name
            gen_proj_name_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='entry.pdbx_SG_project.full_name_of_center']"))
            )
            if not gen_proj_name_checkbox.is_selected():
                gen_proj_name_checkbox.click()
                print("Checkbox for Structural genomics project center name selected.") 
 
            # PUBMED Central ID
            pubmed_central_id_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='entry.pubmed.rcsb_pubmed_central_id']"))
            )
            if not pubmed_central_id_checkbox.is_selected():
                pubmed_central_id_checkbox.click()
                print("Checkbox for PUBMED Central ID selected.") 
 
             # PUBMED ID
            pubmed_id_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='entry.pubmed.rcsb_pubmed_container_identifiers.pubmed_id']"))
            )
            if not pubmed_id_checkbox.is_selected():
                pubmed_id_checkbox.click()
                print("Checkbox for PUBMED ID selected.") 
 
            # RELEASE DATE
            release_date_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='entry.rcsb_accession_info.initial_release_date']"))
            )
            if not release_date_checkbox.is_selected():
                release_date_checkbox.click()
                print("Checkbox for Release Date selected.") 

            # LIGAND
            ligand_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='entry.rcsb_binding_affinity.comp_id']"))
            )
            if not ligand_checkbox.is_selected():
                ligand_checkbox.click()
                print("Checkbox for Ligand selected.") 

            # DISULFIDE BONDS
            disulfide_bonds_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='entry.rcsb_entry_info.disulfide_bond_count']"))
            )
            if not disulfide_bonds_checkbox.is_selected():
                disulfide_bonds_checkbox.click()
                print("Checkbox for Disulfide Bonds selected.")   

            # Structure Determination Methodology
            structure_determination_methodology_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='entry.rcsb_entry_info.structure_determination_methodology']"))
            )
            if not structure_determination_methodology_checkbox.is_selected():
                structure_determination_methodology_checkbox.click()
                print("Checkbox for Structure Determination Methodology selected.")

            # DOI
            doi_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='entry.rcsb_primary_citation.pdbx_database_id_DOI']"))
            )
            if not doi_checkbox.is_selected():
                doi_checkbox.click()
                print("Checkbox for DOI selected.")

            # Title of Paper
            title_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='entry.rcsb_primary_citation.title']"))
            )
            if not title_checkbox.is_selected():
                title_checkbox.click()
                print("Checkbox for Title of Paper selected.")

            # Expression Host 
            expression_host_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='polymer_entities.rcsb_entity_host_organism.ncbi_scientific_name']"))
            )
            if not expression_host_checkbox.is_selected():
                expression_host_checkbox.click()
                print("Checkbox for Expression Host selected.")

            # Source Organisms 
            source_organisms_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='polymer_entities.rcsb_entity_source_organism.ncbi_scientific_name']"))
            )
            if not source_organisms_checkbox.is_selected():
                source_organisms_checkbox.click()
                print("Checkbox for Source Organisms selected.")
                
            # Molecular Weight
            molecular_weight_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='polymer_entities.rcsb_polymer_entity.formula_weight']"))
            )
            if not molecular_weight_checkbox.is_selected():
                molecular_weight_checkbox.click()
                print("Checkbox for Molecular Weight selected.")
                
            # Oligomeric State
            oligomeric_state_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='assemblies.rcsb_struct_symmetry.oligomeric_state']"))
            )
            if not oligomeric_state_checkbox.is_selected():
                oligomeric_state_checkbox.click()
                print("Checkbox for Oligomeric State selected.")
                 
            # Stoichiometry 
            stoichiometry_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='polymer_entities.rcsb_polymer_entity.formula_weight']"))
            )
            if not stoichiometry_checkbox.is_selected():
                stoichiometry_checkbox.click()
                print("Checkbox for Stoichiometry selected.")   
                 
            # Glycosylation Site 
            glycosylation_site_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='branched_entities.branched_entity_instances.rcsb_branched_struct_conn.role']"))
            )
            if not glycosylation_site_checkbox.is_selected():
                glycosylation_site_checkbox.click()
                print("Checkbox for Glycosylation Site selected.")                      
        
            # Click the "Run Report" button
            run_report_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='qb-btn' and contains(text(),'Run Report')]"))
            )
            run_report_button.click()
            print("\nRun Report button clicked.")

            time.sleep(10)
            driver.save_screenshot("screenshot.png")

        except Exception as e:
            print(f'Something went wrong: {gene}')
            skipped_genes.append(gene)
            driver.quit()
            continue

    #? Custom Report Formatted
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "tabular-report")))
    wait = WebDriverWait(driver, 10)
    table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tabular-report")))
    
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Extract the headers
    headers = []
    header_elements = table.find_elements(By.XPATH, ".//thead/tr/th")
    for header in header_elements:
        colspan = int(header.get_attribute("colspan")) if header.get_attribute("colspan") else 1
        for _ in range(colspan):
            headers.append(header.text.strip())
    headers = headers[19:]
    print(headers)

    # Extract data rows
    data = []
    for row in rows[1:]:
        cols = row.find_elements(By.TAG_NAME, "td")
        data.append([col.text for col in cols])

    # Create a DataFrame
    output_df = pd.DataFrame(data, columns=headers)
    output_df['SLC_ID'] = gene

    # Display the DataFrame
    print(output_df)

    #? Add to CSV
    output_filename = "output.csv" # edit this filename for different output saving

    file_exists = os.path.isfile(output_filename)
    output_df.to_csv(output_filename, mode='a', header=not file_exists, index=False)


    driver.quit()

print(skipped_genes)