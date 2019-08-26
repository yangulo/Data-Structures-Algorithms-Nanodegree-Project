import unittest
from Project_3.problem_7.problem_7 import Router


class RouterTest(unittest.TestCase):
    def setUp(self):
        self.root_handler = "root handler"
        self.error_handler = "not found handler"
        self.router = Router(self.root_handler, self.error_handler)
        self.router.add_handler("/home/about", "about handler")
        self.router.add_handler("/home/user/tmp/media", "user tmp media handler")

    def test_root_handler(self):
        self.assertEqual(self.router.lookup("/"), self.root_handler)
        print(self.router.lookup("/"))  # Prints root handler

    def test_home_handler_not_found_handler(self):
        self.assertEqual(self.router.lookup("/home"), self.error_handler)
        print(self.router.lookup("/home"))  # Prints not found handler

    def test_home_about_handler(self):
        self.assertEqual(self.router.lookup("/home/about"), "about handler")
        print(self.router.lookup("/home/about"))  # Prints about handler

    def test_home_about_handler_slash(self):
        self.assertEqual(self.router.lookup("/home/about/"), "about handler")
        print(self.router.lookup("/home/about/"))  # Prints about handler

    def test_home_about_handler_not_found(self):
        self.assertEqual(self.router.lookup("/home/about/something"), self.error_handler)
        print(self.router.lookup("/home/about/something"))  # Prints not found handler

    def test_home_multiple_path_handler(self):
        self.assertEqual(self.router.lookup("/home/user/tmp/media"), "user tmp media handler")
        self.assertEqual(self.router.lookup("/home/user/tmp/media/"), "user tmp media handler")

        print(self.router.lookup("/home/user/tmp/media"))  # Prints user tmp media handler
        print(self.router.lookup("/home/user/tmp/media/"))  # Prints user tmp media handler

    def test_none(self):
        self.assertIsNone(self.router.lookup(None))
        print(self.router.lookup(None))  # Prints None

if __name__ == '__main__':
    unittest.main()
