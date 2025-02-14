"""Initialize the agents package."""

from .sentiment_agent import SentimentAgent

# Create singleton instance
sentiment_agent = SentimentAgent()

__all__ = ["sentiment_agent", "SentimentAgent"]
