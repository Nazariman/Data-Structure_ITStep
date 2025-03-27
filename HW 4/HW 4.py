class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class TreeNode:
    def __init__(self, car):
        self.car = car
        self.left = None
        self.right = None


class CarPark:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, car):
        def _insert(node, car):
            if not node:
                return TreeNode(car)
            if car.model < node.car.model:
                node.left = _insert(node.left, car)
            else:
                node.right = _insert(node.right, car)
            return node

        self.root = _insert(self.root, car)
        self.size += 1

    def search(self, model):
        def _search(node, model):
            if not node:
                return None
            if model == node.car.model:
                return node.car
            elif model < node.car.model:
                return _search(node.left, model)
            else:
                return _search(node.right, model)

        return _search(self.root, model)

    def remove(self, model):
        def _remove(node, model):
            if not node:
                return node, None
            if model < node.car.model:
                node.left, deleted = _remove(node.left, model)
            elif model > node.car.model:
                node.right, deleted = _remove(node.right, model)
            else:
                deleted = node.car
                if not node.left:
                    return node.right, deleted
                elif not node.right:
                    return node.left, deleted

                min_larger_node = self._min_value_node(node.right)
                node.car = min_larger_node.car
                node.right, _ = _remove(node.right, min_larger_node.car.model)
            return node, deleted

        self.root, deleted = _remove(self.root, model)
        if deleted:
            self.size -= 1
        return deleted

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def __len__(self):
        return self.size

    def sell_car(self, client, model):
        car = self.remove(model)
        if car:
            print(f"Клієнту {client} продано автомобіль: {car}")
        else:
            print(f"Автомобіль з маркою '{model}' не знайдено")
