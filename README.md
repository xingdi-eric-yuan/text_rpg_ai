## Golovin agent

source activate a python2 env.

Use `env.sh` to set environment.

Install frotz:
```
cd textplayer
cd frotz
make dumb
sudo make install_dumb
```

Install other dependencies:
```
pip install cython
pip install word2vec
pip install pyrsistent
pip install tensorflow
```

Run `massRuner.sh` to run agent on provided games.
