import random
import math

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class Random_computer_player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class Human_player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None

        while not valid_square:
            square = input(self.letter+ '  turn. Input Move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid move try again.')

        return val        

class Genius_computer_player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']

        return square

    def minimax(self, state, player):
        # first we initialized both the players
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        #setting up base case (i.e end of the recursion whether it is tie or win)

        if state.current_winner == other_player:

            '''this will help while simulating scores too (it'll basically tell our GCP if the other player is 
            winning and if it is then make GCP's best move to block other player's move) other theory is when 
            GCP will get the winning Utility value of other player, it'll know how or what moves it made to 
            get 3 letters in a row and will block that row with GCP's letter'''

            return {'position': None, 'score': 1*(state.num_empty_squares()+1) if other_player == max_player 
                                          else -1*(state.num_empty_squares()+1) } 

        elif not state.num_empty_squares():
            #this is for the case of tie
            return {'postion': None, 'score': 0}

        '''and now if the game is not won neither its a tie, that means the game is still on, thus we'll create
        dictionaries for both insatnces i.e (whether GCP is maximizer or minimizer) that'll save the best move
        and the best score(i.e the utility value) that'll help our GCP win or tie)'''

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        '''now for every possibel move in the game, 1) we want to try that move 
        2) we want to get a simulated score that'll have all the states of the game after the move and 
        also inclucing aternating players.
        3) undo that move to simulate different move, but save the best postion to move in the simulated 
        game postion
        4) update dictionaries if better postion and scores are found for GCP to win'''

        for possible_moves in state.available_moves():
            state.make_move(possible_moves, player)
            sim_score =  self.minimax(state, other_player)

            state.board[possible_moves] = ' '
            state.current_winner = None
            sim_score['position'] = possible_moves

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best            
        


                          



