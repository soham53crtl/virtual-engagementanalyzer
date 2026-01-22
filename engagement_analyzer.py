"""
Engagement Calculator
----------------------
Calculates engagement scores based on attendance, chat activity, and reactions.
"""


def calculate_engagement(attendance: float, chat_messages: int, reactions: int) -> float:
    """
    Calculates engagement score based on:
    - Attendance percentage (0-100)
    - Chat messages count
    - Reactions count
    
    Returns a score between 0-100.
    """
    # Normalize inputs
    attendance_weight = min(attendance, 100) * 0.4
    
    # Normalize chat messages (assume 50+ messages is maximum engagement)
    chat_weight = min(chat_messages / 50, 1) * 40
    
    # Normalize reactions (assume 30+ reactions is maximum engagement)
    reactions_weight = min(reactions / 30, 1) * 20
    
    engagement_score = attendance_weight + chat_weight + reactions_weight
    return round(min(engagement_score, 100), 2)


if __name__ == "__main__":
    score = calculate_engagement(85, 20, 15)
    print("Engagement Score:", score)
