import streamlit as st
from love_match import HerStandards, GuyProfile, BiblicalStandards, is_match, get_guy_profile

# standards for her
her_standards = HerStandards(
    age_range=(25, 35),
    interests=["music", "travel", "reading", "cooking", "hiking", "coding", "learning", "teaching"],
    occupation=["engineer", "doctor", "lawyer", "teacher", "Data Scientist", "Software Engineer"],
    education_level=["Bachelor's", "Master's", "PhD"],
    hobbies=["yoga", "painting", "cooking", "gym", "coding", "learning", "teaching"],
    biblical_standards=BiblicalStandards(
        righteousness=True,
        wisdom=True,
        faithfulness=True,
        love=True,
        patience=True,
        strength=True,
        kindness=True,
        gentleness=True,
        self_control=True,

    )
)

# st.title("Simisola Matchmaking For Hebrew Man")
st.title("MatchMaker For Her Hebrew Man")
st.header("Find out if you are a match for her")
st.subheader("Enter your profile below")


# Collect user data
with st.form("Guy Profile"):
    name = st.text_input("Enter your name")
    age = st.slider("Enter your age", 18, 100, 28)
    interests = st.text_input("Enter your interests separated by commas (e.g., music, travel)")
    occupation = st.text_input("Enter your occupation")
    education = st.text_input("Enter your highest level of education (e.g., Bachelor's, Master's, PhD)")
    hobbies = st.text_input("Enter your hobbies separated by commas (e.g., yoga, painting)")

    # Biblical attributes
    righteousness = st.checkbox("Are you righteous?")
    wisdom = st.checkbox("Are you wise?, like can you make good decisions?")
    faithfulness = st.checkbox("Are you faithful?")
    strength = st.checkbox("Are you strong?, like can you protect her?")
    love = st.checkbox("Are you loving?, will you love her?")
    patience = st.checkbox("Do you have patience?")
    kindness = st.checkbox("Are you kind?, like can you spend money on her?")
    gentleness = st.checkbox("Are you gentle?")
    self_control = st.checkbox("Do you have self control?")

    submitted = st.form_submit_button("Submit")

if submitted:
    biblical_attributes = BiblicalStandards(righteousness, wisdom, faithfulness, love, patience, strength, kindness,
                                            gentleness,
                                            self_control)
    guy = GuyProfile(name, age, interests.split(", "), occupation, education, hobbies.split(", "), biblical_attributes)

    # Finding match
    if is_match(guy, her_standards):
        st.success(f"{guy.name}, you are a match!, you can contact her on 08012345678")
    else:
        st.error(f"Sorry, {guy.name}, you are not a match, try again later.")

