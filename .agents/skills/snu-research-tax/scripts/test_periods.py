import unittest
from periods import fiscal_year, cutoff_check

class TestPeriods(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(fiscal_year(2026)["end"], "2027-02-28")

    def test_leap_year(self):
        self.assertEqual(fiscal_year(2027)["end"], "2028-02-29")

    def test_pre_sunset(self):
        self.assertTrue(fiscal_year(2027)["within_published_sunset_by_date_only"])

    def test_post_sunset(self):
        self.assertFalse(fiscal_year(2028)["within_published_sunset_by_date_only"])

    def test_sunset_inclusive(self):
        self.assertTrue(cutoff_check("2028-12-31")["within_published_sunset_by_date_only"])

    def test_one_day_later(self):
        self.assertFalse(cutoff_check("2029-01-01")["within_published_sunset_by_date_only"])

    def test_invalid_day(self):
        with self.assertRaises(ValueError):
            cutoff_check("2028-02-30")

    def test_invalid_year(self):
        with self.assertRaises(ValueError):
            fiscal_year(9999)

    def test_bool_rejected(self):
        with self.assertRaises(ValueError):
            fiscal_year(True)

if __name__ == "__main__":
    unittest.main()
