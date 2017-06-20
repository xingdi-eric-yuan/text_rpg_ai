mkdir diggedCommands
rm diggedCommands.txt
for game in `ls commands`
do
  echo $game
  timeout 60s python commandsDigger.py commands/$game items/$game diggedCommands/$game.commands
done
for game in `ls commands`
do
  cat diggedCommands/$game.commands >>diggedCommands.txt
done