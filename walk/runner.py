class Runner(object):

    def __init__(self, game_state):
        self.game_state = game_state

    def run(self):
        print("Starting game with state: " + str(self.game_state))
