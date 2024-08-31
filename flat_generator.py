def flat_generator(list_of_lists):
    item = -1   
    flat_list = flatten_list(list_of_lists) 
    for _ in range(len(flat_list)):
        item += 1
        yield flat_list[item]

def flatten_list(list_):
    flat_list = []
    for item in list_:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list    

    