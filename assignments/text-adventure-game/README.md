# 📘 Assignment: Text Adventure Game

## 🎯 Objective

Create a small text-based adventure game in Python where the player explores rooms, makes choices, and manages a simple inventory while practicing conditionals, loops, and dictionaries.

## 📝 Tasks

### 🛠️ Build the Game World

#### Description
Create the structure of a simple adventure game by defining rooms, descriptions, and possible player actions.

#### Requirements
Completed program should:

- Define at least three rooms or locations in the game
- Give each room a short description that is displayed to the player
- Allow the player to move between rooms using commands like `go north` or `go south`
- Store the game map in a dictionary or similar structured format

### 🛠️ Add Player Choices and Inventory

#### Description
Add the core interaction system so the player can make choices, collect items, and track progress.

#### Requirements
Completed program should:

- Ask the player for input using `input()`
- Support commands such as `look`, `inventory`, and `take item`
- Track items in a list or dictionary
- Prevent duplicate item collection or invalid actions
- Display the player's current inventory after meaningful actions

### 🛠️ Win or Lose Conditions

#### Description
Add the final gameplay logic so the game has a clear goal and ending state.

#### Requirements
Completed program should:

- Define a win condition such as collecting a key and reaching an exit
- Include a lose condition such as a limited number of wrong moves or a dead end
- Use loops to keep the game running until the player wins or loses
- Display a clear ending message when the game concludes
