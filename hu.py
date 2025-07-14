import os
import praw
from openai import OpenAI
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# Set up Reddit client
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT")
)

# Initialize Together client
client = OpenAI(
    base_url="https://api.together.xyz/v1",
    api_key=TOGETHER_API_KEY
)

# Fetch Reddit user data
def fetch_user_data(username, post_limit=20, comment_limit=50):
    redditor = reddit.redditor(username)
    posts, comments = [], []

    try:
        for submission in redditor.submissions.new(limit=post_limit):
            posts.append(f"Title: {submission.title}\nText: {submission.selftext}")

        for comment in redditor.comments.new(limit=comment_limit):
            comments.append(f"Comment: {comment.body}")

    except Exception as e:
        print(f"Error fetching data for {username}: {e}")

    return posts, comments

# Create a prompt and stream LLM response
def generate_persona(username, posts, comments):
    user_data = "\n\n".join(posts + comments)

    prompt = f"""
You're an expert analyst. Based on the Reddit posts and comments below, generate a detailed User Persona.

Persona should include:
- Name (creative nickname based on username)
- Age group
- Occupation (guess if possible)
- Personality traits
- Interests
- Goals or motivations
- Pain points / frustrations
- Top subreddits
- Sample quotes (from their posts/comments)
- Citations from original text

Reddit Data:
{user_data}
"""

    stream = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
        temperature=0.7,
        max_tokens=1024
    )

    os.makedirs("outputs", exist_ok=True)
    output_file = f"outputs/{username}_persona.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for chunk in stream:
            text = chunk.choices[0].delta.content or ""
            print(text, end="", flush=True)
            f.write(text)
    print(f"\n\n✅ Persona saved to {output_file}")

# Main entry point
if __name__ == "__main__":
    url = input("Enter Reddit profile URL (e.g., https://www.reddit.com/user/spez): ").strip()
    if "/user/" in url:
        username = url.split("/user/")[1].strip("/").split("/")[0]
        posts, comments = fetch_user_data(username)
        if posts or comments:
            generate_persona(username, posts, comments)
        else:
            print("No data found.")
    else:
        print("❌ Invalid Reddit profile URL.")
