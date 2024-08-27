from django.test import TestCase
from .utils import calculate_total
from .exceptions import InvalidItemError
from .pricing import PRICING_RULES

class CalculateTotalTestCase(TestCase):
    def setUp(self):
        # Pricing rules for testing
        self.pricing_rules = PRICING_RULES

    def test_empty_items(self):
        """Test total calculation for empty string input."""
        self.assertEqual(calculate_total("", self.pricing_rules), 0)

    def test_single_item(self):
        """Test total calculation for a single item."""
        self.assertEqual(calculate_total("A", self.pricing_rules), 50)

    def test_multiple_items_no_discount(self):
        """Test total calculation for multiple items with no applicable discount."""
        self.assertEqual(calculate_total("AB", self.pricing_rules), 80)

    def test_items_with_discount(self):
        """Test total calculation for items where discounts apply."""
        self.assertEqual(calculate_total("AAAB", self.pricing_rules), 160)

    def test_items_with_combined_discount(self):
        """Test total calculation for items where combined discounts apply."""
        self.assertEqual(calculate_total("AAABB", self.pricing_rules), 175)
        self.assertEqual(calculate_total("AAABBD", self.pricing_rules), 190)
        self.assertEqual(calculate_total("DABABA", self.pricing_rules), 190)

    def test_multiple_same_items(self):
        """Test total calculation for multiple identical items with and without discount."""
        self.assertEqual(calculate_total("AA", self.pricing_rules), 100)
        self.assertEqual(calculate_total("AAA", self.pricing_rules), 130)
        self.assertEqual(calculate_total("AAAA", self.pricing_rules), 180)
        self.assertEqual(calculate_total("AAAAA", self.pricing_rules), 230)
        self.assertEqual(calculate_total("AAAAAA", self.pricing_rules), 260)

    def test_invalid_item(self):
        """Test calculation with an invalid item that should raise an exception."""
        with self.assertRaises(InvalidItemError):
            calculate_total("Z", self.pricing_rules)
