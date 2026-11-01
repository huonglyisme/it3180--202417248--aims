def discounted_total(total, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Invalid discount percentage")

    return total * (1 - percent / 100)
