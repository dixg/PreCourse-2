# Python program for implementation of MergeSort 
from email.errors import MessageError
from heapq import merge


def mergeSort(arr):
  if len(arr)>1:
    mid=len(arr)//2
    L=arr[:mid]
    print("L=",L)
    R=arr[mid:]
    print("R=", R)  
    mergeSort(L)
    mergeSort(R)
    i=0
    j=0
    k=0
    while i<len(L) and j< len(R):
      if L[i]<R[j]:
        arr[k]=L[i]
        i+=1
      else:
        arr[k]=R[j]
        j+=1
      k+=1
    
    while i< len(L):
      arr[k]=L[i]
      i+=1
      k+=1
      
    while j<len(R):
      arr[k]=R[j]
      j+=1
      k+=1
  #write your code here
  
# Code to print the list 
def printList(arr): 
  for i in range(len(arr)):
    print(arr[i])
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
