import unittest
from HW_14.Employe import User


class TestUser(unittest.TestCase):
    def test_init_valid_values(self):
        user = User("John", 12345, 5)
        self.assertEqual(user.name, "John")
        self.assertEqual(user.the_id, 12345)
        self.assertEqual(user.level, 5)

    def test_init_invalid_name(self):
        with self.assertRaises(ValueError):
            User(123, 12345, 5)

    def test_init_invalid_id(self):
        with self.assertRaises(ValueError):
            User("John", -12345, 5)

    def test_init_invalid_level(self):
        with self.assertRaises(ValueError):
            User("John", 12345, 8)


if __name__ == "__main__":
    unittest.main()