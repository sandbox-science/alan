## Matrix Bot

Library used: https://github.com/Code-Society-Lab/matrixpy

## Requirements
> [!IMPORTANT]
>
> Don't skip this step, as it is crucial for the bot to work properly.

- Python 3.10 or higher
- [Matrix account](https://app.element.io/#/register) (create a new account for the bot).
- Create a `config.yaml` file in the `config/` directory with the following structure:
```yaml
CLIENT: "https://matrix.org"
USERNAME: "@username:matrix.org" # replace with the bot's username
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
