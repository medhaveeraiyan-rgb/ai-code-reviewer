import streamlit as st
from streamlit_ace import st_ace
from reviewer import review_code

st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🔍",
    layout="wide"
)

st.title("AI Code Reviewer")
st.write("Paste your code below and get instant feedback from AI.")

col1, col2 = st.columns(2)

with col1:
    language = st.selectbox(
        "Select programming language",
        ["Python", "JavaScript", "Java",
         "C++", "C#", "Go", "Ruby", "Other"]
    )

    st.subheader("Your code")
    code_input = st_ace(
        language=language.lower(),
        theme="monokai",
        height=400,
        placeholder="Paste your code here..."
    )

    review_btn = st.button("Review my code", type="primary")

with col2:
    st.subheader("Review results")
    if review_btn:
        if not code_input or len(code_input.strip()) == 0:
            st.warning("Please paste some code first.")
        else:
            with st.spinner("Claude is reviewing your code..."):
                result = review_code(code_input, language)
            st.success("Review complete!")
            st.markdown(result)
    else:
        st.info("Your review will appear here after you click the button.")