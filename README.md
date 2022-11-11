# NFM-Control
Controls the NetzFrequenz (Messung) on the basis of statistical values and manages a Telegram Bot to inform subscribed users about critical developments

## Get started

1. Clone repository
2. Install InfluxDB ([Download InfluxDB](https://docs.influxdata.com/influxdb/v2.5/install/))
3. Start InfluxDB Daemon
4. Run the `main.py`

## Interact

### CL (Command Line)
- via make and Makefile
  - windows:
    - install [chocolatey](https://chocolatey.org/)
    - install make (`choco install make`)
    - See [here](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows)
  - usage:
    - `make "command"` where "command" can be any command in the `Makefile`
- via pipenv scripts
  - run `pipenv run "script"` where script can be any listed script in the `Pipfile`
- via the custom cli
  - enter virtual environment via `pipenv shell`
  - run `python cli.py "command"` where "command" is any decorated function in the `cli.py` file 


## File info and directory structure
- ### app
  - Contains the app logic
- ### tests
  - Contains the test logic
- #### .env
  - .env file declaring important environment variables
- #### build.sh
  - Build script to initialize the application (create virtual environment, install dependencies, install database) after cloning
- #### cli.py
  - Exposes a cli written in python to control the application
- #### config.toml
  - Contains configuration details and credentials regarding the whole application
- #### Makefile
  - Contains executable commands that can be triggered from the command line
- #### run.sh
  - Starts the application
