import streamlit as st
import os

# Simple password protection
def check_password():
    password = st.text_input("Enter the password:", type="password")
    if password == "kammo":  # Change this to your actual password
        return True
    else:
        st.warning("mein aapko kya bulaata hoon?")
        return False

if not check_password():
    st.stop()  # Stop the app if the password is wrong

# Custom CSS to set background image
st.markdown(
    """
    <style>
    body {
        background-image: url('https://img.freepik.com/free-vector/blurred-valentine-s-day-wallpaper_23-2148819570.jpg');
        background-size: cover;  /* Adjust to cover the entire background */
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Embed Spotify music player starting at 0:47
st.markdown(
    """
    <iframe src="https://open.spotify.com/embed/track/5iFwAOB2TFkPJk8sMlxP8g?autoplay=1&start=47" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
    """, unsafe_allow_html=True
)

# Title
st.title("Our Journey Together ❤🌻")

# Home Page
st.header("Happy 2 Months Kammo! ❤️😘😘")

# Timeline Section
st.header("Timeline of Our Moments 💖")

timeline_data = {
    "Date": ["2024-01-11", "2024-01-19", "2024-01-20", "2024-08-06"],
    "Event": ["First Hug in 2024", "First Kiss 💋 (4:17 PM)", "First Time We Held Hands", "We Started Dating (5:47 PM)"],
}
for date, event in zip(timeline_data["Date"], timeline_data["Event"]):
    st.write(f"**{date}:** {event}")

# Future Section
st.header("Future Adventures ✨🌄")
future_plans = ["Visiting a Hill Station 🏔️", "Aquarium 🐠", "Planetarium 🌌", "Concert 🎶", "Mountains 🏞️"]
for plan in future_plans:
    st.write(f"- {plan}")

# Gallery Section: Displaying images from the specified folder
st.header("Our Gallery 💞")
image_folder = r"output"  # Use raw string to avoid escape characters

# List all image files in the folder
if os.path.exists(image_folder):
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    # Create columns to display images side by side
    cols = st.columns(6)  # Create 6 columns
    for i, image_file in enumerate(image_files):
        if i < 6:  # Limit to 6 images
            image_path = os.path.join(image_folder, image_file)
            cols[i].image(image_path, use_column_width='auto', width=200)  # Set width for smaller size
else:
    st.error("Image folder does not exist!")

# Romantic Message Section
st.header("A Sweet Note for You 💖")
romantic_message = """
*“In a sea of people, my eyes will always search for you.”* 🌹
  
*“You are my sun, my moon, and all my stars.”* ✨
  
Every moment spent with you is a beautiful memory in the making. I can't wait for all the adventures that lie ahead, hand in hand, heart to heart. You're my everything, Kammo. 💞
"""
st.write(romantic_message)

# Messages Section
st.header("Messages for You 💌")
my_message = """ Happy 2 months, my beautiful Kammo! 🌻💖 I still can't believe it's been two whole months since this incredible adventure with you began. Every moment we've shared feels like a dream, and I am beyond grateful to have you in my life. You make me feel alive in ways I never knew were possible. Being with you is pure magic.

From the bottom of my heart, thank you for creating a space where I can be my truest self. With you, I feel safe, heard, and understood—like I can tell you anything without fear. I know I haven’t always been perfect, and there have been times I let you down, but I want you to know that I’m learning, growing, and trying to become the best version of myself for *us*. I’m sorry for any hurt I’ve caused, and I’m committed to being the kind of partner you deserve—because you deserve the world.

I can't wrap my head around why you’d ever feel insecure because to me, you’re flawless. You're not just beautiful—you’re stunning. Your hair? Oh, Kammo, it’s always so perfect, and I love the way it shines, framing your face like it’s meant to be in a painting. Those brown eyes of yours—they're filled with warmth and kindness, and they see right into my soul. Every time I see your smile, it feels like the sun is rising just for me, and I swear my heart races every single time.

And your lips? Perfect. Every moment we’ve shared together feels like a blessing, and I cherish every hug, every kiss, every laugh. You’ve got this irresistible charm that’s not just in your looks but in your heart. Your kindness is so rare, Kammo—it’s like you light up the world just by being in it. I love the way you care for others, with such compassion and warmth. It’s one of the many things that make you so special to me.

There’s no one like you, Kammo. You’re the most amazing woman I’ve ever had the joy of loving—next to my mom, of course. The past two months have been filled with memories I’ll hold close forever, and I can’t wait to make more with you. You inspire me every day to be better, to love harder, and to never take a single second with you for granted.

Here’s to us and the future we’re building together. I love you with all my heart, Kammo. And I’ll keep loving you deeper and deeper, reminding you every day just how incredible, beautiful, and absolutely perfect you are. You're my everything, always and forever. 💖✨
"""
st.write(my_message)
