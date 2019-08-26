# Problem 6:

## Description
* In this problem the smallest and largest integer from a list of unsorted integers has to be returned.

## Implementation
* For this problem solution there are two variables "max" and "min" which will saved the max and min values accordingly.
 These variables are initialized with the same value at the beginning, which is the first value at index 0 of the array. 
 The array is then traversed starting at the second element which is at index 1 until the last element of the array. 
 Each iteration compares the max value with the current, and if the max value is smaller than the current, then the max element 
 becomes the current element. This is also applied in order to calculate the array's min element.

## Complexity
* The space complexity is constant. Since only two variables to saved max and min values where created and not additionally 
data structures, such as array, tries and so on are created. Also the memory of these variables is very small so space 
efficiency is O(1).
* The time complexity is O(N) with a single traversal run of the array is performed while finding the max and min values 
on this giving array.