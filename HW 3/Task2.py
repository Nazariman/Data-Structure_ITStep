import queue

class Passenger:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"{self.name} (пріоритет {self.priority})"

class Zone:
    def __init__(self, name):
        self.name = name
        self.passengers = queue.PriorityQueue()

    def add(self, passenger):
        self.passengers.put((passenger.priority, passenger))
        print(f"Додано пасажира {passenger} до зони '{self.name}'")

    def serve_passenger(self):
        if not self.passengers.empty():
            _, passenger = self.passengers.get()
            print(f"Обслуговується пасажир {passenger} у зоні '{self.name}'")
            return passenger
        else:
            print(f"У зоні '{self.name}' немає пасажирів")
            return None


class Airport:
    def __init__(self):
        self.zones = {
            "реєстрація": Zone("реєстрація"),
            "контроль безпеки": Zone("контроль безпеки"),
            "посадка": Zone("посадка")
        }
        self.passengers = []  # пройшли всі зони

    def add(self, passenger):
        self.zones["реєстрація"].add(passenger)

    def serve_registration(self):
        passenger = self.zones["реєстрація"].serve_passenger()
        if passenger:
            self.zones["контроль безпеки"].add(passenger)

    def serve_security_control(self):
        passenger = self.zones["контроль безпеки"].serve_passenger()
        if passenger:
            self.zones["посадка"].add(passenger)

    def serve_boarding(self):
        passenger = self.zones["посадка"].serve_passenger()
        if passenger:
            self.passengers.append(passenger)
            print(f"Пасажир {passenger.name} успішно пройшов всі етапи! 🛫")

    def show_statistics(self):
        print("\n--- Статистика ---")
        for name, zone in self.zones.items():
            print(f"У зоні '{name}': {zone.passengers.qsize()} пасажирів")
        print(f"Пасажирів, які пройшли всі зони: {len(self.passengers)}")




# Тестування
airport = Airport()
passengers = [
    Passenger("Олег", 3),
    Passenger("Анна", 1),
    Passenger("Марія", 4),
    Passenger("Сергій", 2)
]

for p in passengers:
    airport.add(p)

airport.serve_registration()
airport.serve_registration()
airport.serve_security_control()
airport.serve_boarding()

airport.show_statistics()

