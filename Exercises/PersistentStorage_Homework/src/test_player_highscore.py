import unittest
from player_highscore import manage_highscore 
from player_highscore import zero_highscore 

class TestPlayerHighscore(unittest.TestCase):
    
    def setUp(self):
        """Make sure there is no previous high score file to mess the tests"""
        zero_highscore()
        
    def testNoPreviousScore(self):
        """Test a player with no previous registered high score"""
        player_name = "john"
        player_score = 3
        self.assertEqual(player_score, manage_highscore(player_name,player_score))
    
    def testLowerPreviousScore(self):
        """Test a player with a lower high score compared to the latest score"""
        player_name = "john"
        player_high_score = 2
        player_latest_score = 4
        manage_highscore(player_name, player_high_score)
        self.assertEqual(player_latest_score, manage_highscore(player_name, player_latest_score))
        
    def testHigherPreviousScore(self):
        """Test a player with a previous higher high score than the latest one"""
        player_name = "john"
        player_high_score = 4
        player_latest_score = 2
        manage_highscore(player_name, player_high_score)
        self.assertEqual(player_high_score, manage_highscore(player_name, player_latest_score))
        
    def testEqualPreviousHighScore(self):
        """Test a player with a high score equal to latest score"""
        player_name = "john"
        player_high_score = 3
        player_latest_score = 3
        manage_highscore(player_name, player_high_score)
        self.assertEqual(player_latest_score, manage_highscore(player_name, player_latest_score))
    
if __name__ == "__main__":
    unittest.main()
