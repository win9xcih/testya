import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_story(name, language):
    """Generate a story using OpenAI API based on user inputs"""
    try:
        prompt = f"""
        Write a realistic and compelling short story in {language} about a crypto trader named {name}, chronicling their rise to millionaire status within the volatile and unpredictable world of the Solana ecosystem. 
        The story should focus on the trader's experience with memecoins, emphasizing both the emotional and financial struggles they faced, and the strategic, yet often risky, moves they made to build their fortune.
        Incorporate moments of failure and loss, such as a misguided investment in a hyped but ultimately worthless token or the devastating impact of a sudden market crash, and how {name} learned from these setbacks.
        Show how {name} navigated the chaos of the market, using advanced analytics, spotting hidden patterns, or taking calculated risks where others saw only panic. 
        Highlight the psychological toll of the highs and lows — the stress, the doubts, the moments of second-guessing — and how {name} developed resilience and mental clarity.
        Describe pivotal turning points, like when a seemingly overlooked low-cap token caught their eye just before it skyrocketed, or when they made a bold decision during a market collapse that defied conventional wisdom.
        Avoid glorifying the journey — make it authentic by depicting the ups and downs of trading, the sacrifices, and the tough decisions faced along the way.
        Use market-savvy language that reflects the complexity of the crypto world, offering insights into the strategic thinking and decision-making process of an experienced trader.
        """

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative story writer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating story: {str(e)}"


def main():
    st.set_page_config(
        page_title="AI Crypto Story Generator",
        page_icon="📚",
        layout="wide"
    )

    # Customizing the page with neon effect through HTML and CSS
    st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: white;
        font-family: 'Arial', sans-serif;
    }

    .title {
        font-size: 3em;
        color: #00ff99;
        text-align: center;
        text-shadow: 0 0 10px #00ff99, 0 0 20px #00ff99, 0 0 30px #00ff99;
    }

    .header {
        font-size: 1.5em;
        text-align: center;
        color: #ff66cc;
        text-shadow: 0 0 5px #ff66cc, 0 0 10px #ff66cc;
    }

    .button {
        background-color: #ff66cc;
        color: white;
        font-size: 1.2em;
        padding: 10px 30px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
        box-shadow: 0 0 10px #ff66cc, 0 0 20px #ff66cc;
        transition: 0.3s ease;
        margin: 20px auto;
        display: block;
    }

    .button:hover {
        background-color: #00ff99;
        box-shadow: 0 0 10px #00ff99, 0 0 20px #00ff99;
    }

    .story {
        font-size: 1.1em;
        line-height: 1.6;
        margin-top: 30px;
    }

    .instructions {
        color: #66ff66;
        font-size: 1.1em;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>Your story</div>", unsafe_allow_html=True)
    st.markdown("<div class='header'>A fun journey through the world of memecoins on Solana!</div>",
                unsafe_allow_html=True)

    # User inputs for name
    name = st.text_input("Enter your name:", placeholder="e.g., Alex")

    # User selects language for the story
    language = st.selectbox(
        "Select story language:",
        ["English", "Spanish", "French", "German", "Russian"]
    )

    # Ensure there's only one button
    if st.button("Generate Story ✨"):
        if name:
            with st.spinner("Creating your story... Please wait..."):
                story = generate_story(name, language)
                st.markdown("<div class='story'>### Your Story:</div>", unsafe_allow_html=True)
                st.write(story)
        else:
            st.warning("Please enter your name!")

    st.markdown("<div class='instructions'>### How to use:</div>", unsafe_allow_html=True)
    st.markdown("""
    1. Enter your name.
    2. Select your preferred language.
    3. Click 'Generate Story' and enjoy your crypto adventure!
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()