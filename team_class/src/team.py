class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
        
    def add_player(self, player):
        self.players.append(player)
        
    def has_player(self, new_player):
        print(self.players)
        for player in self.players:
            if player==new_player:
                return True
        return False
    
    def play_game(self, game):
        if game == True:
            self.points = 3
        
        
        