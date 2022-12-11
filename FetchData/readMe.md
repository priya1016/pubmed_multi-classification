
## Script to fetch and preprocess the raw data. 

The data does not contain the labels, so we fetch the data from huggingface into raw_batch_data, then add the root category and store the result into training_data.  

File Summary

* rinsepubmed 
This folder contains the [huggingface script](https://huggingface.co/datasets/pubmed). We have modified it a little to extract chunks at a time, because the total size of the data is approx. 79GB and growing. It also has a dataset_infos.json that has information about each chunk and the total size.

* training_data
This link contains final processed training data. This has the label categories added to each batch file. [Link](https://drive.google.com/drive/folders/1Xnw1tM4yddlSmlREkQ9bRwkBLYEsll-8?usp=share_link)

* raw_batch_data
Folder contains the raw processed_batch_ files that we get by running pull_data.ipynb. The drive link to raw data.

* batch_cleaner.py
Run the script to process the batch data and store the training data files to training data directory.

* batch_cleaner.ipynb
This notebook takes the intermediate processed data, and outputs a final processed training data.

* desc2022.xml
This file has all the matadata on the MeSH terms. Click the link to [download](https://drive.google.com/file/d/1K5I7QbrO4-w3j7jm3d5bj2dq4UbKno5R/view?usp=share_link).

* descriptor_mapper_raw.csv
Intermediate processed file containing Unique ID,Descriptor Name,Tree Number

* descriptor_mapper.csv
Final descriptor processed file, with extract root cateogory. The file has Descriptor Name,Root Category,Descriptor Name Lower.

* pull_data.ipynb
Important script that pulls the data from an API and extracts valuable information. 

* parsing_descriptors.ipynb 
Notebook showing the process of parsing the desc2022.xml file to extract the required attributes.

* PMAnalysis.ipynb
This notebook is our first attempt to scraping the data, but we later found an XML file. 

* post_process_descriptors.ipynb
Notebook the further process the data from parsing_descriptors.ipynb notebook to extract the root category.

* rinsepubmed.zip
A zip file for script to be run on google colab.

* root_categories.csv
Mapping of root category to full form.

* sub_categories.csv
Sub categories for root categories. No use now for this file. Just kept for the future.

* text_extraction.py
A test script whose code was incorporated into parse_data.ipynb. Also the script can be run to get a few examples from the API. 

### Files of Concern for the project
- pull_data.ipynb: This code will pull the raw data
- batch_cleaner_script.ipynb: Clean and Process the batch.
- Other files are supplementary files.

### Hosted Train and Test File on Kaggle
We have uploaded the final [train](https://www.kaggle.com/datasets/priya1506/training-batch-800-809csv) and [test](https://www.kaggle.com/datasets/priya1506/pubmedtest) file to Kaggle. 