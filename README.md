# 🌟 TokenPulse Sentiment Agent

Real-time crypto sentiment analysis system with autonomous AI agents. Built with ❤️ by Mavens.

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Virtuals API Key (Get from [Virtuals Platform](https://console.game.virtuals.io/projects))
- Twitter Developer Account

### Installation
```bash
# Clone repository
git clone 
cd safe-sentiment-agent

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
```

## 🔧 Configuration
1. Get your Virtuals API key from their developer portal
2. Edit `.env` file:
```env
VIRTUALS_API_KEY="your_api_key_here"
TWITTER_USERNAME="your_twitter_handle"
TWITTER_PASSWORD="your_twitter_password"
```

## 🔐 Twitter Authentication
```bash
# Run Twitter authentication script (stores cookies in cookies.json)
python src/agents/twitter_auth.py
```

## 🖥️ Running the System

### Frontend Dashboard
```bash
streamlit run src/frontend/sentiment_dashboard.py
```

### Backend Agent
```bash
python src/agents/game_sentiment_agent.py --tokens solana,ethereum
```

## 📂 Project Structure
```
safe-sentiment-agent/
├── src/
│   ├── agents/            # Autonomous agent implementations
│   ├── frontend/          # Streamlit dashboard components
│   └── data/              # Analysis results and historical data
├── requirements.txt       # Python dependencies
└── .env.example           # Environment configuration template
```

## 📌 Dependencies Highlights
- **Core**: `transformers`, `torch`, `pandas`
- **Twitter**: `httpx`, `tweepy`
- **Frontend**: `streamlit`, `plotly`
- **Utils**: `python-dotenv`, `termcolor`

💡 **Tip**: Use `black` and `pylint` from requirements.txt for code formatting/linting!
](http://dorahacks.io/hackathon/build-and-brew/hackers)http://dorahacks.io/hackathon/build-and-brew/hackers
