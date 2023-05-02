& "$($ENV:LOCALAPPDATA)\Programs\Python\Python310\python.exe" -m PyInstaller .\play_game.spec
butler push .\dist\play_game ruralbrick/nui:win
