class Player:

    name = ""
    number = 0


class Team:
    name = ""
    antalPoints = 0

    def add_player(self, player):
        if player not in self.team:
            self.Team.append(player)

    def print_players(self):
        for player in self.team:
            print('--->', player.fullName())

    def playerName(self):
        return '{}'.format(self.first)

    def add_team(self, team):
        if team not in self.Team:
            self.team.append(team)

    def __init__(self, name):
        super().__init__(name, Team=None)
        if Team is None:
            self.team = []
        else:
            self.team = Player


player_1 = Player('Player1', 1)
player_2 = Player('Player2', 2)
player_3 = Player('Player3', 3)

team_1 = Team('team1', 50)
team_2 = Team('team2', 99)


team_1.add_player(player_1)
team_1.add_player(player_2)
team_2.add_player(player_3)

team_1.print_players()
team_2.print_players()






