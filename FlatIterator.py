class FlatIterator:

    def __init__(self, list_of_list):
        self.list_ = list_of_list

    def __iter__(self):
        self.item = -1
        return self
    
    def _flatten_list(self, list_):
        flat_list = []
        for item in list_:
            if isinstance(item, list):
                flat_list.extend(self._flatten_list(item))
            else:
                flat_list.append(item)
        return flat_list

    def __next__(self):
        self.item += 1
        self.flat_list = self._flatten_list(self.list_)
        if self.item == len(self.flat_list):
            raise StopIteration
        return self.flat_list[self.item]

            
    
