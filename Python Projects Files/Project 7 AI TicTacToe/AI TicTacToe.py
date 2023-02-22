import random
import math


class Genius_computer_player:
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        if len(game.available_moves()) == 9:
           square =  random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']

        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = "O" if player == 'X' else 'X'

        if state.current_winner == other_player:

            return{'position': None, 'score': 1*(state.num_empty_squares() +1) if other_player == max_player else -1*(state.num_empty_squares() +1)}
        elif not state.num_empty_squares():

            return{'position': None,'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf} 

        for possible_moves in state.available_moves():
            state.make_move(possible_moves, player)
            sim_score = self.minimax(state, other_player)

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


