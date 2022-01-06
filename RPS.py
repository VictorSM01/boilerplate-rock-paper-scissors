# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


# This program implements a Markov chain-like strategy to beat
# the bots. It considers the most common n-steps sequence of
# the opponent to make the prediction of the future draw.
play_order = {}
opponent_history=[]

def player(prev_play):

    # State space
    states = ["R", "P", "S"]

    # Build the opponents history or reset it if it is facing a
    # new contender
    if prev_play in states:
        opponent_history.append(prev_play)
    else:
        opponent_history.clear()
        play_order.clear()

    prediction = predictor(opponent_history)

    return prediction

def predictor(history):

    # Number of previous moves considered
    n = 4

    # Dictionary of the ideal counter moves
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    if len(history) >= n:
        # Consider the n last moves
        last_n = "".join(history[-n:])
        # Actualize the record of previous sequences
        if last_n in play_order.keys():
            play_order[last_n] += 1
        else:
            play_order[last_n] = 1

        # Build the three next possible moves
        prev_sequ = "".join(history[-(n-1):])
        potential_plays = [
            prev_sequ + "R",
            prev_sequ + "P",
            prev_sequ + "S",
        ]

        # Check wether the potential moves have been already
        # seen in the game and with which frequency
        sub_order = {
            k: play_order[k]
            for k in potential_plays if k in play_order.keys()
        }
        # Make a prediction based on frequencies of the
        # potential moves
        if len(sub_order) >0:
            prediction = max(sub_order, key=sub_order.get)[-1:]
        else:
            # Default value if potential moves haben't been
            # seen yet in the game
            prediction = 'R'

        prediction = ideal_response[prediction]

    else:
        # Default value if there is still not enough history
        prediction = 'S'

    return prediction