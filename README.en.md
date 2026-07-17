# TriClash 🪨📄✂️

A simple, fun command-line **Rock–Paper–Scissors** game written in Python. Pick your move, challenge the computer, and see who comes out on top!

> Read this in other languages: [Deutsch](README.de.md) · [فارسی](README.fa.md)

## Features

- Clean, minimal command-line interface
- Play against a randomized computer opponent
- Input validation (won't crash on invalid entries)
- Automatic replay on a draw
- Option to play again after each round

## How It Works

1. You're shown a numbered menu: `1. Rock`, `2. Paper`, `3. Scissors`
2. Enter the number of your choice
3. The computer picks randomly
4. The winner is announced based on classic Rock–Paper–Scissors rules
5. On a draw, the game automatically restarts the round
6. After a win or loss, you're asked if you'd like to play again

## Requirements

- Python 3.x (no external dependencies)

## Installation & Usage

Clone the repository:

```bash
git clone https://github.com/<your-username>/TriClash.git
cd TriClash
```

Run the game:

```bash
python game.py
```

### Windows

You can also double-click `run.bat` to launch the game.

## Project Structure

```
TriClash/
├── game.py       # Main game logic
├── run.bat       # Windows launcher script
├── README.md     # Language selector
├── README.en.md  # English documentation
├── README.de.md  # German documentation
├── README.fa.md  # Persian documentation
└── LICENSE       # MIT License
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues) or open a pull request.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
