from BasketBallPlayer import BasketBallPlayer


class Defender(BasketBallPlayer):
    '''

    '''
    def __init__(self, name, posessions, minutes, __offense, __defense, __total):
        super().__init__(name, posessions, minutes, __offense, __defense, __total)

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


    def stealsBlocksCalc(self):
        print(f"His projected combined steals and blocks per game stat is {int(self.defense + 4)}")

    def shootingPercentCalc(self):
        opponentOverall = int(input("What is the opponent's overall rating out of 100?"))
        opponentFG = int(100 - (opponentOverall/self.defense))
        print(f"His opponents projected field goal percentage when guarded by him is {opponentFG}")
