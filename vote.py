import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Know Your Vote Limit",
    page_icon="🗳️",
    layout="centered"
)

# 2. Injecting Custom CSS for Background and Styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
        url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdEvSNJmcmbRaUTwUENBlDjAuQG4Up5R7H3g&s");
        background-size: cover;
        background-attachment: fixed;
    }
    
    /* Styling text to be white for visibility */
    .stMarkdown, label, p {
        color: white !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Making the input box look sleek */
    div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
    }
    
    h1 {
        color: #FFD700 !important; /* Gold Title */
        text-align: center;
        text-shadow: 2px 2px 4px #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. App Content
st.title("🗳️ Know Your Vote Limit")
st.write("Enter your details below to check your eligibility status.")

# Using a container to keep it organized
with st.container():
    age = st.number_input("Enter your current age:", min_value=0, max_value=110, value=0, step=1)
    
    st.markdown("---") # Visual divider

    if age == 0:
        st.info("Please enter your age to begin.")
    elif age >= 18:
        if age == 18:
            st.warning("You are exactly 18! You can vote, but ensure your Voter ID is ready.")
        else:
            st.success(f"You are {age} years old. You are fully eligible to vote!")
    else:
        years_left = 18 - age
        st.error(f"You are not eligible yet. You need to wait {years_left} more year(s).")

# 4. Footer
st.markdown("<br><p style='text-align: center; opacity: 0.8;'>Built with Python & Nishanth Team</p>", unsafe_allow_html=True)