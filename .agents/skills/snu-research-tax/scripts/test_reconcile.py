import unittest
from reconcile import reconcile


class TestReconcile(unittest.TestCase):
    def test_example(self):
        self.assertEqual(reconcile(200000, 16000, 1600)["net_won"], 182400)

    def test_zero(self):
        self.assertEqual(reconcile(125000, 0, 0)["net_won"], 125000)

    def test_all_withheld(self):
        self.assertEqual(reconcile(100, 90, 10)["net_won"], 0)

    def test_excess(self):
        with self.assertRaises(ValueError):
            reconcile(100, 100, 1)

    def test_negative(self):
        with self.assertRaises(ValueError):
            reconcile(100, -1, 0)

    def test_non_integer(self):
        with self.assertRaises(ValueError):
            reconcile(100.0, 1, 0)

    def test_boolean(self):
        with self.assertRaises(ValueError):
            reconcile(True, 1, 0)


if __name__ == "__main__":
    unittest.main()
