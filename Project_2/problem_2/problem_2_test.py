import unittest
from Project_2.problem_2.problem_2 import find_files


class FindingFilesTest(unittest.TestCase):
    def setUp(self):
        # Input path and suffix
        self.__path = "."
        self.__suffix = ".c"

    def test_finding_files(self):
        arr = find_files(self.__suffix, self.__path)
        print(arr)
        self.assertListEqual(arr, ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c',
                                   './testdir/subdir1/a.c']
                             )

        # Output
        # ./ testdir / subdir3 / subsubdir1 / b.c
        # ./ testdir / t1.c
        # ./ testdir / subdir5 / a.c
        # ./ testdir / subdir1 / a.c
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
