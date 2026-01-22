from engagement_analyzer import calculate_engagement
from analytics_engine import EngagementAnalytics

print("Virtual Engagement Analyzer – Intelligence Prototype\n")

analytics = EngagementAnalytics()

while True:
    attendance = float(input("Attendance percentage: "))
    chat_messages = int(input("Chat messages count: "))
    reactions = int(input("Reactions count: "))

    score = calculate_engagement(attendance, chat_messages, reactions)
    analytics.add_session_score(score)

    print("\nSession Engagement Score:", score)

    print("Average Engagement:", analytics.average_engagement())
    print("Engagement Trend:", analytics.engagement_trend())

    cont = input("\nAdd another session? (y/n): ")
    if cont.lower() != "y":
        break

