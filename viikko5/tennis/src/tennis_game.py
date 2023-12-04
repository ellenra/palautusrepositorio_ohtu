SCORES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.tie()

        if self.player1_score >= 4 or self.player2_score >= 4:
            difference = self.player1_score - self.player2_score
            if difference == 1 or difference == -1:
                return self.advantage(difference)
            else:
                return self.win(difference)

        else:
            return f"{SCORES[self.player1_score]}-{SCORES[self.player2_score]}"
    
    def tie(self):
        if self.player1_score > 3:
            return "Deuce"
        else: 
            return f"{SCORES[self.player1_score]}-All"
        
    def advantage(self, difference):
        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        
    def win(self, difference):
        if difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
        
        
        
