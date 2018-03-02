tab=[1,2,3,4,5,6,7,8,9,10,24,25,40,36,230]
lookingNumber=1

def SorcBin(inputTab,lookingNumber):
    left=0
    right=len(inputTab)
    index=-1
    while (left<right):
        mid=round((left+right)/2)
        
        if(inputTab[mid]<lookingNumber):
            left=mid+1
        else:
            right=mid
        if(inputTab[left]==lookingNumber):
            index= left
        else:
            index= -2
    return index

print("Index poszukiwanej liczby: ",lookingNumber," to :",SorcBin(tab,lookingNumber))
  