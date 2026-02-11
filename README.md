# Snake Game - Optimized Python Edition

A classic arcade-style Snake game built using Python's built-in `turtle` graphics module. This project features optimized movement logic, a score tracking system, and increasing difficulty.

##  Features
* **Smooth Controls:** Play using either 'W-A-S-D' keys or the standard Arrow keys.
* **Dynamic Difficulty:** The game speed increases slightly as the snake grows longer.
* **High Score Tracking:** Keeps track of your best performance during the session.
* **Collision Detection:** Includes logic for wall collisions and self-collision.

##  Installation & Usage

### Prerequisites
* Python 3.x installed on your system.
* The `turtle` module (included in the Python Standard Library, so no extra installation is needed).

### How to Run
1. Clone this repository or download the `snake_game.py` file.
2. Open your terminal or command prompt.
3. Navigate to the folder containing the file.
4. Run the following command:
   ```bash
   
   ##  Recent Improvements
Compared to the initial version, this updated build includes:
* **Optimized Rendering:** Refined `wn.update()` calls to reduce input lag.
* **Direction Lock:** Added logic to prevent the snake from reversing directly into itself (e.g., you can't go 'Down' while moving 'Up').
* **Speed Scaling:** Adjusted the `delay` logic so the game gets progressively more challenging.
