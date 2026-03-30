import streamlit as st
import time
import random

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="AI Academic Assistant Pro", page_icon="🎓", layout="wide")

# ------------------ SESSION STATE ------------------
if "level" not in st.session_state:
    st.session_state.level = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = []

if "submitted" not in st.session_state:
    st.session_state.submitted = False

# ------------------ HEADER ------------------
st.title("🎓 AI Academic Assistant Pro")
st.markdown("---")

# ------------------ SIDEBAR ------------------
with st.sidebar:
    st.header("📌 Project Details")
    name = st.text_input("Enter Your Name", placeholder="e.g., Manasa")
    subject = st.text_input("Enter Subject", placeholder="e.g., Cloud Computing")
    topic = st.text_input("Enter Topic", placeholder="e.g., Virtualization")
    difficulty = st.selectbox("Select Difficulty", ["Beginner", "Intermediate", "Advanced"])
    generate_btn = st.button("🚀 Generate Full Pack", use_container_width=True)

# ------------------ MAIN ------------------
if generate_btn and subject and topic:

    # 🔄 Loading Animation
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)
    progress.empty()

    st.success(f"🤖 AI Generated Content for '{topic}'")

    tab1, tab2, tab3 = st.tabs(["📘 Lesson Plan", "🎮 Quiz Game", "🏆 Leaderboard"])

    # ------------------ LESSON PLAN ------------------
    with tab1:
        st.subheader("📘 Lesson Plan")

        st.write(f"**Subject:** {subject}")
        st.write(f"**Topic:** {topic}")
        st.write(f"**Difficulty:** {difficulty}")

        st.markdown(f"""
### 🏫 Workflow
- Introduction to {topic}
- Core Concepts
- Applications in {subject}
- Summary
""")

    # ------------------ QUIZ GAME ------------------
    with tab2:
        st.subheader(f"🎮 Level {st.session_state.level} Quiz")
        st.info("⏱ Select answers and click SUBMIT")

        # LEVEL 1 QUESTIONS
        if st.session_state.level == 1:
            q1 = st.radio(
                f"Q1: What is {topic}?",
                [f"A concept in {subject}", "Not related", "Random idea"],
                key="q1"
            )

            q2 = st.radio(
                f"Q2: Why is {topic} important?",
                ["Improves efficiency", "No use", "Only theory"],
                key="q2"
            )

            q3 = st.radio(
                f"Q3: Where is {topic} used?",
                ["Real-world applications", "Nowhere", "Only exams"],
                key="q3"
            )

        # LEVEL 2 QUESTIONS
        else:
            q1 = st.radio(
                f"Q1: Advanced application of {topic}?",
                ["Scalable systems", "Not useful", "Random"],
                key="q1"
            )

            q2 = st.radio(
                f"Q2: Optimization improves?",
                ["Performance", "Nothing", "Complexity"],
                key="q2"
            )

            q3 = st.radio(
                f"Q3: Used in?",
                ["Industry systems", "Nowhere", "Old tech"],
                key="q3"
            )

        # ------------------ SUBMIT ------------------
        if st.button("🚀 Submit Quiz"):

            score = 0

            if st.session_state.level == 1:
                if st.session_state.q1 == f"A concept in {subject}":
                    score += 1
                if st.session_state.q2 == "Improves efficiency":
                    score += 1
                if st.session_state.q3 == "Real-world applications":
                    score += 1
            else:
                if st.session_state.q1 == "Scalable systems":
                    score += 1
                if st.session_state.q2 == "Performance":
                    score += 1
                if st.session_state.q3 == "Industry systems":
                    score += 1

            st.session_state.score = score
            st.session_state.submitted = True

            # RESULT
            st.progress(score / 3)
            st.markdown(f"## 🎯 Score: {score}/3")

            # BADGE SYSTEM
            if score == 3:
                st.balloons()
                st.success("🏆 GOLD BADGE - Academic Master")

                # LEVEL UNLOCK
                if st.session_state.level == 1:
                    st.session_state.level = 2
                    st.success("🎮 LEVEL 2 UNLOCKED!")

            elif score == 2:
                st.info("🥈 SILVER BADGE - Good")
            else:
                st.warning("🥉 BRONZE BADGE - Try again")

            # FACULTY NOTIFICATION
            st.info("📢 Faculty Notified")

            # LEADERBOARD ENTRY
            if name:
                st.session_state.leaderboard.append((name, score))

        # ------------------ RESET ------------------
        if st.button("🔄 Reset Quiz"):
            st.session_state.level = 1
            st.session_state.score = 0
            st.session_state.submitted = False

    # ------------------ LEADERBOARD ------------------
    with tab3:
        st.subheader("🏆 Leaderboard")

        if st.session_state.leaderboard:
            sorted_board = sorted(
                st.session_state.leaderboard,
                key=lambda x: x[1],
                reverse=True
            )

            for i, (player, sc) in enumerate(sorted_board, 1):
                st.write(f"{i}. {player} - {sc} points")
        else:
            st.info("No scores yet. Play quiz!")

else:
    st.info("Enter details and click Generate 🚀")