class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):  # SPAMFilter 是 Filter 的子类
    def init(self):  # 重写超类 Filter 的方法 init
        self.blocked = ['SPAM']


class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print('Hi, my value is', self.value)


class TalkingCalculator(Calculator, Talker):
    pass

from abc import ABC, abstractmethod

class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass

class Knigget(Talker):
    def talk(self):
        print("Ni!")

