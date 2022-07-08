class Karmic:
    def __init__(self):
        # Karma begins at base level of zero
        self.karma = 0

    def decrease(self):
        # Non ethical decisions lead to decrement of karma by 1 point
        self.karma -= 1

    def increase(self):
        # Ethical decision leads to increment of karma by 1 point
        self.karma += 1

    def returnKarma(self):
        return str(self.karma)


# test karma decreases
p1 = Karmic()
p1.decrease()
p1.decrease()
print("Karma decrement by two: Karma = " + p1.returnKarma())

# test karma increases
p1.increase()
p1.increase()
p1.increase()
print("Karma increment by 3: Karma = " + p1.returnKarma())