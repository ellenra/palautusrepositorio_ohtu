import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = self.get_players()

    def get_players(self):
        response = requests.get(self.url).json()
        players = []
        for i in response:
            players.append(Player(i))
        return players
            
class PlayerStats: 
    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()
        
    def top_scorers_by_nationality(self, nationality):
        player = []
        for i in self.players:
            if i.nationality == nationality:
                player.append(i)
        return sorted(player, key=lambda i: i.total, reverse=True)

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")
    print('Players from FIN\n')
    for player in players:
        print(player)

if __name__ == "__main__":
    main()