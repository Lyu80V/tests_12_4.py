import logging
from unittest import TestCase

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(TestCase):
    def test_walk(self):
        try:
            r1 = Runner('Ben', -5)
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance,50)
            logging.info(f'"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner')


    def test_run(self,):
        try:
            r2 = Runner(25)
            for i in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner')

    def test_challenge(self):
        r1 = Runner('Jerry')
        r2 = Runner('Tom')
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)

#first = Runner('Вася', 8)
'''second = Runner('Илья', 5)
third = Runner('Арсен', 10)

t = Tournament(101, first, second)
print(t.start())

t1 = Tournament(110,  second, third)
print(t1.start())'''

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s/%(levelname)s/%(message)s')

