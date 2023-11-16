from BasketBallPlayer import BasketBallPlayer


class Defender(BasketBallPlayer):
    '''

    '''
    def __init__(self, name, posessions, minutes, __offense, __defense, __total, speed, __age, stamina):
        super().__str__(name, posessions, minutes, __offense, __defense, __total)

        '''

        '''
        self.speed = speed
        self.age = __age
        self.stamina = stamina

    def __str__(self):
        super().__str__()
        '''

        '''
        return f"The defender {self.name} had {self.posessions} posessions and played a total of {self.minutes} minutes this season. His RAPTOR offense was {self.offense}, RAPTOR defense was {self.defense}, and his RAPTOR total was {self.total}. His speed rating was {self.speed} ovr. His stamina rating was {self.stamina} ovr."


    def speedTraining(self):
        print(f" {int(self.defense + 4)}")

    def shootingPercentCalc(self):
        opponentOverall = int(input("What is the opponent's overall rating out of 100?"))
        opponentFG = int(100 - (opponentOverall/self.defense))
        print(f"His opponents projected field goal percentage when guarded by him is {opponentFG}")

    def projectedSalary(self):
        super().projectedSalary()
        print(f"His age-adjusted projected salary is {int((self.offense + self.defense + 1 + (self.minutes/1000) + (self.posessions/5000) - (self.age/30)) * 3000000)} ")

