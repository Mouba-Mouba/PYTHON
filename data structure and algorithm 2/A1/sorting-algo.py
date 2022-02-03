def mergeSort(myArray):
    if len(myArray) > 1:
        middleIndex = len(myArray)//2
  
        firstHalf = myArray[:middleIndex]
        secondHalf = myArray[middleIndex:] 
        mergeSort(firstHalf)
        mergeSort(secondHalf)

        i = 0
        j = 0
        k = 0  
  
        while i < len(firstHalf) and j < len(secondHalf):
            if firstHalf[i] < secondHalf[j]:
                myArray[k] = firstHalf[i]
                i += 1
            else:
                myArray[k] = secondHalf[j]
                j += 1
            k += 1
  
        while i < len(firstHalf):
            myArray[k] = firstHalf[i]
            i += 1
            k += 1
  
        while j < len(secondHalf):
            myArray[k] = secondHalf[j]
            j += 1
            k += 1

def countSort(myArray):
    largestElement = int(max(myArray))
    smallestElement = int(min(myArray))
    elementRange = largestElement - smallestElement + 1
    countArray = [0] * elementRange
    displayArray = [0] * len(myArray)
    
    # count occurange of each element
    for i in range(0, len(myArray)):
        countArray[myArray[i]-smallestElement] += 1

    # Adding two elements
    for i in range(1, len(countArray)):
        countArray[i] += countArray[i-1]

    # Assign each element to correct index
    for i in range(len(myArray)-1, -1, -1):
        displayArray[countArray[myArray[i] - smallestElement] - 1] = myArray[i]
        countArray[myArray[i] - smallestElement] -= 1

    return displayArray

mergeSortArray = [10, 59, 8, 24, 41, 34, 99]
countSortArray = [10, 59, 8, 24, 41, 34, 99]

print("Before Merge Sort: ")
print(mergeSortArray)
mergeSort(mergeSortArray)
print("After Merge Sort: ")
print(mergeSortArray)

print("Before Count Sort: ")
print(countSortArray)
countSortArray = countSort(countSortArray)
print("After Count Sort: ")
print(countSortArray)
