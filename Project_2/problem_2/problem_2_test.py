import unittest
from Project_2.problem_2.problem_2 import find_files


class FindingFilesTest(unittest.TestCase):
    def setUp(self):
        # Input path and suffix
        self.__path = "/Users/yangulo/Desktop/Udacity_Project2/testdir"
        self.__suffix = ".c"

    def test_finding_files(self):
        arr = find_files(self.__suffix, self.__path)
        self.assertListEqual(arr, [
            '/Users/yangulo/Desktop/Udacity_Project2/testdir/subdir3/subsubdir1/b.c',
            '/Users/yangulo/Desktop/Udacity_Project2/testdir/t1.c',
            '/Users/yangulo/Desktop/Udacity_Project2/testdir/subdir5/a.c',
            '/Users/yangulo/Desktop/Udacity_Project2/testdir/subdir1/a.c'
        ])

        # Output
        # '/Users/yangulo/Desktop/Udacity_Project2/testdir/subdir3/subsubdir1/b.c',
        # '/Users/yangulo/Desktop/Udacity_Project2/testdir/t1.c',
        # '/Users/yangulo/Desktop/Udacity_Project2/testdir/subdir5/a.c',
        # '/Users/yangulo/Desktop/Udacity_Project2/testdir/subdir1/a.c'
        for element in arr:
            print(element)

    def test_finding_files_no_suffix(self):
        suffix = ".yad"
        arr = find_files(suffix, self.__path)
        # Print -1 no suffix found
        self.assertEqual(arr, -1)
        print(arr)

    def test_finding_files_no_path(self):
        suffix = ".a"
        path = ""
        arr = find_files(suffix, path)
        # Print -1 no path found
        self.assertEqual(arr, -1)
        print(arr)


if __name__ == '__main__':
    unittest.main()
