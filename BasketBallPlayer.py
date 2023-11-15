
class BasketBallPlayer():
    '''
    A basketball players class that holds the name, posessions, minutes, offense, defense, and total of basketball players

    Attributes
    ----------
    name : str
				Full name of the basketball player
    posessions : int
				The # of total posessions played by the basketball player
    minutes : int
				The # of total minutes played by the basketball player
    __offense : float
				The truncated RAPTOR offense rating for this player
    __defense : float
				The truncated RAPTOR defense rating for this player
    __total : float
		    The truncated RAPTOR total rating for this player

    Methods
    -------
    possPerMin() -> int
				Prints the # of posessions each player averages per minute
		possPerGame() -> int
				Prints the # of posessions each player averages per game, if their total stats were spread across 82 games
		minPerGame() -> int
				Prints the # of minutes each player averages per game, if their total stats were spread across 82 games

    '''
    def __init__(self, name, posessions, minutes, __offense, __defense, __total):
        '''
        Constructor to build a basketball player object


        Parameters
        ----------
        name : str
						Full name of the basketball player
    		posessions : int
						The # of total posessions played by the basketball player
    		minutes : int
						The # of total minutes played by the basketball player
    		__offense : float
						The truncated RAPTOR offense rating for this player
    		__defense : float
						The truncated RAPTOR defense rating for this player
    		__total : float
		    		The truncated RAPTOR total rating for this player



        '''
        self.name = name
        self.posessions = posessions
        self.minutes = minutes
        self.offense = __offense
        self.defense = __defense
        self.total = __total

    def __str__(self):
        '''
        Returns a string with the basketball player's name, # of posessions, # of minutes, RAPTOR offense, RAPTOR defense, and RAPTOR total

        Returns
        -------
        The basketball player's name, posessionss, minutes, offense, defense, total in a string


        '''
        return f"{self.name} had {self.posessions} posessions and played a total of {self.minutes} minutes this season. His RAPTOR offense was {self.offense}, RAPTOR defense was {self.defense}, and his RAPTOR total was {self.total}."

    def possPerMin(self):
        '''
        Prints basketball player's posessions per minute

        This divides the player's total posessions by their total minutes

        Prints
        ------
        String
				Includes the player's posessions per minute

        '''
        print(f"He averaged approx. {self.posessions // self.minutes} posessions per minute.")

    def possPerGame(self):
        '''
        Prints basketball player's posessions per game, if spread across 82 games

        This divides the player's total posessions by 82 (# of games in a season)

        Prints
        ------
        String
				Includes the player's posessions per game

        '''
        print(f"He would have averaged approx. {self.posessions // 82} posessions per game, if his numbers were spread across 82 games.")

    def minPerGame(self):
        '''
        Prints basketball player's posessions per minute

        This divides the player's total minutes by 82 (# of games in a season)

        Prints
        ------
        String
				Includes the player's minutes per game

        '''
        print(f"He would have averaged approx. {self.minutes // 82} minutes per game, if his numbers were spread across 82 games")

    def projectedSalary(self):
      	print(f"His projected salary is {int((self.offense + self.defense + 1 + (self.minutes/1000) + (self.posessions/5000)) * 10000000)} ")

