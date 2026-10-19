# discord-bot

a dumb little discord bot with fun commands. prefix is `!`.

## run it

```bash
pip install -r requirements.txt
cp .env.example .env        # then paste your bot token into .env
python3 bot.py
```

Get a token from the [Discord Developer Portal](https://discord.com/developers/applications):
create an application → Bot → reset/copy token. Enable the **Message Content Intent**
and **Server Members Intent** under the Bot settings, or the commands won't work.

## commands

| command | what |
|---------|------|
| `!ping` | pong + latency |
| `!roll 3d6+2` | roll dice |
| `!flip` | coin flip |
| `!8ball <q>` | magic 8 ball |
| `!choose a \| b \| c` | pick one |
| `!say <text>` | echo (deletes your msg) |
| `!avatar [@user]` | show avatar |
| `!userinfo [@user]` | user info |
| `!help` | list commands |

## notes

`.env` is gitignored — never commit your real token. If it leaks, reset it in the dev portal.
