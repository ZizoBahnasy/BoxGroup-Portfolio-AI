# BoxGroup Portfolio AI: OpenAI's Realtime API + LiveKit Integration

BoxGroup Portfolio AI is a voice agent that combines web scraping, LLM analysis, and real-time voice interaction to analyze BoxGroup's investment portfolio. Using OpenAI's language models and LiveKit's real-time communication infrastructure, it provides deep insights into portfolio companies, market trends, and investment patterns. Users can explore investment styles, company defensibility, fundraising activities, and portfolio comparisons through natural conversation.

This is a local development project. Follow the setup guide below to run your own instance.

You can find a demo of the final product [here](https://youtu.be/yh4HXIG3CqU).

## Features

- Automated portfolio company extraction and analysis
- Real-time AI-powered portfolio insights
- Interactive voice and text interface for portfolio exploration
- Deep analysis of company defensibility and market positioning
- Comprehensive industry categorization and trend analysis
- Real-time fundraising and valuation tracking from news sources
- Comparative portfolio analysis

## Repository Structure

### /agent
Contains the LiveKit Python Agents implementation.

### /web
Houses the Next.js web frontend.

### /data
Stores generated portfolio data files:
- portfolio_1_extracted.json : Initial company data
- portfolio_2_enriched.json : Enriched company information
- portfolio_3_analyzed.json : AI analysis results
- portfolio_4_valuations.json : Final data with fundraising information

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- LiveKit Cloud or self-hosted LiveKit server
- OpenAI API key
- pnpm (for web frontend)
- Node.js and npm (for news scraping)

## Complete Setup Guide

### 1. Initial Setup
```bash
# Clone the repository
git clone https://github.com/ZizoBahnasy/BoxGroup-Portfolio-AI.git
cd BoxGroup-Portfolio-AI

# Install pnpm (if not already installed)
npm install -g pnpm

# Install Python dependencies
pip3 install -r requirements.txt

# Install Node.js dependencies
pnpm install google-news-scraper
```

### 2. Portfolio Data Generation
```bash
# Install dependencies
pip3 install -r requirements.txt

# Generate all portfolio data
python3 scripts/script_1_run.py
```

### 3. Agent Setup
```bash
# Navigate to agent directory
cd agent

# Set up Python virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Configure agent (this file is git-ignored for security)
cp .env.sample .env

```
Add to your `.env`:

```python
OPENAI_API_KEY=your_key_here
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
```

# Install agent dependencies
```bash
pip3 install -r requirements.txt
```

# Start the agent
```bash
python3 main.py dev
```

### 4. Web Frontend Setup
```bash
# Navigate to web directory
cd web

# Configure frontend (this file is git-ignored for security)
cp .env.sample .env.local

# Install dependencies
pnpm install

# Start development server
pnpm dev
```

Visit [http://localhost:3000](http://localhost:3000) to access the interface.

## Usage

With all components running, you can engage in natural conversations about the portfolio. Example queries:

Investment Analysis:
- "Which companies align best with BoxGroup's investment style?"
- "Can you tell me about three deep tech companies in our portfolio that have a consumer focus that we're very excited about?"
- "Can you tell me which three companies in our portfolio have the highest capital intensity and also give me a very brief description of what they do and their defensibility?"
- "Please identify the 5 companies that are least compatible or aligned with the BoxGroup investment style but which have an excitement score of 7 or greater."

Company Deep Dives:
- "Tell me about Atom Computing's defensibility and barriers to entry."
- "What is Ramp's most recent valuation?"
- "Which companies have the highest capital intensity?"

Portfolio Insights:
- "Which biotech companies raised the most money in the last 2 years?"
- "Could you please give me the three most recent news articles about Plaid? Don’t read the URLs."

Note: it's helpful to guide the speaking style of the agent by saying things like "In very brief, natural speech..." or add "in brief terms" as the agent defaults to returning all available information for whatever field you're asking about.

## Deployment

- Agent: See [Deployment & Scaling Guide](https://docs.livekit.io/agents/deployment/)
- Frontend: Deploy using Next.js hosting solutions like [Vercel](https://vercel.com/)

## Troubleshooting

Verify that:
1. All environment files are properly configured
2. Portfolio data generation completed successfully
3. Agent is running and connected
4. Web server is active
5. Python 3.9+ and pnpm are installed correctly

## Additional Resources

For more information, visit [LiveKit docs](https://docs.livekit.io/).

## License

Apache 2.0
```