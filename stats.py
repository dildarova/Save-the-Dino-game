class Stats():
    """statistics"""

    def __init__(self):
        """initializes statistics"""
        self.current_stats()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline())


    def current_stats(self):
        """statistisc changing during the game"""
        self.dino_lives = 2
        self.score = 0
