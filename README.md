# Reddit User Persona Generator 🤖

Scrapes a Reddit user’s posts & comments and generates a detailed user persona using Together AI's LLaMA 3 model.

## Features
- Uses `praw` to fetch Reddit data
- Streams responses from Together AI (OpenAI-compatible)
- Outputs structured persona analysis
- Saves results in `outputs/`

## Setup

1. Clone repo
2. Create `.env` with:
    ```
    TOGETHER_API_KEY=your_key
    REDDIT_CLIENT_ID=your_client_id
    REDDIT_CLIENT_SECRET=your_client_secret
    REDDIT_USER_AGENT=your_user_agent
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run:
    ```
    python hu.py
    ```

## Example Output

Saved in `outputs/{username}_persona.txt`
