# Problem 1:

## Description
* This project is about finding the square root of a given integer without using any existing python library
## Implementation
* I used the Binary Search algorithm approach to solve this problem. If that given number is 0 or 1 the square root will
 be the same number. However if not, I call recursive_sqrt and provide a start, and end index (Which the first time will
 be 0 and and the given number) after that the mid index. if the numerator of number divided by mid is same as mid, then
 returns mid (which is the nearest approximation to the square root of the number, given the numerator is always an integer)
 if the numerator is less than mid, recursive_sqrt is called recursively with end index been mid -1. If the numerator is
 greater than than the mid, recursive_sqrt is called recursively with start index been mid +1.
## Complexity
* The solution is "In-place", meaning that no extra data structure were created (i.e. no extra arrays were created). 
Therefore space complexity is O(1) since no auxiliary memory was used.
* The time efficiency of using the Binary Seach approach is having Best Case, Average case and Worse case as O(log n). 
Since, although I am not using auxiliary arrays, I know the order of the numbers.