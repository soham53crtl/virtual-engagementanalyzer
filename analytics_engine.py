"""
Analytics Engine
----------------
Responsible for aggregating engagement data and generating
insights for meetings or virtual sessions.
"""

from statistics import mean


class EngagementAnalytics:
    def __init__(self):
        self.session_scores = []

    def add_session_score(self, score):
        self.session_scores.append(score)

    def average_engagement(self):
        if not self.session_scores:
            return 0
        return round(mean(self.session_scores), 2)

    def engagement_trend(self):
        if len(self.session_scores) < 2:
            return "Insufficient data"
        if self.session_scores[-1] > self.session_scores[0]:
            return "Improving"
        elif self.session_scores[-1] < self.session_scores[0]:
            return "Declining"
        return "Stable"


if __name__ == "__main__":
    analytics = EngagementAnalytics()
    analytics.add_session_score(45)
    analytics.add_session_score(62)
    analytics.add_session_score(78)

    print("Average Engagement:", analytics.average_engagement())
    print("Engagement Trend:", analytics.engagement_trend())
