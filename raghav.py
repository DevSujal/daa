import pandas
import math

def divide(arr,si,ei):
    if(si >= ei):
        return
    mid= (si + ei) // 2
    divide(arr,si,mid)
    divide(arr,mid+1,ei)
    conquer(arr,si,mid,ei)
    
def conquer(arr,si,mid,ei):
    merged=list()
    indx1=si
    indx2=mid+1
    while(indx1<=mid and indx2<=ei):
        if(arr[indx1]<=arr[indx2]):
            merged.append(arr[indx1])
            indx1=indx1+1
        else:
            merged.append(arr[indx2])
            indx2=indx2+1
    while(indx1<=mid):
        merged.append(arr[indx1])
        indx1=indx1+1
    while(indx2<=ei):
        merged.append(arr[indx2])
        indx2=indx2+1
    arr[si : ei + 1] = merged

data = pandas.read_csv("data.csv")
data = list(data["numbers"])

divide(data, 0, len(data) - 1)
print(data)