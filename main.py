
# Module sys for importing arguement
import sys   
a = sys.argv[1]
b = sys.argv[2]

# this  function prints true, if string a can be mmapped to string b or else it prints false
# Precondition: mapping has two arguements
def mapping(a, b):
    # if a has a smaller length, mapping of all character of a is not possible
    if len(a) > len(b):
        print("false")
        return
    Dict = {}
    for i in range(0,len(a)):
        if a[i] not in Dict:
            Dict.update({a[i] : b[i]})  
        elif ( Dict.get(a[i]) != b[i]):  
            print("false")
            return
    print("true")
    
# calling the function using the aruguements    
mapping(a,b)
