class InvalidItemError(Exception):
    """Raised when an invalid item is found."""
    pass

class PricingRuleError(Exception):
    """Raised when pricing rules are not properly defined."""
    pass
