from BasketBallPlayer import BasketBallPlayer


class Scorer(BasketBallPlayer):
    '''

    '''
    def __init__(self, name, posessions, minutes, __offense, __defense, __total, speed, __age, stamina):
        super().__init__(name, posessions, minutes, __offense, __defense, __total)
        self.speed = speed
        self.age = __age
        self.stamina = stamina

        '''

        '''


    def __str__(self):
        '''

        '''
        return f"The scorer {self.name} had {self.posessions} posessions and played a total of {self.minutes} minutes this season. His RAPTOR offense was {self.offense}, RAPTOR defense was {self.defense}, and his RAPTOR total was {self.total}. His speed rating was {self.speed} ovr. His stamina rating was {self.stamina} ovr."


    def skillCalc(self):
        skill = int(self.offense * 10)
        print(f"{self.name}'s skill is {skill}")
        hoursPracticed = int(input("How many hours did this player practice? "))
        skill = int((self.offense + hoursPracticed) * 10)
        print(f"{self.name}'s new skil is {skill}")

    def remainingStamina(self):
        print(f"{self.name}'s stamina is {self.stamina}")
        minutesPlayedInGame = int(input(f"How many minutes did this player play? "))
        print(f"His remaining stamina is {int(self.stamina - minutesPlayedInGame)}")

    def shootingPercentCalc(self):
        attemptedShots = int(input("How many shots did this player take? "))
        print(f"{self.name}'s projected field goal percentage is {int((attemptedShots/self.offense)*10)}%")

    def projectedSalary(self):
        super().projectedSalary()
        print(f"{self.name}'s age-adjusted projected salary is ${int((self.offense + self.defense + 1 + (self.minutes/1000) + (self.posessions/5000) - (self.age/30)) * 3000000)} per year")

