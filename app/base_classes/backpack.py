class BackPack:
    '''
    A class which represents a BackPack

    ...

    Attributes
    ----------
    _backpack : []
        a list of backpack items

    Methods
    -------
    sort()
        Sorts the backpack items
    count()
        Returns how many backpack items there are
    list()
        Returns the backpack list of items
    add(item)
        Adds an item to the backpack list
    remove(item)
        Removes an item from the backpack list
    in_backpack(item)
        Checks if an item is in the backpack
    '''
    
    def __init__(self, items = None):
        self._backpack = []
        if items is None:
            items = []
        if type(items) is not "<class 'list'>":
            items = []
        for item in items:
            self._backpack.append(item)

    def sort(self):
        '''Sorts the backpack items'''
        self._backpack.sort()

    def count(self):
        '''
        Returns how many backpack items there are

        Returns
        ----------
        int : Number of items in backpack
        '''
        return self._backpack.count()

    def list(self):
        '''
        Returns the backpack list of items

        Returns
        ----------
        [] : Returns backpack items as a list
        '''
        return self._backpack[:]

    def add(self, item):
        '''Adds an item to the backpack list'''
        if item is not None:
            self._backpack.append(item)

    def remove(self, item):
        '''Removes an item from the backpack list'''
        self._backpack.remove(item)

    def in_backpack(self, item):
        '''
        Checks if an item is in the backpack
        
        Returns
        ----------
        int : Returns item index number in list or -1 if no item found
        '''
        low = 0
        high = len(self._backpack) - 1
        mid = 0
    
        while low <= high:
            
            mid = (high + low) // 2

            if self._backpack[mid] < item:
                low = mid + 1

            elif self._backpack[mid] > item:
                high = mid - 1

            else:
                return mid
        return -1
    