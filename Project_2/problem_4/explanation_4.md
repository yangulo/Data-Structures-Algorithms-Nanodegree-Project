## Problem 4

* **is_user_in_group Implementation:**
    * The is_user_in_group Each Group object has two arrays. Users array and groups array. Given a user name the users 
    array is iterated searching for that user. If the user not in that array then the groups array is iterated. 
    Each element of the groups array is a Group object therefore a recursive call is implemented to traverse all nested 
    groups arrays, given each Group object. This is done until the user name is found and returns "True". If not found 
    returns "False"
* **Time and Space Efficiency:** 
    * As mentioned in explanation_2.md, array space complexity is O(n) since an array organizes and saves items next to 
    each other in memory. Therefore the more elements in an array the bigger space in memory associated to it.
    * Time efficiency for searching and appending  is O(1) since each item has an index given its position at the array.
     An as mention before, inserting and deleting time complexity is O(n). This problem constructs a hierarchy using 
     two arrays (One which some elements are nested arrays as well). Since the position of the elements been search is 
     unknown  searching an element within the array will take O(n). A recursive call is made within the for. The time 
     efficiency is O(n)
    * Solution Improvement: A way to improve this solution is to implement a Has Map. It will take O(n) to populate the 
    Has Map the first time all elements are been iterated and added, but assuming the group does not change the 
    searching time on following searches will be constant O(1)