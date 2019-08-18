## Problem 2

* **File Recursion Implementation:** 
    * The find_files function will iterate through an array of elements (files and directories (Where directories will 
    be considered as nested arrays)) in order to find all files ending with certain suffix. The os.listdir(path) returns
     an array of elements in a directory. That array is iterated and each element evaluated (whether it is a file or a 
     directory). If the element is a file, then the suffix is checked. If that suffix is the one been searched for, the 
     path is saved into a new array. If the element is not a file ending with that suffix, then it is skipped. If the 
     element is a directory, find_files is called recursively and continues until no elements are left in the array.
* **Time and Space Efficiency:** 
    * Array space complexity is O(n). An array organizes items sequentially, all items are saved next to each other in 
    memory. Arrays are fixed size, so size needs to be specified (Unless using dynamic arrays "Array lists") 
    * Array time efficiency is O(1) for searching and appending  since each position at the array has an index. However,
     inserting and deleting is O(n). Inserting an element into an array, needs to make space by "scooting over" 
     everything starting at the index where the element has to be inserted into. Worse case scenario will be inserted 
     at index 0, moving everything at the array (O(n)).  Same applies for deleting an element. So when an element is 
     removed, the gap has to be filled by "scooting over" all the elements that were after it.
    * Given the nature of this problem an array and linked list will have fit the solution similarly. Searching time in 
    linked list is O(n) and searching time in an array is O(1) when the index of the element is know. Since the position
     of the elements been search is unknown using both data structures will have to traverse the all elements in the 
     worse case. However, an array was chosen over a linked list because it is easier to iterate. Finally the recursive 
     function will be called n times so its time efficiency is O(n*m) where m is the number of sub folders for each 
     folder, which will result in O(n)