## Problem 6

* **Union and Intersection of Two Linked Lists Implementation:**
    * Union and intersection are implemented using a linked list. Since the double linked list class created on 
    problem 1 was made as iterable by using **(__iter__)**, this linked list can be iterated so all elements can be compared 
    on either union or intersection functions. An array can be also used on this problem to store the joined two 
    linked lists or the intersection values. However, due to it flexible storage in memory I decided to used same 
    linked list class created on problem one.
    * **Time and Space Efficiency:**
    * As mentioned before, searching, inserting and deleting time efficiency is O(n) on a linked list but pre-append 
    (at the top) and append (at the tail) are fast operations with constant time O(1). On this problem an empty 
    linked list is created to storage (appending at the tail) each element by joining two linked lists or by selecting 
    only the duplicate values in two linked lists (intersection) with appending constant time. Each function has 
    two "for" making searching (iterating) time efficiency 2 O(n) but since 2 is a constant and constants are 
    dropped off, the time efficiency of union and intersection linked lists is O(n).