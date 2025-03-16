from typing import List


def calculate_total(products: List):
    total = 0

    for product in products:
        try:
            total += int(product.value)
        except ValueError:
            raise TypeError("Product value must be convertible to an integer")
        total += product.value

    return total
