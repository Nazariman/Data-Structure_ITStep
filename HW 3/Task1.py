# TASK 1
import time
import queue
import statistics

class FastFoodQueue:
    def __init__(self):
        # список з 4-ма чергами до кас
        self.queues = [queue.Queue() for _ in range(4)]
        # черга клієнтів на отримання замовлення
        self.order_queue = queue.Queue()
        # список з часом обслуговування клієнтів
        self.service_duration_history = []

    def add(self, client):  #додає клієнта в найкоротшу чергу
        shortest = min(self.queues, key = lambda q: q.qsize())
        shortest.put(client)
        print(f"Клієнт '{client}' став у чергу №{self.queues.index(shortest)}")
    
    def serve(self, idx): #обслуговуємо клієнта з черги за індексом. 
        if not self.queues[idx].empty(): 
            client = self.queues[idx].get()
            order_time = time.time()
            self.order_queue.put((client, order_time))
            print(f"Клієнт '{client}' зробив замовлення на касі {idx}")
        else: 
            print(f"Черга {idx} порожня")
         
    def make_order(self): #видає готове замовлення клієнту та обраховує скільки часу очікував клієнт
        if not self.order_queue.empty(): 
            client, order_time = self.order_queue.get()
            receive_time = time.time()
            duration = receive_time - order_time
            self.service_duration_history.append(duration)
            print(f"Клієнт '{client}' отримав замовлення. Час очікування: {round(duration, 2)} сек") 
        else: 
            print("Немає клієнтів у черзі на отримання")    
    
    def show_statistics(self): # виводить мінімальний, максимальний та середній час обслуговування клієнтів
        if not self.service_duration_history:
            print("Статистика відсутня — ще жодного замовлення не було видано")
            return
        min_time = min(self.service_duration_history)
        max_time = max(self.service_duration_history)
        avg_time = statistics.mean(self.service_duration_history)
        print("--- Статистика обслуговування ---")
        print(f"Мінімальний час: {round(min_time, 2)} сек")
        print(f"Максимальний час: {round(max_time, 2)} сек")
        print(f"Середній час: {round(avg_time, 2)} сек")


# Тестування
fast_food = FastFoodQueue()
fast_food.add("Олег")
fast_food.add("Анна")
fast_food.add("Марія")
fast_food.add("Сергій")

fast_food.serve(0)
fast_food.serve(1)

time.sleep(2)
fast_food.make_order()
time.sleep(3)
fast_food.make_order()

fast_food.show_statistics()
