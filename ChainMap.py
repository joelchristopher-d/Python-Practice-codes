from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Create ChainMap
chain = ChainMap(dict1, dict2)

print(chain['b'])  
print(chain['c'])  
print(type(chain))
