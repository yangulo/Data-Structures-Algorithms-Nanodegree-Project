# Problem 2:

## Description
* Find the index of a given value withing a sorted array rotated at some random pivot.

## Implementation
* Given a sorted array which is rotated at some random pivot point. You are given a target value to search. If it is found
 in the array, then its index is returned, otherwise it returns -1. Since the array has been rotated the Binary Search 
 approach has to be modified to be able to find a value within the right and left areas of searching. The function 
 recursive_rotated_array_search is called with parameters: array, target, start (which is 0 teh first time), and end (
 which is the length of the array -1). Then, mid is calculated and its value is compared with the target. if it is the same
 the mid index is return. Otherwise, if the value of mid is greater or smaller than the target the regular conditions of
 binary search are applied but with this modification:
    * if mid value is smaller than the target: 
        * Then the value of end index is compared to the mid value (with this I mean array[mid_index]) if this is grater
         (Which it should if the array is ordered) then the value of the end index is also compared with the target value. 
         If greater or equal then recursive_rotated_array_search is called recursively with array, target start index as 
         the mid index + 1 and end index.
        * Else, recursive_rotated_array_search is called recursively with array, target start index and end index as 
        the mid index - 1.
    * if mid value is greater than the target:
        * Then the value of start index is compared to the mid value if this is smaller
         (Which it should if the array is ordered) then the value of the start index is also compared with the target value. 
         If smaller or equal then recursive_rotated_array_search is called recursively with array, target start index and
          end index as the mid index - 1.
         * Else, recursive_rotated_array_search is called recursively with array, target start index as mid index + 1 and 
         end index.

## Complexity
* This solution is "In-Place" meaning that no extra data structure was created. (i.e no auxiliary memory was used). Therefore
the space complexity is constant O(1).
* Time efficiency: The time complexity of this problem is O(log N). Since by using the binary search approach the length 
of (N) is reduced by half on every recursive call until the element is found or the are no more elements on the array.