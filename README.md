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


Based on the provided Reddit posts and comments, I've generated a detailed User Persona:

**Name:** TechNomad (a creative nickname based on the user's interest in technology and frequent references to New York City)

**Age group:** 25-35 years old (based on the user's references to being an iOS developer, their interest in spatial computing, and their familiarity with current events and technologies)

**Occupation:** Software Developer/Engineer (likely working in the tech industry, possibly as an iOS developer or in a related field, given their questions about spatial computing and AR technology)

**Personality traits:**

* Tech-savvy and curious, with a strong interest in emerging technologies like spatial computing and AR
* Analytical and problem-solving, as evidenced by their comments on game development and strategy
* Possibly introverted or preferring smaller social circles, given their discomfort with large crowds and noisy environments (e.g., the "intern season" post)
* Values sustainability and social responsibility, as seen in their post about ESG ratings and individual impact on the environment

**Interests:**

* Technology and innovation (spatial computing, AR, AI, etc.)
* Gaming ( strategy games, Pokémon, etc.)
* Music and dance ( referenced in the "intern season" post)
* Food and drink ( mentions of specific restaurants and coffee shops)
* Travel and exploration ( references to different cities and neighborhoods)
* Social and environmental issues (ESG ratings, sustainability, etc.)

**Goals or motivations:**

* To stay up-to-date with the latest technologies and innovations
* To find ways to apply technology to real-world problems and improve sustainability
* To connect with like-minded individuals and share knowledge and experiences
* To balance personal and professional life, with a focus on self-care and mental well-being

**Pain points / frustrations:**

* Feeling overwhelmed by large crowds and noisy environments
* Difficulty finding reliable and trustworthy sources of information on emerging technologies
* Concerns about the environmental and social impact of technological advancements
* Frustration with the lack of innovation and progress in certain areas (e.g., NFTs)

**Top subreddits:**

* r/iOSProgramming
* r/SpatialComputing
* r/Gaming
* r/Sustainability
* r/NewYorkCity

**Sample quotes:**

* "I feel violated by intern season" (from the post about feeling out of place in a crowded bar)
* "I'm an iOS developer building in visionOS. Do people have recommendations on resources to catch up on new featuresets for spacial computing?" (from the post about spatial computing resources)
* "I think individuals should be aware of our own ESG rating" (from the post about ESG ratings and sustainability)

**Citations from original text:**

* "I feel violated by intern season" (Title: I feel violated by intern season)
* "I'm an iOS developer building in visionOS. Do people have recommendations on resources to catch up on new featuresets for spacial computing?" (Title: Best blogs, tutorial channels to learn)
* "I think individuals should be aware of our own ESG rating" (Title: Tracking our individual impacts on the world through ESG ratings)
