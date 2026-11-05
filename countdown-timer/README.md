# ⏳ Python Countdown Timer

A simple command-line countdown timer built using Python. The project allows users to set a custom countdown duration in hours, minutes, and seconds. Once the countdown is complete, an alarm sound plays continuously until the user manually stops it.

## ✨ Features

- Set a custom timer using hours, minutes, and seconds.
- Play background audio while the countdown is running.
- Automatically trigger an alarm when the timer reaches zero.
- Continuously repeat the alarm until manually stopped.
- Stop the alarm using `CTRL + C`.
- Simple and interactive command-line interface.

## 🛠️ Technologies Used

- **Python** – Core programming language.
- **Time Module** – Handles countdown delays.
- **Pygame** – Used for audio playback and sound management.

## 📁 Project Structure

```text
countdown-timer/
│
├── main.py
├── audio.mp3
├── audio2.mp3
└── README.md
```

| File | Description |
|---|---|
| `main.py` | Main Python program |
| `audio.mp3` | Audio played during the countdown |
| `audio2.mp3` | Alarm played when the timer ends |
| `README.md` | Project documentation |

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vanshairi/python-mini-projects.git
```

### 2. Navigate to the Project Directory

```bash
cd python-mini-projects/countdown-timer
```

### 3. Install Pygame

```bash
pip install pygame
```

Alternatively, on Linux:

```bash
python3 -m pip install pygame
```

### 4. Run the Program

```bash
python3 main.py
```

**Note:** Make sure `audio.mp3` and `audio2.mp3` are present in the same directory as `main.py`.

## ▶️ How It Works

1. The program initializes the Pygame mixer.
2. The user enters the desired countdown duration.
3. The entered hours, minutes, and seconds are converted into total seconds.
4. The first audio file starts playing while the program waits for the specified duration.
5. Once the countdown finishes, the program displays `TIME'S UP!`.
6. The countdown audio stops, and the alarm sound starts playing continuously.
7. The user can stop the alarm by pressing `CTRL + C`.

## 📸 Sample Output

```text
Welcome to Countdown Timer
Enter the time:-

Enter hours : 0
Enter minutes : 0
Enter seconds : 10

TIME'S UP!
Press CTRL + C to Stop

Timer stopped.
```

## 📚 Concepts Practiced

Through this project, I practiced:

- Python modules and imports.
- User input and type conversion.
- Arithmetic operations and time calculations.
- Working with external Python libraries.
- Audio playback using Pygame.
- Infinite loops and exception handling.
- Handling keyboard interrupts using `KeyboardInterrupt`.

## 🚀 Future Improvements

- Add a graphical user interface (GUI).
- Display a live countdown instead of waiting silently.
- Add pause and resume functionality.
- Allow users to select custom alarm sounds.
- Add input validation for negative or invalid time values.

---

**Part of my Python learning journey — learning by building, experimenting, and improving. 🐍**