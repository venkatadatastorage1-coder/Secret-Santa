import streamlit as st
import time

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="🎅 Secret Santa Surprise",
    page_icon="🎁",
    layout="centered"
)

# --------------------------------------------------
# Session state
# --------------------------------------------------
if "reveal" not in st.session_state:
    st.session_state.reveal = False

# --------------------------------------------------
# Apply Dark Theme (CSS)
# --------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f0f0f;
        color: #f5f5f5;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #fcbf49;
    }

    div[data-testid="stMarkdownContainer"] {
        color: #f5f5f5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Title section
# --------------------------------------------------
st.markdown(
    "<h1 style='text-align: center;'>🎄 Secret Santa Surprise 🎄</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center;'>Someone has a little surprise just for you… 🎁</h3>",
    unsafe_allow_html=True
)

st.write("")
st.write("")

# --------------------------------------------------
# Centered Reveal Button
# --------------------------------------------------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎁 Reveal My Secret Santa Message"):
        st.session_state.reveal = True

# --------------------------------------------------
# Reveal Section
# --------------------------------------------------
if st.session_state.reveal:

    with st.spinner("Unwrapping your gift... 🎄✨"):
        time.sleep(2)

    st.balloons()
    st.snow()

    st.markdown("---")

    # Message card
    st.markdown(
        """
        <div style="
            background-color:#1a1a1a;
            padding:25px;
            border-radius:15px;
            border:2px dashed #f77f00;
            font-size:18px;
            color:#f5f5f5;
        ">
        <h2 style="text-align:center; color:#fcbf49;">🎅 Ho Ho Ho, Ankit! 🎅</h2>

        <p>
        This message comes wrapped with cheer, warmth, and a little mystery… ✨<br>
        Somewhere out there, a Secret Santa picked you and smiled.
        </p>

        <p>
        <b>“This Santa believes fewer surprises and more smiles make for a successful delivery.”</b> 🎅
        </p>

        <p>
        Since you recently joined the team, I may not have had the chance to know you well yet —
        but your preferences made this choice an easy one. Thank you for that.
        </p>

        <p>
        May this season bring you more joy, laughter, and success — and plenty of fun along the way! 🎄🎁
        </p>

        <p style="text-align:center; color:#eae2b7;">
        Keep smiling, keep shining ✨<br><br>
        <b>Cheers!</b><br>
        <b>Your Secret Santa 🎅</b>
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown(
        "<p style='text-align:center; color:#fcbf49;'>🎄 Merry Christmas 🎄</p>",
        unsafe_allow_html=True
    )
