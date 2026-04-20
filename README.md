# DotaDiscBot

> ⚠️ **Discontinued** - The DPC system was removed by Valve. The bot no longer functions as the underlying data source (Liquipedia DPC standings/matches) no longer exists in the same form.

A Discord bot that provided real time **Dota 2 DPC match information** - countdown timers to upcoming matches, live match listings, and DPC regional standings sourced from Liquipedia.

---

## Commands

| Command | Description |
|---------|-------------|
| `$nm <number>` | List the next N upcoming/ongoing matches |
| `$nm <team name>` | Countdown to a specific team's next match |
| `$table <region> <upper/lower>` | DPC division standings for a region |
| `$help` | List all commands |

**Regions:** `CIS` · `CN` · `EU` · `NA` · `SA` · `SEA`

> **Note:** Team names must match Liquipedia's naming — e.g. `SG e-sports` works, `SG` doesn't. Try the full name if you get no response.

---

## About

Built for Dota 2 communities that wanted match info without leaving Discord. Checking Liquipedia mid game is annoying, this bot fixed that. It parsed Liquipedia's API to return live DPC standings and schedules with a simple command syntax anyone could use.

---

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/Raffiesaurus/DotaDiscBot.git
   cd DotaDiscBot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your bot token to a `.env` file:
```
DISCORD_TOKEN=your_bot_token_here
```

4. Run:
```bash
python Code/main.py
```

---

## Tech

- **Language:** Python
- **Library:** discord.py
- **Data source:** Liquipedia API
- **Deployment:** Heroku (Procfile included)

---

## License

MIT
