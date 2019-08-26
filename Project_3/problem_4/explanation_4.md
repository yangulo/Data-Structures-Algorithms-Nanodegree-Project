# Problem 4:

## Description
* Given an input array consisting on only 0, 1, and 2. The array needs to be sorted in a single traversal. Within this problem 
any sorting function that Python provides can not be used.

## Implementation
* Within this problem solution a single traversal is done within an array by using a left pointer. Another right pointer is
used so that the array is been traversed both ways from the end to the beginning and from current to end based on the direction
of (i). The flag (current) determines which element is being sorted. The left flag only advances if the current position is equal 
to current, and the right flag always advances at the end of the loop. If the left element is greater to the right element 
then these two element are swapped. If the the left and right cross direction, the right pointer is changed. so that the 
solution of this problem works.

## Complexity
* The space complexity is O(1) since no auxiliary memory was used.
* The time complexity is O(N) since, there is only a single traversal array of (N) elements.