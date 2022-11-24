def merge(dict1,dict2):
    return (dict1.update(dict2))
dict1={'a':10,'b':8} ;print("First dictionary is:",dict1)

dict2={'d':6,'c':4} ; print("second dictionary is",dict2)

merge(dict1,dict2)
print("Merged dictionary is:",dict1)
