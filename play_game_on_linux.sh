#!/bin/bash

pattern='Python 3\.[1-9][0-9].*'

if [[ "$(python --version 2>/dev/null)" =~ $pattern ]]
then
    python ./play_game.py
elif [[ "$(python3 --version 2>/dev/null)" =~ $pattern ]]
then
    python3 ./play_game.py
elif [[ "$(python3.10 --version 2>/dev/null)" =~ $pattern ]]
then
    python3.10 ./play_game.py
else
    echo "Please install Python version 3.10 or later and add it to your PATH"
    read
fi
