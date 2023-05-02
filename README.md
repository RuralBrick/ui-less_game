# NUI
Welcome to No User Interface. To play, simply double-click on `play_game_on_<your OS>`. This game is intended to be played on a [shell](https://en.wikipedia.org/wiki/Shell_(computing)), so Command Prompt, Terminal, or some other black box with white text on it should pop up (and stay up) when you click on your respective `play_game...` file. If the game does not start or you get some other error, please first try installing the latest version of Python [https://www.python.org/downloads/](https://www.python.org/downloads/) and rerunning your `play_game...` file. If the game still does not start, please try some of the troubleshooting tips below.

## Windows

First, open the folder you downloaded the game into in File Explorer (you should see `play_game` here).

At the top left of File Explorer, click on File, then Open Windows PowerShell (a blue window should pop up). Copy the line below:
```
python .\play_game.py
```
Paste it into the blue window, and press `[enter]`.

## MacOS

A copy of the Mac installer for the appropriate version of Python is located in the `macos/` folder. Please run this `.pkg` file and then try running `play_game_on_macos` again.

## Debian and Ubuntu

Install the approprate version of Python by opening a terminal and running
```
sudo apt install python3.10
```

After installation, please try running `play_game_on_linux` again.
