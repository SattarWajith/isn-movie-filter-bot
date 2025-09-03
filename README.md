# Movie/Auto Filter Telegram Bot

A fully modular Telegram bot for movie searching, filtering, indexing, and much more!  
Features: Multi-database support, admin controls, stats, broadcast, auto-indexing, AI-powered recommendations, anti-spam, logging, movie requests, and many more (see `config.py`).

## Features
- Toggle all features via `config.py`
- Add or remove modules easily
- Modular: `/features`, `/database`, `/utils`

## Setup

1. Clone/download this repo.
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Edit `config.py` with your credentials (Telegram API, DB, etc).
4. Run the bot:
   ```
   python main.py
   ```

## How to add more features
- Add your code to `/features/` and link in `config.py`.

## How to upload to GitHub

1. Create a new repo on https://github.com
2. In your bot folder, run:
   ```
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git branch -M main
   git push -u origin main
   ```

## Contribution
- PRs, issues, and new features are welcome!