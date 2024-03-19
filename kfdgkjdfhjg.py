# Завдання 2
# Реалізуйте клас "Кошик для покупок" з можливістю
# додавання товарів та підрахунку загальної вартості.
# Застосуйте інкапсуляцію для забезпечення правильності
# обробки даних.
class ShoppingCart:
    def __init__(self):
        self._items = []

    def add_item(self, name, count, price):
        """Додає товар у кошик."""
        if isinstance(name, str) and isinstance(price, (int, float)) and price > 0 and isinstance(count, int) and count > 0:
            self._items.append({"name": name, "price": price, "count": count})
        else:
            print("Некоректні дані товару.")

    def get_total_price(self):
        """Підраховує загальну вартість товарів у кошику."""
        return sum(item["price"] * item["count"] for item in self._items)

    def display_items(self):
        """Виводить список товарів у кошику та загальну вартість."""
        if not self._items:
            print("Кошик порожній.")
            return
        print("Товари у кошику:")
        for item in self._items:
            print(f"- {item['name']} {item['count']}: {item['price']} грн")
        print(f"Загальна вартість: {self.get_total_price()} грн")

cart = ShoppingCart()
cart.add_item("Книга", 2, 300)
cart.add_item("Ручка", 5, 15)
cart.add_item("Зошит", 3,20)
cart.add_item("Зошит", 3,20)

cart.display_items()