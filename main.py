# this  function prints true, if string a can be mmapped to string b or else it prints false
def mapping(a, b):
    # if strings do not have same length mapping is not possible
    if len(a) != len(b):
        print("false")
        return
    for i in range(0,len(a)):
        if a[i] not in Dict:
            Dict.update({a[i] : b[i]})  
        elif ( Dict.get(a[i]) != b[i]):  
            print("false")
            return
    print("true")
