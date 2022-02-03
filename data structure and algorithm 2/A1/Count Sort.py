# MOHAMED MOUBARAK MOHAED MISBAHOU MKOUBOI (1820705)
# Python program for CountSort implementation
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

countSortArray = [10, 59, 8, 24, 41, 34, 99]

print("Given array is: ", end="\n")
print(countSortArray)
countSortArray = countSort(countSortArray)
print("\nCount Sorted array is: ", end="\n")
print(countSortArray)