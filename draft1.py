import datetime
def comp(list1,list2):
    if len(list1) != len(list2):
        return False
    else:
        for i in range(len(list1)):
            if list1[i] != list2[i]:    
                return False
        return True
a = [1,2,3,4,5]
b = [1,2,3,4,5]
start = datetime.datetime.now()
print(comp(a,b))
end = datetime.datetime.now()
print(end-start)
