# DotaDiscBot

> ⚠️ **Discontinued** — The DPC system was removed by Valve. The bot no longer functions as the underlying data source (Liquipedia DPC standings/matches) no longer exists in the same form.

A Discord bot that provided real-time **Dota 2 DPC match information** — countdown timers to upcoming matches, ongoing match listings, and DPC regional table standings — sourced from the Liquipedia API.

## About

Built for Dota 2 communities that wanted match info without leaving Discord. The bot scraped and parsed Liquipedia's API to return live DPC standings and match schedules, with a simple command syntax so anyone in the server could query it.

This was a personal side project driven by actually wanting the thing to exist — checking Liquipedia mid-game is annoying.

## Commands

| Command | Description |
|---|---|
| `$nm <number>` | Returns the next N upcoming/ongoing matches |
| `$nm <team name>` | Returns the next match + countdown for a specific team |
| `$table <region> <upper/lower>` | Returns the DPC division table for a region |
| `$help` | Lists all commands |

**Regions:** CIS, CN, EU, NA, SA, SEA

> **Note:** Some team names have quirks due to Liquipedia’s API — e.g. `SG e-sports` works, `SG` doesn’t. Try variations if you get no response.

## Tech

- **Language:** Python
- **Library:** discord.py
- **Data source:** Liquipedia API

## License

MIT
