from .exceptions import PricingRuleError, InvalidItemError


def calculate_total(items: str, pricing_rules) -> int:
    total = 0
    item_counts = {}

    # Calculate total price directly while counting items
    for item in items:
        if item not in pricing_rules:
            raise InvalidItemError(f"Invalid item found: {item}")

        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1

        count = item_counts[item]
        item_rule = pricing_rules.get(item, {})
        price = item_rule.get('price')

        if price is None:
            raise PricingRuleError(f"Pricing rule missing 'price' for item: {item}")

        if 'discount_quantity' in pricing_rules[item]:
            discount_quantity = pricing_rules[item].get('discount_quantity')
            discount_price = pricing_rules[item].get('discount_price')

            if discount_quantity is None or discount_price is None:
                raise PricingRuleError(f"Invalid discount rules for item: {item}")

            if count % discount_quantity == 0:
                # Apply the discount for the current set of items
                total += discount_price - (discount_quantity - 1) * price
            else:
                total += price
        else:
            total += price

    return total
