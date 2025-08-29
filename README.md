# Phase3-Monopoly-game 

A command-line implementation of **Monopoly** built with **Python**, **SQLAlchemy**, and **Rich** for styling.  
This version supports saving & resuming games, property purchases, rent, jail logic, chance/community chest cards, and player bankruptcy.

---

## 📦 Features
- 🎮 Supports **2–8 players**
- 🏦 Players start with **$1500**
- 🎲 Dice rolling with doubles detection
- 💵 Passing **GO** gives +$200
- 🚔 Jail logic:
  - Option to pay $50
  - Or get sent to jail
- 🏠 Property buying & rent payments
- 💳 Bankrupt players are eliminated
- 📜 Chance & Community Chest cards
- 💾 Persistent game state (resume saved games)
- ⏱️ Game runs with a **6000-second time limit** (configurable)

---

## ⚙️ Requirements

- Python **3.8+**
- Install dependencies:
  ```bash
  pip install sqlalchemy rich

## Project modules:

- engine.py → database engine

- tables.py → SQLAlchemy models (Player, Board, etc.)

- cards.py → chance/community chest logic

- property.py → property & rent handling


▶️ Running the Game

Run the main file:

python main.py


📂 Project Structure

monopoly-cli/
│── main.py             # Game entry point
│── engine.py           # Database engine setup
│── tables.py           # SQLAlchemy models (Player, Board, etc.)
│── cards.py            # Chance & Community Chest logic
│── property.py         # Property and rent handling
│── README.md           # Project documentation


🚀 Future Improvements

Add Free Parking rules

Implement trading between players

Add auctions for unbought properties

Smarter AI for computer players

Save & resume board state in more detail

# Publishers
Mathew Kariuki,William Kuria, Roy Moen, Justine Gichure and Brenda Njaramba.
