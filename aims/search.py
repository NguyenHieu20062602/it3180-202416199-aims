def search_by_title(cart, title):
    keyword = title.strip().lower()
    return [
        dvd for dvd in cart.items
        if keyword in dvd.title.lower()
    ]