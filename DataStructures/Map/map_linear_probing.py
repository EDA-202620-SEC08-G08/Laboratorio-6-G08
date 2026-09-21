from DataStructures.List import array_list as al
from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
import random 

def new_map(num_elements,load_factor,prime=109345121):
    capacity = mf.next_prime(int(num_elements/load_factor))
    
    table= al.new_list()
    for i in range(capacity):
        al.add_last(table,me.new_map_entry(None,None))
        
    my_table = {
        "prime": prime,
        "capacity": capacity,
        "scale":random.randint(1,prime-1),
        "shift":random.randint(0,prime-1),
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
        }
    return my_table

def is_available(table, pos):
    entry = al.get_element(table, pos)
    return me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__"

def default_compare(key, entry):
    entry_key = me.get_key(entry)
    if key == entry_key:
        return 0
    elif key > entry_key:
        return 1
    return -1

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail
