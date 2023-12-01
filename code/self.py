class Tomato:
    states = ['отсутствует', 'цветение', 'зеленый', 'красный']

    def __init__(self, index, state):
        self._index = index
        self._state = state

    def grow(self):
        if self._state < len(self.states) - 1:
            self._state += 1

    def is_ripe(self):
        return self._state == len(self.states) - 1


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index, 0) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        ripe_tomatoes = [tomato for tomato in self.tomatoes if tomato.is_ripe()]
        self.tomatoes = [tomato for tomato in self.tomatoes if not tomato.is_ripe()]
        return ripe_tomatoes

    def __str__(self):
        return f"Куст с {len(self.tomatoes)} помидорами"

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            ripe_tomatoes = self._plant.give_away_all()
            print(f"{self.name} собрал урожай: {len(ripe_tomatoes)} помидоров.")
        else:
            print(f"{self.name}, не все плоды созрели. Подождите еще немного.")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: ...")

    def __str__(self):
        return f"Садовод по имени {self.name}"



# Вызов справки по садоводству
Gardener.knowledge_base()


# Создание объектов TomatoBush и Gardener
tomato_bush = TomatoBush(5)
gardener = Gardener("Иван", tomato_bush)
print(tomato_bush)
print(gardener)
# Уход за кустом с помидорами
gardener.work()

# Проверка зрелости томатов
for tomato in tomato_bush.tomatoes:
  print(f"Томат {tomato._index}: {Tomato.states[tomato._state]}")
#
# Попытка сбора урожая, когда томаты еще не дозрели
gardener.harvest()

# Продолжение ухода за кустом
gardener.work()

# Проверка зрелости томатов
for tomato in tomato_bush.tomatoes:
 print(f"Томат {tomato._index}: {Tomato.states[tomato._state]}")

# Продолжение ухода за кустом
gardener.harvest()

# Проверка, что все томаты собраны
if not tomato_bush.tomatoes:
 print("Урожай собран полностью")
 # Т.к томаты не собраны, то ухаживаем за ними еще один круг, проверяем и собираем
gardener.work()
for tomato in tomato_bush.tomatoes:
 print(f"Томат {tomato._index}: {Tomato.states[tomato._state]}")
gardener.harvest()