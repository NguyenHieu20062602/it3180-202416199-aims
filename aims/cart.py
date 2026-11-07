MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giá» hÃ ng chá»©a tá»‘i Ä‘a MAX_NUMBERS_ORDERED Ä‘Ä©a DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("ÄÃ£ thÃªm Ä‘Ä©a vÃ o giá» hÃ ng")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)

    def print_cart(self):
        print("Cart items:")
        for index, dvd in enumerate(self.items, start=1):
            print(f"{index}. {dvd}")
        print(f"Total cost: {self.total_cost():.2f} $")

    def sort_by_title(self):
        self.items.sort(key=lambda dvd: dvd.title.lower())

    def sort_by_cost(self):
        self.items.sort(key=lambda dvd: dvd.cost)
