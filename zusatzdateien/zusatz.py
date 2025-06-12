def substract_keys(d, keys):
    return {k: d[k] for k in d.keys() - keys}

def print_val(d):
    for p in d:
        print (d[p]) 

def print_key(d):
    for key in d:
        print (key) 

def add_keys(d, adddict):
    return{**d, **adddict}

def bulkInsert(collect_id, STs_strategy_df):
    for row in STs_strategy_df.itertuples():
        rowDict = row._asdict()
        rowDict = substract_keys(rowDict, {"Index"})