from enum import Enum


class Discipline(Enum):
    Geisteswissenschaften = 0,
    Humanwissenschaften = 1,
    Ingenieurwissenschaften = 2,
    Naturwissenschaften = 3,
    Agrarwissenschaften = 4,
    Philosophie = 5,
    Rechtswissenschaften = 6,
    Sozialwissenschaften = 7,
    Strukturwissenschaften = 8,
    Theologie = 9,
    Wirtschaftswissenschaften = 10

    def __str__(self):
        return self.name
