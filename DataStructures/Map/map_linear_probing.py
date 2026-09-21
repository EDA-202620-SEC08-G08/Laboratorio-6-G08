from DataStructures.List import array_list as al
from DataStructures.Map import map_linear_probing as lp

def new_map(num_elements,load_factor,prime=109345121):
    capacity = int(num_elements/load_factor)
    
    table= al.new_list()
    for i in range(capacity):
        al.add_last(table, None)
    return table