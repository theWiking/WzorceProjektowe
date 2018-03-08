import copy
import math
tab=[1,5,7,12,20,25,30]
lookingNumber=8


def SorcBin(inputTab,lookingNumber):
    left=0
    right=len(inputTab)
    index=-1
    while (left<right):
        mid=copy.deepcopy(math.floor((left+right)/2))  #here was bug not round but math.floor
        print("Left: ",left," right ", right, " mid idex (from 0):", mid)
        if(inputTab[mid]<lookingNumber):
            left=copy.deepcopy(mid+1)
        else:
            right=copy.deepcopy(mid)
        
        if(inputTab[left]==lookingNumber):
            index= copy.deepcopy(left)
            print ("test")
            break
        else:
            index= -2
        
        
    return index

print("Index (od 0) poszukiwanej liczby: ",lookingNumber," to :",SorcBin(tab,lookingNumber))
  