from BasketBallPlayer import BasketBallPlayer


class Scorer(BasketBallPlayer):
    '''

    '''
    def __init__(self, name, posessions, minutes, __offense, __defense, __total):

        '''

        '''
        self.name = name
        self.posessions = posessions
        self.minutes = minutes
        self.offense = __offense
        self.defense = __defense
        self.total = __total

    def __str__(self):
        super().__str__()
        '''

        '''
        return f"{self.name} had {self.posessions} posessions and played a total of {self.minutes} minutes this season. His RAPTOR offense was {self.offense}, RAPTOR defense was {self.defense}, and his RAPTOR total was {self.total}."

    def ppgCalc(self):
        print(f"His projected point per game stat is {int((self.offense + 3)*5)}")

    def skillCalc(self):
        skill = int(self.offense * 10)
        print(f"This player's skil is {skill}")
        hoursPracticed = int(input("How many hours did this player practice? "))
        skill = int((self.offense + hoursPracticed) * 100)
        print(f"This player's new skil is {skill}")


    def shootingPercentCalc(self):
        attemptedShots = int(input("How many shots did this player take? "))
        print(f"His projected field goal percentage is {int((attemptedShots/self.offense)*10)}")
