# Imports function files
import movie_website
import media


# Data entry for each individual movie
# Format: Title, Duration, Plot, Poster URL, Youtube Trailer URL
sausage_party = media.Movie(
    "Sausage Party",
    "1h 29m",
    """A sausage learns what really happens to food and sets out to save his
     friends""",
    "https://upload.wikimedia.org/wikipedia/en/e/e4/Sausage_Party.png",
    "https://www.youtube.com/watch?v=9VoNgLnjzVg")

straight_outta_compton = media.Movie(
    "Straight Outta Compton",
    "2h 27m",
    "A biographical film depicting the rise and fall of the N.W.A.",
    "https://upload.wikimedia.org/wikipedia/en/7/7a/Straight_Outta_Compton_poster.jpg",
    "https://www.youtube.com/watch?v=oyoew4T74_w")

finding_dory = media.Movie(
    "Finding Dory",
    "1h 37m",
    "A forgetful fish searches for her long-lost parents",
    "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",
    "https://www.youtube.com/watch?v=UGWv91YZua4")

howls_moving_castle = media.Movie(
    "Howl's Moving Castle",
    "1h 59m",
    "Cursed by a witch, Sophie embarks on the adventure of a lifetime",
    "https://upload.wikimedia.org/wikipedia/en/a/a0/Howls-moving-castleposter.jpg",
    "https://www.youtube.com/watch?v=iwROgK94zcM")

labyrinth = media.Movie(
    "Labyrinth",
    "1h 41m",
    """Sarah must find her way to the center of a magic maze to rescue her
     brother from the Goblin King""",
    "https://upload.wikimedia.org/wikipedia/en/6/6b/Labyrinth_ver2.jpg",
    "https://www.youtube.com/watch?v=XRcOZZDvMv4")

kubo = media.Movie(
    "Kubo and the Two Strings",
    "1h 59m",
    """A young boy must locate his late father's armour to defeat spirits from
     his past""",
    "https://upload.wikimedia.org/wikipedia/en/c/c4/Kubo_and_the_Two_Strings_poster.png",
    "https://www.youtube.com/watch?v=p4-6qJzeb3A")

# Puts individual movie entries into a list
movies = [
    sausage_party,
    straight_outta_compton,
    finding_dory,
    howls_moving_castle,
    labyrinth,
    kubo
    ]

# Sorts movie entries in the list alphabetically
movies.sort(key=lambda movie: movie.title)

# Renders movie data into an interactive webpage
movie_website.open_movies_page(movies)
