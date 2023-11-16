from BasketBallPlayer import BasketBallPlayer


class Scorer(BasketBallPlayer):
    '''
    A scorers class that holds the name, posessions, minutes, offense, defense, total, speed, age, and stamina of scorers. A child of the BasketBallPlayer class

    Attributes
    ----------
    name : str
				Full name of the scorer
    posessions : int
				The # of total posessions played by the scorer
    minutes : int
				The # of total minutes played by the scorer
    __offense : float
				The truncated RAPTOR offense rating for this scorer
    __defense : float
				The truncated RAPTOR defense rating for this scorer
    __total : float
		    	The truncated RAPTOR total rating for this scorer
    speed: int
				The speed rating for this scorer
    __age: int
				The age of this scorer
    stamina: int
				The stamina of this scorer

    Methods
    -------
    possPerMin()
				Prints the # of posessions each player averages per minute
	possPerGame()
				Prints the # of posessions each player averages per game, if their total stats were spread across 82 games
	minPerGame()
				Prints the # of minutes each player averages per game, if their total stats were spread across 82 games
    skillCalc()
				Prints the updated skill rating of a scorer after a user inputs the number of hours of practice
	remainingStamina()
				Prints the remaining stamina of a scorer after a user inputs the number of minutes played
	projectedSalary()
				Prints the projected salary of a scorer, along with the age-adjusted projected salary

    '''
    def __init__(self, name, posessions, minutes, __offense, __defense, __total, speed, __age, stamina):
        super().__init__(name, posessions, minutes, __offense, __defense, __total)
        self.speed = speed
        self.age = __age
        self.stamina = stamina

        '''
        Constructor to build a defender object


        Parameters
        ----------
        	name : str
						Full name of the scorer
    		posessions : int
						The # of total posessions played by the scorer
    		minutes : int
						The # of total minutes played by the scorer
    		__offense : float
						The truncated RAPTOR offense rating for this scorer
    		__defense : float
						The truncated RAPTOR defense rating for this scorer
    		__total : float
		    			The truncated RAPTOR total rating for this scorer
			speed: int
						The speed rating for this scorer
    		__age: int
						The age of this scorer
    		stamina: int
						The stamina of this scorer


        '''


    def __str__(self):
        '''
        Returns a string with the scorer's name, # of posessions, # of minutes, RAPTOR offense, RAPTOR defense, RAPTOR total, speed and stamina.

        Returns
        -------
        The scorer's name, posessions, minutes, offense, defense, total, speed, stamina in a string

        '''
        return f"The scorer {self.name} had {self.posessions} posessions and played a total of {self.minutes} minutes this season. His RAPTOR offense was {self.offense}, RAPTOR defense was {self.defense}, and his RAPTOR total was {self.total}. His speed rating was {self.speed} ovr. His stamina rating was {self.stamina} ovr."


    def skillCalc(self):
        '''
        Prints scorer's updated skill after a certain number of hours of practice

        This calculates an initial skill level by multiplying the offense by 10, takes a # of hours practiced from the user, adds that value to the scorer's skill, and multiplies by 10

        '''
        skill = int(self.offense * 10)
        print(f"{self.name}'s skill rating is {skill}")
        hoursPracticed = int(input("How many hours did this player practice? "))
        skill = int((self.offense + hoursPracticed) * 10)
        print(f"{self.name}'s new skill rating is {skill}")

    def remainingStamina(self):
        '''
        Prints scorer's updated stamina after a certain number of hours of practice

        This takes a # of minutes played from the user and subtracts that value from the scorer's stamina

        '''
        print(f"{self.name}'s stamina is {self.stamina}")
        minutesPlayedInGame = int(input(f"How many minutes did this player play? "))
        self.stamina = int(self.stamina - minutesPlayedInGame)
        print(f"His remaining stamina is {self.stamina}")


    def projectedSalary(self):
        '''
        Prints scorer's projected salary and age-adjusted projected salary

        This takes the projected salary from its parents class and extends it. For the age-adjusted salary, it adds the player's RAPTOR offense, RAPTOR defense, minutes/1000, posessions/5000, subtracts the defender's age by 30, and multiplies all of that by 3000000

        '''
        super().projectedSalary()
        print(f"{self.name}'s age-adjusted projected salary is ${int((self.offense + self.defense + 1 + (self.minutes/1000) + (self.posessions/5000) - (self.age - 30)) * 3000000)} per year")

