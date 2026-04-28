# AnticrewAI - LinkedIn Lead Generator

A CrewAI-powered automated lead generation tool that finds LinkedIn posts from users looking for generative AI developers, providing actionable links for business outreach.

## Overview

This project uses CrewAI and Groq's LLM to automatically research and identify LinkedIn users who are actively seeking generative AI developers. It provides real-time links to relevant LinkedIn posts, making it a powerful tool for lead generation and business development.

## Features

- **Automated Research**: AI agent automatically searches for LinkedIn posts from users looking for generative AI developers
- **Groq Integration**: Uses Groq's fast LLM API (llama-3.3-70b-versatile) for efficient processing
- **Smart Filtering**: Focuses specifically on LinkedIn posts, not job listings
- **Real-time Results**: Provides current, actionable lead links

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd Anticrewai
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get a Groq API key from [Groq Console](https://console.groq.com/)

## Usage

### Method 1: Environment Variable
```bash
export GROQ_API_KEY="your-api-key-here"
python main.py
```

### Method 2: Command Line Argument
```bash
python main.py <GROQ_API_KEY>
```

## Configuration

- **LLM Model**: `llama-3.3-70b-versatile` (Groq)
- **Agent Role**: Strategist / Lead Generator
- **Task**: Find LinkedIn posts from users seeking generative AI developers

## Architecture

- **Agent**: Strategist - A powerful lead generator that searches for potential clients
- **Task**: Research and provide LinkedIn post links (not job listings)
- **LLM**: Groq's Llama 3.3 70B model for fast, accurate results

## Requirements

- Python 3.8+
- Groq API key
- See `requirements.txt` for Python dependencies

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key | Yes |

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.