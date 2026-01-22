import streamlit as st
from engagement_analyzer import calculate_engagement
from analytics_engine import EngagementAnalytics
from sentiment_analyzer import analyze_sentiment

st.set_page_config(
    page_title="Virtual Engagement Analyzer",
    layout="centered"
)

st.title("📊 Virtual Engagement Analyzer")
st.subheader("Engagement Intelligence Prototype")

# Initialize session state for analytics
if "analytics" not in st.session_state:
    st.session_state.analytics = EngagementAnalytics()

analytics = st.session_state.analytics

st.markdown("### Enter Session Details")

attendance = st.slider("Attendance Percentage", 0, 100, 75)
chat_messages = st.number_input("Number of Chat Messages", min_value=0, step=1)
reactions = st.number_input("Number of Reactions", min_value=0, step=1)

chat_text = st.text_area("Paste chat text (optional)")

if st.button("Analyze Engagement"):
    score = calculate_engagement(attendance, chat_messages, reactions)
    analytics.add_session_score(score)

    st.markdown("### Results")
    st.metric("Engagement Score", score)

    if score > 70:
        st.success("High Engagement")
    elif score > 40:
        st.warning("Moderate Engagement")
    else:
        st.error("Low Engagement")

    st.markdown("### Session Analytics")
    st.write("Average Engagement:", analytics.average_engagement())
    st.write("Engagement Trend:", analytics.engagement_trend())

    if chat_text.strip():
        polarity, label = analyze_sentiment(chat_text)
        st.markdown("### Sentiment Analysis")
        st.write("Sentiment:", label)
        st.write("Polarity Score:", round(polarity, 2))

st.markdown(
    """
Secrets: If your app needs secrets, add them in Streamlit Cloud under **Manage app → Settings → Secrets** and use `st.secrets["KEY"]`.
Run locally: `streamlit run streamlit_app.py`
"""
)