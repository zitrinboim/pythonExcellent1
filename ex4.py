def get_recipe_price(prices, optionals=None, **ingredients):
    total_price = 0
    for ingredient, amount in ingredients.items():
        if ingredient in prices:
            total_price += prices[ingredient] * amount / 100
    if optionals:
        for optional in optionals:
            if optional in prices:
                total_price -= prices[optional] * ingredients.get(optional, 0) / 100
    return round(total_price, 2)