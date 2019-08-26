# Problem 7:

## Description
* This exercise implements an "HTTPRouter" like any typical web server uses with a Trie data structure implementation. The 
purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure 
out what content to return.

## Implementation
* The solution is very similar to the solution of problem_6. However in this problem solution implements a Trie data structure 
which contains a handler for a given url or path. Such path is search within the Trie and returns its proper handler. 
    * If the provided path has no handler an error handler is returned.

## Complexity
* Same as mentioned in problem_6, the space complexity will be O(MN) which approximates to O(n)
* The time complexity of adding a handler is O(n). In which (n) is the path length. The path's length is based on how many
 ("/") where found. Looking up a path has similar complexity of O(N) is which (n) is the number ("/") found.