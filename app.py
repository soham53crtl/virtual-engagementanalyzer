from engagement_analyzer import calculate_engagement

print("Virtual Engagement Analyzer - Prototype")

attendance = float(input("Enter attendance percentage: "))
chat_messages = int(input("Enter number of chat messages: "))
reactions = int(input("Enter number of reactions: "))

score = calculate_engagement(attendance, chat_messages, reactions)

print("\nEngagement Score:", score)

if score > 70:
    print("Engagement Level: High")
elif score > 40:
    print("Engagement Level: Moderate")
else:
    print("Engagement Level: Low")
