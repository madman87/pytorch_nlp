import torch
import json

#handling text data
from torchtext.legacy import data 


# with open("/Users/macbook/Desktop/ML_NLP_PROJECT/paragraphs.json","r") as f:
#     for line in f:
#         jsn = json.loads(line)
#         paragraph = jsn['body']
#         words = jsn['words']

#Reproducing same results
SEED = 2019
#Torch
torch.manual_seed(SEED)

#Cuda algorithms
torch.backends.cudnn.deterministic = True 

TEXT = data.Field(tokenize='spacy',batch_first=True,include_lengths=True)
LABEL = data.LabelField(dtype = torch.float,batch_first=True)
fields = [(None, None), ('text',TEXT),('label', LABEL)]

     
training_data=data.TabularDataset(path = '/Users/macbook/Desktop/ML_NLP_PROJECT/paragraphs.json',format = 'json',fields = fields,skip_header = True)
#print preprocessed text
print(vars(training_data.examples[0]))  

import random
train_data, valid_data = training_data.split(split_ratio=0.7, random_state = random.seed(SEED))

        