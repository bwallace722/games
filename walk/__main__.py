import state
import runner

def main():
    game_state = state.State()
    game_runner = runner.Runner(game_state)
    game_runner.run()

if __name__ == "__main__":
    main()

