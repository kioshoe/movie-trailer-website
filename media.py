import webbrowser


# Function template for movie data entry
class Movie():
    def __init__(self, m_title, m_duration, m_plot, m_poster, youtube_trailer):
        self.title = m_title
        self.duration = m_duration
        self.plot = m_plot
        self.poster_url = m_poster
        self.youtube_url = youtube_trailer
