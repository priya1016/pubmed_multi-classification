from datasets import load_dataset
dataset = load_dataset(path="rinsepubmed", streaming=True)

x = 0
processed_data = []
for i in dataset['train']:
    data_row = {}
    if x < 1:
        medlinecitation = i.get('MedlineCitation')
        if medlinecitation:
            data_row['PMID'] = medlinecitation.get('PMID')
            data_row['DateCompleted'] = medlinecitation.get('DateCompleted')
            data_row['NumberOfReferences'] = medlinecitation.get('NumberOfReferences')
            article = medlinecitation.get('Article')
            if article:
                language = article.get('Language')
                if language != 'eng':
                    continue
                abstract = article.get('Abstract')
                if abstract:
                    data_row['AbstractText'] = abstract.get('AbstractText')
                data_row['ArticleTitle'] = article.get('ArticleTitle')
                data_row['AuthorList'] = article.get('AuthorList')
            mesh_heading_list = medlinecitation.get('MeshHeadingList')
            if mesh_heading_list:
                mesh_heading = mesh_heading_list.get('MeshHeading')
                if mesh_heading:
                    data_row['DescriptorName'] = mesh_heading.get('DescriptorName')
                    data_row['QualifierName'] = mesh_heading.get('QualifierName')
            processed_data.append(data_row)   
    else:
        break
    x+=1