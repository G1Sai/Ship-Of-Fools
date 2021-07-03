from ShipOfFools import *

if __name__ == "__main__":
    room = PlayRoom()
    room.set_game(ShipOfFoolsGame())
    room.add_player(Player("Ling"))
    room.add_player(Player("Chang"))
    room.reset_scores()
    roun=0
    while not room.game_finished():
        print("\n*******Round %d*******"%(roun+1))
        room.play_round()
        print()
        room.print_scores()
        roun=roun+1
    print()
    print("*******Final Scores*******")
    print()
    room.print_scores()
    print()   
    room.print_winner()
