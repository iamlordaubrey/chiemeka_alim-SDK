# Lord Of The Rings SDK

Description: An SDK that makes it easy for developers to consume information about the Lord of The Rings trilogy.

SDK builds on an existing Lord of The Rings API


### Tech Stack
Built using Python 3.10.5 (see `.python-version` file). External libraries are kept as minimal as possible 
(see `requirements.in` file)


## Install
Creates a fresh virtual environment (called .venv) and installs requirements
```commandline
make setup
```


Install pip requirements / Sync requirements.in with requirements.txt
```commandline
make pip_sync
```


### Run tests
```commandline
make runtest
```
