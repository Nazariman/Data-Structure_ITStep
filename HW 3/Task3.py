# TASK3
from Task2 import Zone

class Passenger:
    def __init__(self, name, priority, baggage=None):
        if baggage is None:
            baggage = []
        self.name = name
        self.priority = priority
        self.baggage = baggage

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"{self.name} (пріоритет {self.priority})"

class RegistrationZone(Zone):
    def serve_passenger(self):
        if not self.passengers.empty():
            _, passenger = self.passengers.get()
            if "білет" in passenger.baggage:
                print(f"✅ Пасажир {passenger} пройшов реєстрацію")
                return passenger, True
            else:
                print(f"❌ Пасажир {passenger} не має білета — відмова у реєстрації")
                return passenger, False
        else:
            print(f"У зоні '{self.name}' немає пасажирів")
            return None, False


class SecurityZone(Zone):
    def serve_passenger(self):
        if not self.passengers.empty():
            _, passenger = self.passengers.get()
            dangerous_items = {"ніж", "зброя", "вибухівка"}
            if any(item in dangerous_items for item in passenger.baggage):
                print(f"❌ Пасажир {passenger} має заборонені предмети — зупинено на безпеці")
                return passenger, False
            else:
                print(f"✅ Пасажир {passenger} пройшов контроль безпеки")
                return passenger, True
        else:
            print(f"У зоні '{self.name}' немає пасажирів")
            return None, False


class BoardingZone(Zone):
    def serve_passenger(self):
        if not self.passengers.empty():
            _, passenger = self.passengers.get()
            print(f"✅ Пасажир {passenger} проходить на посадку")
            return passenger, True
        else:
            print(f"У зоні '{self.name}' немає пасажирів")
            return None, False


class Airport:
    def __init__(self):
        self.zones = {
            "реєстрація": RegistrationZone("реєстрація"),
            "контроль безпеки": SecurityZone("контроль безпеки"),
            "посадка": BoardingZone("посадка")
        }
        self.passengers = []  # пройшли всі зони

    def add(self, passenger):
        self.zones["реєстрація"].add(passenger)

    def serve_registration(self):
        passenger, success = self.zones["реєстрація"].serve_passenger()
        if passenger and success:
            self.zones["контроль безпеки"].add(passenger)

    def serve_security_control(self):
        passenger, success = self.zones["контроль безпеки"].serve_passenger()
        if passenger and success:
            self.zones["посадка"].add(passenger)

    def serve_boarding(self):
        passenger, success = self.zones["посадка"].serve_passenger()
        if passenger and success:
            self.passengers.append(passenger)
            print(f"✈️ Пасажир {passenger.name} успішно пройшов всі етапи! 🛫")

    def show_statistics(self):
        print("\n--- Статистика ---")
        for name, zone in self.zones.items():
            print(f"У зоні '{name}': {zone.passengers.qsize()} пасажирів")
        print(f"Пасажирів, які пройшли всі зони: {len(self.passengers)}")


# Використання
passenger1 = Passenger("Alice", 2, ["ticket", "phone"])
passenger2 = Passenger("Bob", 1, ["ticket", "knife"])
passenger3 = Passenger("Charlie", 3, ["ticket"])
passenger4 = Passenger("David", 4, ["ticket", "laptop"])
passenger5 = Passenger("Eva", 2, ["bottle", "knife"])
passenger6 = Passenger("Frank", 3, ["book"])
passenger7 = Passenger("Grace", 1, ["ticket", "explosives"])
passenger8 = Passenger("Hannah", 5, ["phone", "tablet"])
passenger9 = Passenger("Ivy", 2, ["ticket", "earphones"])
passenger10 = Passenger("Jack", 1, ["ticket", "gun"])

# Створюємо аеропорт
airport = Airport()

# Додаємо пасажирів до реєстрації
airport.add(passenger1)
airport.add(passenger2)
airport.add(passenger3)
airport.add(passenger4)
airport.add(passenger5)
airport.add(passenger6)
airport.add(passenger7)
airport.add(passenger8)
airport.add(passenger9)
airport.add(passenger10)

# Проходимо етапи для кожного пасажира
for _ in range(10):
    airport.serve_registration()
    airport.serve_security_control()
    airport.serve_boarding()

# Показуємо статистику
airport.show_statistics()