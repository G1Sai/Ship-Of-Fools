from random import randint    

class ShipOfFoolsGame:
'''
 Responsible for the game logic and has the ability to play a round of the game resulting in a score.
 Also has a property that tells what accumulated score results in a winning state
'''
    def __init__(self):
        self._cup=DiceCup()
        self.winning_score=21
        self.has_ship=False
        self.has_captain=False
        self.has_crew=False
    def round(self):
        for num in range(3):
            self._cup.roll()
            if (not self.has_ship):
                for i in range(0,5):
                    if(self._cup.value(i)==6):
                        self._cup.bank(i)
                        self.has_ship=True
                        break
            if (not self.has_captain&self.has_ship):
                for i in range(0,5):
                    if(self._cup.value(i)==5):
                        self._cup.bank(i)
                        self.has_captain=True
                        break
            if (not self.has_crew&self.has_ship&self.has_captain):
                for i in range(0,5):
                    if(self._cup.value(i)==4):
                        self._cup.bank(i)
                        self.has_crew=True
                        break
            if(self.has_ship&self.has_captain&self.has_crew):
                score=0
                for i in range(0,5):
                    if(self._cup.value(i)>3):
                        self._cup.bank(i)
                    score=score+self._cup.value(i)
        self._cup.release_all()
        if(self.has_ship&self.has_captain&self.has_crew):
            self.has_ship=False
            self.has_captain=False
            self.has_crew=False
            return score-15
        self.has_ship=False
        self.has_captain=False
        self.has_crew=False
        return 0
        
 
 
class Player:
'''
Responsible for the score of the individual player. Has the ability, given a game logic, play a 
round of a game. The gained score is accumulated in the attribute score.
'''
    def __init__(self, namestring):
        self._name=namestring
        self._score=0
    def get_name(self):
        return self._name
    def set_name(self, namestring):
        self._name=namestring
    def play_round(self, game):
        print()
        print("%s's Dice:"%(self._name))
        self._score=self._score+game.round()
    def current_score(self):
        return self._score
    def reset_score(self):
        self._score=0
	
 
 

class PlayRoom:
'''
Responsible for handling a number of players and a game. Every round the room lets each 
player play, and afterwards check if any player have reached the winning score.
'''
    _players=[]
    round=0
    def set_game(self,game):
        self._game=game
    def add_player(self,player):
        self._players.append(player)
    def reset_scores(self):
        for i in range(len(self._players)):
            self._players[i].reset_score()
    def play_round(self):
        for i in range(len(self._players)):
            self._players[i].play_round(self._game)
    def game_finished(self):
        for i in range(len(self._players)):
            if(self._players[i].current_score()>=self._game.winning_score):
                return True
        return False
    def print_scores(self):
        print("%-11s %4s"%("Player","Score"))
        for i in range(len(self._players)):
            print("%-11s %d"%(self._players[i].get_name(),self._players[i].current_score()))
    def print_winner(self):
        highest_score=self._players[0].current_score()
        winners=[]
        for i in range(len(self._players)):
            if(self._players[i].current_score()>highest_score):
                highest_score=self._players[i].current_score()
        for i in range(len(self._players)):
            if(self._players[i].current_score()==highest_score):
                winners.append(self._players[i].get_name())
        if(len(winners)==1):
            print("Winner is %s!"%(winners[0]))
        elif(len(winners)>1):
            print("Winners are ",end="")
            for i in range(len(winners)-1):
                print(winners[i]+", ",end="")
            print("and "+winners[len(winners)-1]+"!")
            


class DiceCup:
'''
Handles five objects (dice) of class Die. Has the ability to bank and release dice individually.
Can also roll dice that are not banked.
'''
    def __init__(self, num=5):
        self._dice=[]
        self._num=num
        for i in range(0,num):
            self._dice.append([Die(),0])
    def value(self, index):
        return self._dice[index][0].get_value()
    def is_banked(self, index):
        return self._dice[index][1]
    def bank(self, index):
        self._dice[index][1]=1
    def release(self, index):
        self._dice[index]=0
    def release_all(self):
        for i in range(0,self._num):
            self._dice[i][1]=0
    def roll(self):
        for i in range(0,self._num):
            if(self.is_banked(i)==0):
                self._dice[i][0].roll()
            print(self._dice[i][0].get_value(),end=" ")
        print()   

    
class Die:
'''
Used to generate a random integer value between 1 and 6
'''
    def __init__(self):
        self._value=1
        self.roll()
    def roll(self):
        self._value=randint(1,6)
    def get_value(self):
        return self._value
