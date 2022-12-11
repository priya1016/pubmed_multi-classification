The scripts for training Word2Vec + Classifiers

We use [BioWordVec](https://github.com/ncbi-nlp/BioSentVec) pretrained model as features. We process the data to remove words that are in the abstract but not in the pretrained model. Then we take the mean of the abstract words. Finally, we apply classification models (logistic regression, light gradient boost model, random forest & extra tree classifier). 

File Summary:

* Evaluating_W2Vec.ipynb: Important file walking over the training and evaluation of the classifier models.

* mean_vector_pretrained_testing.ipynb: The notebook generates the testing abstract data mean vectors.

* mean_vector_pretrained_training.ipynb: The notebook generates the training abstract data mean vectors.

* pretrained_extract_data_test.csv: The test abstract vector mapping.  Download from [Link](https://drive.google.com/file/d/1R820Ytq8Wn9vi4ZZQt3KbKiNqOloChqL/view?usp=share_link).

* pretrained_extract_data.csv: The train abstract vector mapping.  Download from [Link](https://drive.google.com/file/d/1W1fgKrdPDwgsgvkPrcC1ctf5S4wVKmtc/view?usp=sharing).

* training_and_results_w2vec.zip: Contains the raw results. 4GB file download from [here](https://drive.google.com/file/d/1sq4Fj1m7z-XwMsbmCWkl6WLInMul81J4/view?usp=share_link).

* Vector_Download.ipynb: Script to download the vectors from https://github.com/ncbi-nlp/BioSentVec.

* vector_subset.pkl: Specific to the batch data, subset of words and vector mapping. So that the search space is smaller. It is easier to lookup in a few million table than using the original BioVec model that has 4 billion words. Download from [here](https://drive.google.com/file/d/1y-DfnKJRJCmz9LZw9evgPxhsIC2P5bqD/view?usp=share_link)

* wi.pkl: BioWordVec word list. Download from [here](https://drive.google.com/file/d/1-4Fq9dlYz46myF9wA3rd_CzUEu821pEx/view?usp=sharing)
