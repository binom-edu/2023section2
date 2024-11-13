from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self, name='untitled'):
        self.fuel = 100
        self.hp = 100
        self.name = name

    def __str__(self):
        return f'имя: {self.name}, здоровье: {self.hp}, сытость: {self.fuel}'
    
    @abstractmethod
    def speak(self):
        pass

class Cat(Pet):
    def __init__(self, name='untitled cat'):
        Pet.__init__(self, name)

    def meow(self):
        print(f'{self.name}: мяу')

    def speak(self):
        self.meow()

class Dog(Pet):
    def __init__(self, name='untitled dog'):
        Pet.__init__(self, name)

    def speak(self):
        print(f'{self.name}: гав')

cat1 = Cat('murzik')
cat2 = Cat('barsik')
print(cat1.name, cat2.name)
cat1.speak()
print(cat1)
sharik = Dog('Шарик')
sharik.speak()