def search_by_category(cart, category):
    keyword = category.strip().lower()
    return [
        dvd for dvd in cart.items
        if keyword in dvd.category.lower()
    ]


def search_by_title(cart, title):
    keyword = title.strip().lower()
    return [
        dvd for dvd in cart.items
        if keyword in dvd.title.lower()
    ]
