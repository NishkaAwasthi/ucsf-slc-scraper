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
    "GENE", "PDB ID", "STRUCTURE AUTHOR", "RESOLUTION", 
    "PUBMED CENTRAL ID", "PUBMED ID", "RELEASE DATE", 
    "PUBLICATION YEAR", "DOI", "TITLE OF PAPER", 
    "EXPRESSION HOST", "SOURCE ORGANISM", 
    "MOLECULAR WEIGHT", "STOICHIOMETRY"
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
                        
            # PDB ID            
            print('PDB ID:', structure)
            new_row.append(structure)

            try:
                # STRUCTURE AUTHOR
                li_element = driver.find_element(By.ID, 'header_deposition-authors')
                a_tags = li_element.find_elements(By.TAG_NAME, 'a')
                authors = [a.text for a in a_tags]
                print('AUTHORS:', authors)
                new_row.append(authors)
            except:
                print('AUTHORS: Not found')
                new_row.append('')

            try:
                # RESOLUTION
                li_element = driver.find_element(By.ID, 'exp_header_0_em_resolution')
                resolution_text = li_element.text
                resolution = resolution_text.split('Resolution:')[-1].strip()
                print('RESOLUTION:', resolution)
                new_row.append(resolution)
            except:
                print('RESOLUTION: Not found')
                new_row.append('')


            try:
                # PUBMED CENTRAL ID
                pubmed_id_li = driver.find_element(By.ID, 'pubmedLinks')
                pubmed_id_a = pubmed_id_li.find_element(By.TAG_NAME, 'a')
                pubmed_central_id = pubmed_id_a.text
                print('PUBMED CENTRAL ID:', pubmed_central_id)
                new_row.append(pubmed_central_id)
            except:
                print('PUBMED CENTRAL ID: Not found')
                new_row.append('')

            try:
                # PUBMED ID
                pubmed_id_li = driver.find_element(By.ID, 'pubmedLinks')
                pubmed_id_a = pubmed_id_li.find_element(By.TAG_NAME, 'a')
                pubmed_id = pubmed_id_a.text
                print('PUBMED ID:', pubmed_id)
                new_row.append(pubmed_id)
            except:
                print('PUBMED ID: Not found')
                new_row.append('')

            try:
                # RELEASE DATE
                li_element = driver.find_element(By.ID, 'header_deposited-released-dates')
                text = li_element.text
                released_date = text.split('Released:')[-1].strip()
                released_date = released_date.split()[0]
                print('RELEASED DATE:', released_date)
                new_row.append(released_date)
            except:
                print('RELEASE DATE: Not found')
                new_row.append('')

            try:
                # PUBLICATION YEAR
                div_element = driver.find_element(By.ID, 'primarycitation')
                p_tag = div_element.find_element(By.TAG_NAME, 'p')
                publication_year = p_tag.text
                print('PUBLICATION YEAR', publication_year[1:5])
                new_row.append(publication_year)
            except:
                print('PUBLICATION YEAR: Not found')
                new_row.append('')

            try:
                # DOI
                li_element = driver.find_element(By.ID, 'header_doi')
                a_tag = li_element.find_element(By.TAG_NAME, 'a')
                doi_url = a_tag.get_attribute('href')
                print('DOI:', doi_url)
                new_row.append(doi_url)
            except:
                print('DOI: Not found')
                new_row.append('')

            try:
                # TITLE OF PAPER
                div_element = driver.find_element(By.ID, 'primarycitation')
                h4_tag = div_element.find_element(By.TAG_NAME, 'h4')
                paper_title = h4_tag.text
                print('TITLE OF PAPER:', paper_title)
                new_row.append(paper_title)
            except:
                print('TITLE OF PAPER: Not found')
                new_row.append('')

            try:
                # EXPRESSION HOST
                li_element = driver.find_element(By.ID, 'header_expression-system')
                a_tag = li_element.find_element(By.TAG_NAME, 'a')
                expression_system = a_tag.text
                print('EXPRESSION HOST:', expression_system)
                new_row.append(expression_system)
            except:
                print('EXPRESSION HOST: Not found')
                new_row.append('')

            try:
                # SOURCE ORGANISM
                li_element = driver.find_element(By.ID, 'header_organism')
                a_tag = li_element.find_element(By.TAG_NAME, 'a')
                source_organism = a_tag.text
                print('SOURCE ORGANISM:', source_organism)
                new_row.append(source_organism)
            except:
                print('SOURCE ORGANISM: Not found')
                new_row.append('')

            try:
                # MOLECULAR WEIGHT
                weight_li = driver.find_element(By.ID, 'contentStructureWeight')
                weight_text = weight_li.text
                molecular_weight = weight_text.split(': ')[1].strip()
                print('MOLECULAR WEIGHT:', molecular_weight)
                new_row.append(molecular_weight)
            except:
                print('MOLECULAR WEIGHT: Not found')
                new_row.append('')

            # try: 
            #     # Ligands
            #     ligand_ids = []
            #     for i in range(1, 100):  # You might need to adjust this range based on the number of rows
            #         try:
            #             row_id = f"ligand_row_{i}"  
            #             element = driver.find_element(By.ID, row_id)
            #             link = element.find_element(By.TAG_NAME, 'a')
            #             ligand_id = link.text
            #             ligand_ids.append(ligand_id)
            #         except Exception as e:
            #             print(f"Exception for row {i}: {e}")
            #             break
            #         print(ligand_ids)

            # except:
            #     print('LIGANDS: Not found')

            try:
                # STOICHIOMETRY 
                stoichiometry_element = driver.find_element(By.XPATH, "//strong[text()='Global Stoichiometry']/following-sibling::text()[1]")
                stoichiometry = stoichiometry_element.text.strip()
                print('STOICHIOMETRY:', stoichiometry)
                new_row.append(stoichiometry)
            except:
                print('STOICHIOMETRY: Not found')
                new_row.append('')

            # Crystallization Method
            # Crystal growth procedure 
            # Structural genomics project center name 
            # XRAY/EM
            # Disulfide bonds 
            # Structure determination methodology
            # Oligomeric State
            # Glycosylation Site

            print('row made')
            output_df = add_row(output_df, new_row)
            print('df updated')

    except:
        print('Something went wrong.')

driver.quit()

output_filename = "output.csv" # edit this filename for different output saving
output_df.to_csv(output_filename, index=False)
