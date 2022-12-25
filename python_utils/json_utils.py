import json
import pandas
from pathlib import Path

#return dictionary from file with json.loads
def read_file(fpath:Path):
    dictionary = {}
    with open(str(fpath), 'r') as fin:
        dictionary = json.loads(fin.read())
    return dictionary

#return dictionary with keys containing sub dictionaries removed and the key/value pairs from sub dicts on the top level (1 deep)
def flatten_dict(dictionary):
    flattened = {}
    for key, value in dictionary.items():
        if isinstance(value, dict):
            flattened.update(value)
        elif isinstance(value, list):
            flattened[key] = json.dumps(value)
        else:
            flattened[key] = value
    return flattened
   

# def to_csv():
    
    # for i in range(len(df)):
    #     df['system.rules'][i] = encode_rules(df, i)
        

# def encode_rules(df, idx):
#     return json.dumps(df['system.rules'][idx])

def decode_rules(df, idx):
    return json.loads(df['system.rules'][idx])

def get_distinct_rules(df):
    
    


# extract_rules(flattened_dict['rules'])
#Expand a list item into the dictionary if possible
# def expand_list(dictionary, list_key):

#     return
   

def main():
    fpath = Path('/home/toast/Documents/python_utils/test.json')
    data = read_file(fpath=fpath)
    print('unnormalized:\n', data)
    data_normalized = pandas.json_normalize(data)
    print('normalized:\n', data_normalized)

if __name__ == '__main__':
    main()


