import unittest
from datetime import date
from fiscalmind.reconciliation import Entry, suggest


class SuggestionTests(unittest.TestCase):
    def setUp(self):
        self.document = Entry("empresa-a", "nota-1", 10500, date(2026, 1, 10))

    def test_exact_amount_and_dates_produce_explained_suggestions(self):
        matches = suggest(self.document, [Entry("empresa-a", "t2", 10500, date(2026, 1, 17)), Entry("empresa-a", "t1", 10500, date(2026, 1, 10))])
        self.assertEqual([s.transaction_id for s in matches], ["t1", "t2"])
        self.assertIn("7 dia(s)", matches[1].reason)

    def test_rejects_wrong_company_amount_and_date(self):
        transactions = [Entry("empresa-b", "other", 10500, date(2026, 1, 10)), Entry("empresa-a", "amount", 10501, date(2026, 1, 10)), Entry("empresa-a", "late", 10500, date(2026, 1, 18))]
        self.assertEqual(suggest(self.document, transactions), [])

    def test_ambiguous_matches_remain_multiple_suggestions(self):
        transactions = [Entry("empresa-a", "a", 10500, date(2026, 1, 10)), Entry("empresa-a", "b", 10500, date(2026, 1, 10))]
        self.assertEqual(len(suggest(self.document, transactions)), 2)

    def test_invalid_amount_and_window(self):
        for value in (0, -1, 100.0, True):
            with self.subTest(value=value), self.assertRaises(ValueError):
                Entry("a", "x", value, date(2026, 1, 1))
        with self.assertRaises(ValueError):
            suggest(self.document, [], -1)


if __name__ == "__main__":
    unittest.main()
