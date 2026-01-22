def calculate_engagement(attendance, chat_messages, reactions):
    """
    Calculate a basic engagement score based on interaction metrics.
    """

    score = 0
    score += attendance * 0.5
    score += chat_messages * 2
    score += reactions * 3

    return round(score, 2)


if __name__ == "__main__":
    attendance = 80
    chat_messages = 5
    reactions = 3

    print("Engagement Score:",
          calculate_engagement(attendance, chat_messages, reactions))
