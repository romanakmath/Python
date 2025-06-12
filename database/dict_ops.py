import itertools

import pandas as pd 
from utility.util_functions import convert_to_iso

def dict_multiassign(dict, keys, values):
    dict.update(zip(keys, values))

def getSymbolTimeframes(symbol_timeframes_dict):
    paramlist_values = list(symbol_timeframes_dict.values())
    # Convert start point dates to the right format
    paramlist_values[1] = convert_to_iso(paramlist_values[1])
    paramlist_keys = list(symbol_timeframes_dict.keys())
    symbolTimeframes = []

    for potentialParams in itertools.product(*paramlist_values):
        curr_symbol_timeframe = {
            paramlist_keys[i]: value for i, value in enumerate(potentialParams)
        }

        symbolTimeframes.append(curr_symbol_timeframe)


    return symbolTimeframes