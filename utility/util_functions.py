import datetime as dt

def dict_multiassign(dict, keys, values):
    dict.update(zip(keys, values))

def dict_from_kv(dict, keys, values):
    dict = {}
    dict.update(zip(keys, values))

def getDictValues(dict):
    dict_values = dict.values()
    return dict_values

def convert_to_iso(start_point_list):
    iso_date_list = []
    for d in start_point_list:
        d = dt.datetime.strptime(d, "%Y-%m-%d")
        d = d.isoformat()
        iso_date_list.append(d)
    return iso_date_list