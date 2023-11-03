import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]    

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
        
    def test_search_player(self):
        player = self.stats.search("Semenko")
        self.assertAlmostEqual(player.name, "Semenko")

    def test_search_player_not_listed(self):
        player = self.stats.search("Thompson")
        self.assertAlmostEqual(player, None)
    
    def test_search_team_returns_list_of_players(self):
        team = self.stats.team("EDM")
        self.assertAlmostEqual(len(team), 3)
        
    def test_top_points(self):
        top_points = self.stats.top(3)
        self.assertAlmostEqual(top_points[0].name, "Gretzky")
        self.assertAlmostEqual(top_points[1].name, "Lemieux")
        self.assertAlmostEqual(top_points[2].name, "Yzerman")
        self.assertAlmostEqual(top_points[3].name, "Kurri")
        
    def test_top_goals(self):
        top_goals = self.stats.top(2, SortBy.GOALS)
        self.assertAlmostEqual(top_goals[0].name, "Lemieux")
        self.assertAlmostEqual(top_goals[1].name, "Yzerman")
    
    def test_top_assists(self):
        top_assists = self.stats.top(2, SortBy.ASSISTS)
        self.assertAlmostEqual(top_assists[0].name, "Gretzky")
        self.assertAlmostEqual(top_assists[2].name, "Lemieux")