for game in `ls textplayer/games`
do
  python golovinRunner.py $game --quiet
done
