✂️ Rock Paper Scissors AI

This project is a solution to the Rock Paper Scissors project
 from the Machine Learning with Python Certification by .

The goal is to create an AI that predicts the opponent’s next move in the classic Rock-Paper-Scissors game using historical moves.

🧠 Project Overview

The AI keeps track of the opponent’s previous plays.

It analyzes patterns over the last 3 moves and adapts its responses.

It tries to counter the opponent’s expected choice based on frequency and sequence.

Default behavior: if there’s no previous move, it starts with Rock.

🧰 Features

✅ Track opponent’s history

✅ Adaptive response based on last 1–3 moves

✅ Uses simple rule-based logic instead of ML libraries

🔄 Can be used in iterative Rock-Paper-Scissors matches

📂 File Structure
.
├── RPS.py             # Main AI function
└── README.md

🧪 How to Run

Import the player function

from RPS import player


Call the function with the opponent’s last move

move = player('R')  # Opponent played Rock last
print(move)          # AI chooses counter move


Iterate in a loop for multiple rounds

opponent_moves = ['R', 'P', 'S']
for m in opponent_moves:
    print(player(m))

🔍 Logic Overview

opponent_history stores previous moves.

last_three analyzes the last 3 moves to detect patterns:

All three moves different → counter with 'S': 'P', 'P': 'R', 'R': 'P'

Two different moves → counter with 'P': 'S', 'R': 'P', 'S': 'R'

Single repeated move → repeat the same move

Default guess is Rock if no previous move exists.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    guess = prev_play if prev_play != '' else 'R'
    last_three = set(opponent_history[-3:])
    # pattern detection...
    return response[guess]

📝 Notes

This project demonstrates pattern recognition and adaptive logic.

No external ML libraries are used, but the logic mimics predictive behavior.

Ideal for showing understanding of state tracking and simple AI strategies.

👤 Author

BondAlex-maker
🔗 GitHub Repository
