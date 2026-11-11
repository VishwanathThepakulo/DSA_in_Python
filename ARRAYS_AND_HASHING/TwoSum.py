Array = [3,2,4]
Target = 6
def twoSum(Array, Target):
    mydict = {}
    for i in range(len(Array)):
        element = Target - Array[i]
        if element in mydict:
            return [mydict[element], i]
        mydict[Array[i]]=i
print(twoSum(Array, Target))

























