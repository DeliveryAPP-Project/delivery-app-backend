from typing import List


def calculate_total(products: List):
    total = 0

    for product in products:
        if not isinstance(product.value, int):
            raise TypeError("Product value must be an integer")
        total += product.value

    return total
