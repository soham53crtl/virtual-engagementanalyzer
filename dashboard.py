import streamlit as st
from engagement_analyzer import calculate_engagement
from analytics_engine import EngagementAnalytics

st.set_page_config(
    page_title="Virtual Engagement Analyzer",
    layout="centered"
)

st.title("📊 Virtual Engagement Analyzer")
st.subheader("Engagement Intelligence Prototype")

analytics = EngagementAnalytics()

st.markdown("### Enter Session Details")

attendance = st.slider("Attendance Percentage", 0, 100, 75)
chat_messages = st.number_input("Number of Chat Messages", min_value=0, step=1)
reactions = st.number_input("Number of Reactions", min_value=0, step=1)

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
