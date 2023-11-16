from BasketBallPlayer import BasketBallPlayer


class Defender(BasketBallPlayer):
    '''
    A defenders class that holds the name, posessions, minutes, offense, defense, total, speed, age, and stamina of defenders. A child of the BasketBallPlayer class.

    Attributes
    ----------
    name : str
				Full name of the defender
    posessions : int
				The # of total posessions played by the defender
    minutes : int
				The # of total minutes played by the defender
    __offense : float
				The truncated RAPTOR offense rating for this defender
    __defense : float
				The truncated RAPTOR defense rating for this defender
    __total : float
		    	The truncated RAPTOR total rating for this defender
    speed: int
				The speed rating for this defender
    __age: int
				The age of this defender
    stamina: int
				The stamina of this defender

    Methods
    -------
    possPerMin()
				Prints the # of posessions each player averages per minute
	possPerGame()
				Prints the # of posessions each player averages per game, if their total stats were spread across 82 games
	minPerGame()
				Prints the # of minutes each player averages per game, if their total stats were spread across 82 games
    speedTraining()
				Prints the updated speed rating of a defender after a user inputs the number of hours of training
	shootingPercentCalc()
				Prints the projected oppponent's field goal % based on the opponent's overall when guarded by a defender
	projectedSalary()
				Prints the projected salary of a defender, along with the age-adjusted projected salary

    '''
    def __init__(self, name, posessions, minutes, __offense, __defense, __total, speed, __age, stamina):
        '''
        Constructor to build a defender object


        Parameters
        ----------
        	name : str
						Full name of the defender
    		posessions : int
						The # of total posessions played by the defender
    		minutes : int
						The # of total minutes played by the defender
    		__offense : float
						The truncated RAPTOR offense rating for this defender
    		__defense : float
						The truncated RAPTOR defense rating for this defender
    		__total : float
		    			The truncated RAPTOR total rating for this defender
			speed: int
						The speed rating for this defender
    		__age: int
						The age of this defender
    		stamina: int
						The stamina of this defender


        '''
        super().__init__(name, posessions, minutes, __offense, __defense, __total)
        self.speed = speed
        self.age = __age
        self.stamina = stamina


    def __str__(self):

        '''
        Returns a string with the defender's name, # of posessions, # of minutes, RAPTOR offense, RAPTOR defense, RAPTOR total, speed and stamina.

        Returns
        -------
        The defender's name, posessions, minutes, offense, defense, total, speed, stamina in a string

        '''
        return f"The defender {self.name} had {self.posessions} posessions and played a total of {self.minutes} minutes this season. His RAPTOR offense was {self.offense}, RAPTOR defense was {self.defense}, and his RAPTOR total was {self.total}. His speed rating was {self.speed} ovr. His stamina rating was {self.stamina} ovr."


    def speedTraining(self):
        '''
        Prints defender's updated speed after a certain number of hours of training

        This takes a # of hours trained from the user, and adds that value to the defender's speed

        '''
        print(f"{self.name}'s speed rating is {self.speed}")
        hoursTrained = int(input("How many hours did this player train for? "))
        self.speed = int(self.speed + hoursTrained)
        print(f"{self.name}'s new temporary speed rating is {self.speed}")

    def shootingPercentCalc(self):
        '''
        Prints defender's opponent's projected field goal percentage based on their overall

        This takes a user's input for the overall of an oponent, and divides that value by the defender's defense

        '''
        opponentOverall = int(input("What is the opponent's overall rating out of 99? "))
        opponentFG = int((opponentOverall/self.defense))
        print(f"{self.name}'s opponent's projected field goal percentage when guarded by him is {opponentFG}")

    def projectedSalary(self):
        '''
        Prints defender's projected salary and age-adjusted projected salary

        This takes the projected salary from its parent class and extends it. For the age-adjusted salary, it adds the player's RAPTOR offense, RAPTOR defense, minutes/1000, posessions/5000, subtracts the defender's age by 30, and multiplies all of that by 3000000

        '''
        super().projectedSalary()
        print(f"His age-adjusted projected salary is ${int((self.offense + self.defense + 1 + (self.minutes/1000) + (self.posessions/5000) - (self.age-30)) * 3000000)} ")

