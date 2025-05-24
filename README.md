## Matrix Bot

Library used: https://pypi.org/project/simplematrixbotlib/

## Requirements
- Python 3.11 or higher
- pip install -r requirements.txt
- Create a `config.yaml` file in the root directory with the following structure:
```yaml
CLIENT: "https://matrix.org"
USERNAME: "@username:matrix.org" # replace with the bot's username
PREFIX: "!"
PASSWORD: "password" # replace with the bot's password
```

## Usage
First, activate the virtual environment:
```bash
python -m venv venv      # create a virtual environment
source venv/bin/activate # activate the virtual environment
```

Then, run the following command to install and start the bot:
```bash
pip install -e .
alan start
``` 
Invite the bot to a room and type the command you want to execute.
- The bot will respond to commands prefixed with `!` and will also respond to some messages without the prefix.
- The bot will respond to the following commands:
  - `!hello`: Responds with "Hello, world!".
  - `!echo <message>`: Echoes back the message.
  - `hello`: Responds with a waving hand emoji "👋".
  - `!ping`: Responds with "Pong!".
