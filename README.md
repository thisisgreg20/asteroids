# Asteroids Clone

A high-fidelity 2D arcade shooter built with Python and Pygame. Navigate your spaceship through a perilous asteroid field, using your laser to destroy obstacles before they destroy you.

## 🚀 Features

*   **Vector-Based Movement**: Smooth, physics-based rotation and acceleration for the spaceship.
*   **Dynamic Asteroid Splitting**: Large asteroids split into smaller, faster fragments when hit, increasing the challenge as you play.
*   **Collision Detection**: Precise circle-based collision math between shots, asteroids, and the player.
*   **Wrap-Around Screen**: Objects that move off one edge of the screen instantly reappear on the opposite side.

## 🛠️ Installation

Ensure you have **Python 3.8+** installed.

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com
    cd asteroids-clone
    ```

2.  **Install Dependencies**:
    This project requires the `pygame` library.
    ```bash
    pip install pygame
    ```

## 🎮 How to Play

To start the game, execute the main script from your terminal:
```bash
python main.py
```

### Controls
*   **W / S**: Move forward or backward.
*   **A / D**: Rotate the ship left or right.
*   **SPACE**: Fire your laser.
*   **R**: Reset your position if you get stuck.
*   **ESC**: Exit the game.

## 🧩 Gameplay Mechanics

### Asteroid Splitting
When a shot successfully collides with a medium or large asteroid, the original is destroyed and two smaller asteroids are spawned at its exact location. These new fragments fly off at random angles (between 20 and 50 degrees) relative to the parent's velocity and move 1.2x faster, making them harder to hit.

### Shooting
Pressing the spacebar creates a new instance of a `Shot` class at the player's center. Each projectile moves in the direction the ship is facing with a designated speed. If you experience issues with shots not spawning while moving, ensure your keyboard supports multiple simultaneous key presses (N-Key Rollover).

## 📜 License

This project is open-source and available under the **MIT License**.
