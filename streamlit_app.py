import streamlit as st

st.set_page_config(page_title="Virtual Engagement Analyzer", layout="wide")

st.title("Virtual Engagement Analyzer")
st.write("This is a minimal deploy template. Replace with your real app later.")

attendance = st.slider("Attendance %", 0, 100, 75)
chat_messages = st.number_input("Chat messages", min_value=0, value=10)
reactions = st.number_input("Reactions", min_value=0, value=5)

if st.button("Calculate Engagement"):
    score = (attendance * 0.5) + (chat_messages * 0.3) + (reactions * 0.2)
    score = min(score, 100)
    st.metric("Engagement Score", round(score, 2))

    if score > 70:
        st.success("High Engagement")
    elif score > 40:
        st.warning("Moderate Engagement")
    else:
        st.error("Low Engagement")

    if chat_text.strip():
        polarity, label = analyze_sentiment(chat_text)
        st.markdown("### Sentiment Analysis")
        st.write("Sentiment:", label)
        st.write("Polarity Score:", round(polarity, 2))
