# Axel Feet Feed 👣

A Discord-powered website that shows a live gallery of images posted in a specific channel (e.g., Axel's feet pics).

## 🛠️ Project Setup

### Discord Bot
1. Install dependencies:
   ```
   cd bot
   pip install -r requirements.txt
   ```
2. Create a `.env` file with your bot token:
   ```
   DISCORD_BOT_TOKEN=your-token-here
   ```
3. Run the bot:
   ```
   python bot.py
   ```

### Flask Backend
1. Install dependencies:
   ```
   cd backend
   pip install -r requirements.txt
   ```
2. Run the server:
   ```
   python app.py
   ```

### Frontend
Just open `frontend/index.html` in your browser.

## 🌐 Hosting

You can host:
- **Backend** on Render/Railway
- **Frontend** on Vercel/Netlify
- **Bot** on Replit, Render, or local machine

## License
MIT
