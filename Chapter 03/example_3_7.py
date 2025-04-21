def calculate_discount(customer_type):
    if customer_type == "VIP":
        return 20
    elif customer_type == "Regular":
        return 10
    else:
        return 0