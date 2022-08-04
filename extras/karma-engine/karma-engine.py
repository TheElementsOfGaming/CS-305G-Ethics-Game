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

        def returnOverall(self):
        # Verify where you stand ethically, this can be modified accordingly
        if self.karma < 0:
            ethics = "Low Ethics"
        elif self.karma < 5:
            ethics = "Average Ethics"
        elif self.karma > 5:
            ethics = "High Ethics"
        return ethics
   
        
