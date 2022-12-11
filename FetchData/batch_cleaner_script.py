import glob
import ast
import pandas as pd
import numpy as np
from pathlib import Path
from tqdm import tqdm

class BatchProcessor:
    '''
    Script to Batch Process the intermediate raw data
    '''
    def __init__(
        self, 
        processed_directory_path: str = 'raw_batch_data'
        '/processed_batch_*.csv',
        output_directory: str = 'training_data',
        recompute: bool = False,
        descriptor_filepath: str = 'descriptor_mapper.csv'
        ):
        '''
        Initialize the BatchProcessor Class

        Parameters:
            1. processed_directory_path [str]
            Preprocessed data directory.

            2. output_directory [str]
            The output directory path to store the processed
            results.

            3. recompute [bool]
            Set to true to recompute the processed batch.

            4. descriptor_filepath [str]
            The descriptor file path.
        '''
        self.processed_files_list = glob.glob(processed_directory_path)
        self.output_directory = output_directory
        Path(f'./{output_directory}').mkdir(parents=True, exist_ok=True)
        self.recompute = recompute
        self.dn = pd.read_csv(descriptor_filepath)
        self.dn['Root Category'] = self.dn['Root Category'].apply(ast.literal_eval)



    def process_batch(self):
        '''
        Process the processed batch data.
        '''
        for file_name in tqdm(self.processed_files_list):
            batch_number = '_'.join(file_name.split('_')[-2:])
            path = Path(f'training_data/training_batch_{batch_number}')
            if (not path.is_file()) or (self.recompute):
                data = pd.read_csv(file_name)
                data['DescriptorName'] = data['DescriptorName']\
                    .apply(ast.literal_eval)
                data_large = data.explode('DescriptorName')
                data_large = data_large[
                    ~data_large['DescriptorName']
                    .isna()]
                data_merged = data_large.merge(
                    self.dn, 
                    left_on='DescriptorName', 
                    right_on='Descriptor Name', 
                    how='inner')
                
                root_data = data_merged\
                    .groupby('PMID')['Root Category']\
                    .apply(list)\
                    .apply(np.array, dtype='object')\
                    .apply(lambda x: set(''.join(x.flatten())))\
                    .to_frame()\
                    .reset_index()\
                    .explode('Root Category')
                root_data['Values'] = 1
                finish_data = pd.pivot_table(
                    root_data, 
                    values='Values', 
                    index='PMID', 
                    columns='Root Category', 
                    fill_value=0)
                meta_data = data_merged[
                    [
                    'PMID', 
                    'date_completed', 
                    'NumberOfReferences', 
                    'AbstractText', 
                    'ArticleTitle', 
                    'AuthorList'
                    ]]\
                    .drop_duplicates()
                final_data = meta_data.merge(
                    finish_data, 
                    on='PMID', 
                    how='inner')
                final_data = final_data[
                    ~final_data['AbstractText']
                    .isna()]
                final_data.to_csv(
                    f'./training_data/training_batch_{batch_number}',
                     index=False)
            else:
                print(f'File {file_name} already '
                'in file. Set recompute to True '
                'to preprocess again.')

    def main(self):
        self.process_batch()

if __name__ == '__main__':

    bp = BatchProcessor()
    bp.main()
                
                