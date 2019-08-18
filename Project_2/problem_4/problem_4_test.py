import unittest
from Project_2.problem_4.problem_4 import Group


class GroupTest(unittest.TestCase):
    def setUp(self):
        self.__parent = Group("parent")
        self.__child = Group("child")
        self.__sub_child = Group("subchild")

        self.sub_child_user = "sub_child_user"
        self.__sub_child.add_user(self.sub_child_user)

        self.__child.add_group(self.__sub_child)
        self.__parent.add_group(self.__child)

    def test_has_user(self):
        self.assertTrue(self.__parent.is_user_in_group(self.sub_child_user, self.__parent))
        # Add user
        child_user = "Yadira"
        self.__child.add_user(child_user)
        self.assertTrue(self.__parent.is_user_in_group(child_user, self.__parent))
        self.assertTrue(self.__child.is_user_in_group(child_user, self.__child))

        # Print True is user exists in folder
        print(self.__parent.is_user_in_group(child_user, self.__parent))
        print(self.__child.is_user_in_group(child_user, self.__child))

    def test_has_no_user(self):
        self.assertFalse(self.__parent.is_user_in_group("Edgar", self.__parent))

        # Print False if user does not exist in folder
        print(self.__parent.is_user_in_group("Edgar", self.__parent))

    def test_user_is_none(self):
        self.assertFalse(self.__parent.is_user_in_group(None, self.__parent))

        # Print False if user is None
        print(self.__parent.is_user_in_group(None, self.__parent))
        print(self.__parent.is_user_in_group(None, self.__child))


if __name__ == '__main__':
    unittest.main()
