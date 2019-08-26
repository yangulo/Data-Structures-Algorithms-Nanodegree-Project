# Problem 3:

## Description
* This problem is about rearrange the elements of an array such as to form two numbers which sum is the maximum possible.

## Implementation
* The merge sort approach was used in this problem but with a tweak, since it has to be traverse only one time. A deep 
copy of the array was created as well as two empty strings, which eventually will be populated with the array numbers.
The iteration will be fulfilled until the copy of the array has length zero. 
    * If the length of string 1 and string 2 are the same the last number of the copy of the array (which is already the 
    max value since the array is sorted) is added in string 1 and popped from the copy.
    * if the length of the string is different (having string 1 greater than string 2) then the last value of the copy of
    the array is added into string 2 and popped from the copy of the array.
    * This process continues until the copy of the array is empty. Having the two strings different by max 1 character in 
    length. And maximising its value so when they are converted into integers their sum is the highest possible. 

## Complexity
* The space complexity of this problem is O(n) since this approach is "Out-place" meaning it creates new smaller arrays and therefore
uses auxiliary memory. 
* The time complexity in this problem solution is O(n log⁡ n) given merge sort is implemented.