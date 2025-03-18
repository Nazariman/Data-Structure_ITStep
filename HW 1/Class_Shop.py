import base_code

class Shop:
    def __init__(self):
        self.queue1 = base_code.DoubleLinkedList()
        self.queue2 = base_code.DoubleLinkedList()
        self.queue3 = base_code.DoubleLinkedList()

    def add_buyer(self, name, idx):
        if idx == 1:
            self.queue1.push_end(name)
        elif idx == 2:
            self.queue2.push_end(name)
        elif idx == 3:
            self.queue3.push_end(name)
        else:
            print("Невірний номер черги!")

    def serve_buyer(self, idx):
        if idx == 1:
            buyer = self.queue1.pop_start()
        elif idx == 2:
            buyer = self.queue2.pop_start()
        elif idx == 3:
            buyer = self.queue3.pop_start()
        else:
            print("Невірний номер черги!")
            return

        if buyer:
            print(f"Обслуговано покупця: {buyer}")
        else:
            print(f"Черга {idx} порожня! Викликаємо _reorder.")
            self._reorder(idx)

    def _reorder(self, idx):
        last_buyer = None
        if self.queue3.tail:
            last_buyer = self.queue3.pop_end()
        elif self.queue2.tail:
            last_buyer = self.queue2.pop_end()
        elif self.queue1.tail:
            last_buyer = self.queue1.pop_end()

        if last_buyer:
            print(f"Переміщуємо останнього покупця ({last_buyer}) у чергу {idx}.")
            self.add_buyer(last_buyer, idx)
        else:
            print("Усі черги порожні, немає кого переміщати.")

    def display_info(self):
        print(f"Черга 1: {self.queue1}")
        print(f"Черга 2: {self.queue2}")
        print(f"Черга 3: {self.queue3}")
        
        
# Приклад використання
shop = Shop()
shop.add_buyer("Олег", 1)

# Домашнє завдання
shop.add_buyer("Марина", 2)
shop.add_buyer("Марія", 2)
shop.add_buyer("Андрій", 3)
shop.add_buyer("Ірина", 1)
shop.add_buyer("Василь", 2)
shop.add_buyer("Тетяна", 3)
shop.add_buyer("Сергій", 3)
shop.add_buyer("Анна", 3)
print("Черги:")
shop. display_info()
shop.serve_buyer(1)
shop.serve_buyer(2)
shop.serve_buyer(3)
print("Після обслуговування покупців:")
shop. display_info()
shop.serve_buyer(1)
print("Покупці перейшли до вільної каси:")
shop. display_info()