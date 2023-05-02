#!/bin/bash

if [[ "$(python --version 2>/dev/null)" == "Python 3.10"* ]]
then
    python ./play_game.py
elif [[ "$(python3 --version 2>/dev/null)" == "Python 3.10"* ]]
then
    python3 ./play_game.py
elif [[ "$(python3.10 --version 2>/dev/null)" == "Python 3.10"* ]]
then
    python3.10 ./play_game.py
else
    echo "Please install Python 3.10 and add it to your PATH"
fi
