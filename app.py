import streamlit as st

st.set_page_config(page_title="MoodFlix | Movie Finder", page_icon="🎬", layout="wide")

# Manual movie catalog: no database and no API key required.
MOVIES = [
    {"title":"Interstellar","year":2014,"genres":["Sci-Fi","Adventure","Drama"],"moods":["Mind-blown","Inspired","Emotional"],"rating":8.7,"emoji":"🚀","color":"#33256e","description":"A journey beyond the stars to save humanity.","tags":["space","future","family","science","epic"],"industry":"Hollywood"},
    {"title":"The Pursuit of Happyness","year":2006,"genres":["Drama","Biography"],"moods":["Inspired","Sad","Hopeful"],"rating":8.0,"emoji":"🌅","color":"#8a4b25","description":"A moving story about hope, hard work, and never giving up.","tags":["life","motivation","family","true story"],"industry":"Hollywood"},
    {"title":"The Intern","year":2015,"genres":["Comedy","Drama"],"moods":["Happy","Relaxed","Hopeful"],"rating":7.1,"emoji":"🧑‍💼","color":"#24665c","description":"An unexpected friendship makes work and life better.","tags":["friendship","work","feel good","funny"],"industry":"Hollywood"},
    {"title":"La La Land","year":2016,"genres":["Romance","Drama","Music"],"moods":["Romantic","Dreamy","Emotional"],"rating":8.0,"emoji":"🎹","color":"#8e3e72","description":"Love, music, and big dreams collide under city lights.","tags":["love","music","dreams","dance"],"industry":"Hollywood"},
    {"title":"Knives Out","year":2019,"genres":["Mystery","Comedy","Crime"],"moods":["Mind-blown","Thrilled","Curious"],"rating":7.9,"emoji":"🕵️","color":"#7d3f32","description":"A sharp detective unravels a family's tangled secrets.","tags":["mystery","detective","puzzle","funny"],"industry":"Hollywood"},
    {"title":"The Dark Knight","year":2008,"genres":["Action","Crime","Drama"],"moods":["Thrilled","Intense"],"rating":9.0,"emoji":"🦇","color":"#25344a","description":"A city faces chaos when a brilliant criminal appears.","tags":["hero","crime","dark","action"],"industry":"Hollywood"},
    {"title":"Inside Out","year":2015,"genres":["Animation","Comedy","Family"],"moods":["Happy","Emotional","Relaxed"],"rating":8.1,"emoji":"🌈","color":"#2d6b9b","description":"A colourful adventure inside the mind and its emotions.","tags":["family","feel good","emotions","funny"],"industry":"Hollywood"},
    {"title":"The Grand Budapest Hotel","year":2014,"genres":["Comedy","Adventure"],"moods":["Happy","Curious","Relaxed"],"rating":8.1,"emoji":"🏨","color":"#a84e77","description":"A quirky concierge gets caught in a wonderfully odd mystery.","tags":["quirky","colourful","funny","adventure"],"industry":"Hollywood"},
    {"title":"Your Name","year":2016,"genres":["Animation","Romance","Fantasy"],"moods":["Romantic","Dreamy","Emotional"],"rating":8.4,"emoji":"🌠","color":"#425ca0","description":"Two strangers become connected by a mysterious phenomenon.","tags":["anime","love","fantasy","stars"],"industry":"International"},
    {"title":"The Martian","year":2015,"genres":["Sci-Fi","Adventure","Drama"],"moods":["Inspired","Thrilled","Curious"],"rating":8.0,"emoji":"🪐","color":"#a64c2b","description":"An astronaut uses science and humour to survive on Mars.","tags":["space","science","survival","funny"],"industry":"Hollywood"},
    {"title":"Zindagi Na Milegi Dobara","year":2011,"genres":["Comedy","Drama","Adventure"],"moods":["Happy","Inspired","Relaxed"],"rating":8.2,"emoji":"🌊","color":"#167c80","description":"Three friends rediscover life during a road trip.","tags":["friendship","travel","life","feel good"],"industry":"Bollywood"},
    {"title":"A Quiet Place","year":2018,"genres":["Horror","Thriller","Drama"],"moods":["Thrilled","Intense"],"rating":7.5,"emoji":"🤫","color":"#384735","description":"A family must stay silent to survive a terrifying threat.","tags":["survival","suspense","scary","family"],"industry":"Hollywood"},
    {"title":"Paddington 2","year":2017,"genres":["Comedy","Family","Adventure"],"moods":["Happy","Relaxed","Hopeful"],"rating":7.8,"emoji":"🧸","color":"#bf7434","description":"A kind-hearted bear brings a neighbourhood together.","tags":["family","kindness","funny","feel good"],"industry":"Hollywood"},
    {"title":"Eternal Sunshine of the Spotless Mind","year":2004,"genres":["Romance","Sci-Fi","Drama"],"moods":["Sad","Dreamy","Mind-blown"],"rating":8.3,"emoji":"🧠","color":"#426e78","description":"A strange, heartfelt story about memory and love.","tags":["memory","love","thought provoking","emotional"],"industry":"Hollywood"},
    {"title":"Spider-Man: Into the Spider-Verse","year":2018,"genres":["Animation","Action","Adventure"],"moods":["Happy","Thrilled","Inspired"],"rating":8.4,"emoji":"🕸️","color":"#a82d4b","description":"A fresh, energetic superhero adventure across dimensions.","tags":["hero","multiverse","colourful","action"],"industry":"Hollywood"},
    {"title":"The Shawshank Redemption","year":1994,"genres":["Drama","Crime"],"moods":["Inspired","Emotional","Hopeful"],"rating":9.3,"emoji":"🕊️","color":"#536c4c","description":"An enduring story of friendship, patience, and hope.","tags":["hope","friendship","prison","life"],"industry":"Hollywood"},
    {"title":"Jab We Met","year":2007,"genres":["Romance","Comedy"],"moods":["Romantic","Happy","Hopeful"],"rating":7.9,"emoji":"🚆","color":"#b64b61","description":"A lively encounter turns into an unforgettable journey.","tags":["love","travel","funny","feel good"],"industry":"Bollywood"},
    {"title":"Coco","year":2017,"genres":["Animation","Family","Fantasy"],"moods":["Happy","Emotional","Relaxed"],"rating":8.4,"emoji":"🎸","color":"#bb5b25","description":"A young musician discovers family, memory, and tradition.","tags":["music","family","emotional","colourful"],"industry":"Hollywood"},
    {"title":"Get Out","year":2017,"genres":["Horror","Mystery","Thriller"],"moods":["Mind-blown","Thrilled","Intense"],"rating":7.8,"emoji":"👁️","color":"#654e86","description":"A weekend visit turns into a chilling mystery.","tags":["mystery","suspense","psychological","dark"],"industry":"Hollywood"},
    {"title":"Finding Nemo","year":2003,"genres":["Animation","Adventure","Family"],"moods":["Happy","Relaxed","Hopeful"],"rating":8.2,"emoji":"🐠","color":"#1686a4","description":"A little fish inspires a big ocean-spanning adventure.","tags":["ocean","family","adventure","feel good"],"industry":"Hollywood"},
    {"title":"3 Idiots","year":2009,"genres":["Comedy","Drama"],"moods":["Happy","Inspired","Emotional"],"rating":8.4,"emoji":"🎓","color":"#2f8a74","description":"Three engineering students challenge pressure, expectations, and the meaning of success.","tags":["college","friendship","education","funny","motivation"],"industry":"Bollywood"},
    {"title":"Dangal","year":2016,"genres":["Drama","Sport","Biography"],"moods":["Inspired","Emotional","Thrilled"],"rating":8.3,"emoji":"🤼","color":"#8b5535","description":"A determined father trains his daughters to become wrestling champions.","tags":["sports","family","motivation","true story"],"industry":"Bollywood"},
    {"title":"Queen","year":2013,"genres":["Comedy","Drama"],"moods":["Happy","Inspired","Hopeful"],"rating":8.1,"emoji":"👑","color":"#a86b39","description":"A young woman discovers confidence and independence on a solo trip.","tags":["travel","self discovery","women","funny"],"industry":"Bollywood"},
    {"title":"Taare Zameen Par","year":2007,"genres":["Drama","Family"],"moods":["Emotional","Inspired","Sad"],"rating":8.3,"emoji":"🎨","color":"#3f6895","description":"A caring teacher helps a child see his own strengths.","tags":["school","family","education","emotional"],"industry":"Bollywood"},
    {"title":"Andhadhun","year":2018,"genres":["Thriller","Crime","Mystery"],"moods":["Mind-blown","Thrilled","Intense"],"rating":8.2,"emoji":"🎹","color":"#4e456c","description":"A pianist becomes tangled in a dangerous series of surprises.","tags":["twist","mystery","crime","suspense"],"industry":"Bollywood"},
    {"title":"Drishyam","year":2015,"genres":["Thriller","Crime","Drama"],"moods":["Mind-blown","Thrilled","Curious"],"rating":8.2,"emoji":"🧩","color":"#4c6550","description":"A father uses careful planning to protect his family.","tags":["family","mystery","crime","twist"],"industry":"Bollywood"},
    {"title":"Dil Chahta Hai","year":2001,"genres":["Comedy","Drama","Romance"],"moods":["Happy","Relaxed","Hopeful"],"rating":8.1,"emoji":"🌴","color":"#337e87","description":"Three friends navigate love and adulthood in their own ways.","tags":["friendship","travel","love","growing up"],"industry":"Bollywood"},
    {"title":"Kal Ho Naa Ho","year":2003,"genres":["Romance","Comedy","Drama"],"moods":["Romantic","Emotional","Sad"],"rating":7.9,"emoji":"❤️","color":"#a94458","description":"A warm-hearted stranger changes the lives of a family and their friends.","tags":["love","family","friendship","emotional"],"industry":"Bollywood"},
    {"title":"Lagaan","year":2001,"genres":["Drama","Sport","Musical"],"moods":["Inspired","Thrilled","Hopeful"],"rating":8.1,"emoji":"🏏","color":"#94713d","description":"Villagers risk everything in a cricket match against colonial rulers.","tags":["cricket","history","teamwork","underdog"],"industry":"Bollywood"},
    {"title":"Barfi!","year":2012,"genres":["Romance","Comedy","Drama"],"moods":["Happy","Romantic","Emotional"],"rating":8.1,"emoji":"🎈","color":"#bb6c8b","description":"A heartfelt story about love, friendship, and seeing beyond appearances.","tags":["love","kindness","friendship","feel good"],"industry":"Bollywood"},
    {"title":"Bajrangi Bhaijaan","year":2015,"genres":["Drama","Comedy","Adventure"],"moods":["Emotional","Hopeful","Inspired"],"rating":8.1,"emoji":"🤝","color":"#397b76","description":"A kind man helps a lost child reunite with her family.","tags":["kindness","family","journey","hope"],"industry":"Bollywood"},
    {"title":"Gully Boy","year":2019,"genres":["Drama","Music"],"moods":["Inspired","Emotional","Thrilled"],"rating":7.9,"emoji":"🎤","color":"#7650a3","description":"A Mumbai street rapper fights to make his voice heard.","tags":["music","dreams","rap","motivation"],"industry":"Bollywood"},
    {"title":"Chak De! India","year":2007,"genres":["Drama","Sport"],"moods":["Inspired","Thrilled","Hopeful"],"rating":8.1,"emoji":"🏑","color":"#286b9b","description":"A coach brings a women's hockey team together to chase a title.","tags":["sports","teamwork","motivation","underdog"],"industry":"Bollywood"},
    {"title":"PK","year":2014,"genres":["Comedy","Drama","Sci-Fi"],"moods":["Happy","Curious","Mind-blown"],"rating":8.1,"emoji":"👽","color":"#4d8a9b","description":"An outsider asks unusual questions about human beliefs and society.","tags":["alien","society","funny","thought provoking"],"industry":"Bollywood"},
    {"title":"Inception","year":2010,"genres":["Sci-Fi","Action","Thriller"],"moods":["Mind-blown","Thrilled","Curious"],"rating":8.8,"emoji":"🌀","color":"#3c4c78","description":"A specialist enters dreams to plant an idea in someone's mind.","tags":["dreams","heist","twist","science"],"industry":"Hollywood"},
    {"title":"The Avengers","year":2012,"genres":["Action","Sci-Fi","Adventure"],"moods":["Happy","Thrilled","Inspired"],"rating":8.0,"emoji":"🛡️","color":"#8b443c","description":"A team of heroes unite to defend Earth from a powerful threat.","tags":["superhero","teamwork","action","aliens"],"industry":"Hollywood"},
    {"title":"Forrest Gump","year":1994,"genres":["Drama","Romance"],"moods":["Inspired","Emotional","Hopeful"],"rating":8.8,"emoji":"🏃","color":"#59805a","description":"An unassuming man experiences extraordinary moments in American history.","tags":["life","hope","love","true story"],"industry":"Hollywood"},
    {"title":"The Lion King","year":1994,"genres":["Animation","Adventure","Drama"],"moods":["Happy","Emotional","Inspired"],"rating":8.5,"emoji":"🦁","color":"#a36a2d","description":"A young lion learns about responsibility, loss, and courage.","tags":["family","animals","courage","classic"],"industry":"Hollywood"},
    {"title":"Titanic","year":1997,"genres":["Romance","Drama"],"moods":["Romantic","Sad","Emotional"],"rating":7.9,"emoji":"🚢","color":"#416d8c","description":"A romance unfolds aboard a doomed ocean liner.","tags":["love","history","tragedy","classic"],"industry":"Hollywood"},
    {"title":"Jurassic Park","year":1993,"genres":["Adventure","Sci-Fi","Thriller"],"moods":["Thrilled","Curious","Inspired"],"rating":8.2,"emoji":"🦖","color":"#547344","description":"A theme park of cloned dinosaurs becomes a fight for survival.","tags":["dinosaurs","adventure","science","survival"],"industry":"Hollywood"},
    {"title":"The Devil Wears Prada","year":2006,"genres":["Comedy","Drama"],"moods":["Happy","Inspired","Relaxed"],"rating":7.0,"emoji":"👠","color":"#9a3155","description":"A new assistant learns the demanding world of fashion publishing.","tags":["fashion","career","work","funny"],"industry":"Hollywood"},
    {"title":"The Notebook","year":2004,"genres":["Romance","Drama"],"moods":["Romantic","Sad","Emotional"],"rating":7.8,"emoji":"📖","color":"#a75b66","description":"A lifelong love story unfolds through memories and difficult choices.","tags":["love","memories","romance","emotional"],"industry":"Hollywood"},
    {"title":"Shutter Island","year":2010,"genres":["Mystery","Thriller","Drama"],"moods":["Mind-blown","Thrilled","Intense"],"rating":8.2,"emoji":"🏝️","color":"#3c5367","description":"A detective investigates a disappearance at a remote institution.","tags":["mystery","psychological","twist","dark"],"industry":"Hollywood"},
    {"title":"The Conjuring","year":2013,"genres":["Horror","Mystery","Thriller"],"moods":["Thrilled","Intense"],"rating":7.5,"emoji":"👻","color":"#484456","description":"Paranormal investigators help a family facing a frightening presence.","tags":["ghost","supernatural","scary","suspense"],"industry":"Hollywood"},
    {"title":"Toy Story","year":1995,"genres":["Animation","Comedy","Family"],"moods":["Happy","Relaxed","Hopeful"],"rating":8.3,"emoji":"🧸","color":"#3d7b9c","description":"Toys come to life when humans are not around.","tags":["friendship","family","funny","adventure"],"industry":"Hollywood"},
    {"title":"The Secret Life of Walter Mitty","year":2013,"genres":["Adventure","Comedy","Drama"],"moods":["Inspired","Dreamy","Happy"],"rating":7.3,"emoji":"📷","color":"#3b797e","description":"A daydreamer steps into the real world on an unexpected journey.","tags":["travel","dreams","self discovery","adventure"],"industry":"Hollywood"},
    {"title":"The Social Network","year":2010,"genres":["Drama","Biography"],"moods":["Curious","Inspired","Intense"],"rating":7.8,"emoji":"💻","color":"#344f82","description":"The story of the creation of a world-changing social network.","tags":["technology","startup","business","ambition"],"industry":"Hollywood"},
    {"title":"Ratatouille","year":2007,"genres":["Animation","Comedy","Family"],"moods":["Happy","Inspired","Relaxed"],"rating":8.1,"emoji":"🍲","color":"#a94c35","description":"A rat with a passion for cooking pursues an unlikely culinary dream.","tags":["food","dreams","family","funny"],"industry":"Hollywood"},
    {"title":"The Truman Show","year":1998,"genres":["Comedy","Drama","Sci-Fi"],"moods":["Mind-blown","Curious","Inspired"],"rating":8.2,"emoji":"📺","color":"#3f7d8a","description":"A man begins to suspect his seemingly perfect world is staged.","tags":["reality","media","thought provoking","twist"],"industry":"Hollywood"},
    {"title":"A Beautiful Mind","year":2001,"genres":["Drama","Biography"],"moods":["Inspired","Emotional","Curious"],"rating":8.2,"emoji":"🧮","color":"#5d6c92","description":"A brilliant mathematician faces personal challenges while pursuing his work.","tags":["science","mathematics","life","motivation"],"industry":"Hollywood"},
    {"title":"The Hangover","year":2009,"genres":["Comedy"],"moods":["Happy","Relaxed"],"rating":7.7,"emoji":"🎉","color":"#a67b37","description":"Friends try to piece together a wild night in Las Vegas.","tags":["friends","party","funny","mystery"],"industry":"Hollywood"},
]

MOOD_INFO = {
    "Happy": ("☀️", "Feel-good stories, bright adventures, and easy laughs."),
    "Sad": ("🌧️", "A little emotional storytelling for a reflective evening."),
    "Romantic": ("💗", "Love stories, chemistry, and dreamy moments."),
    "Mind-blown": ("🌀", "Twists, big ideas, and stories to think about afterward."),
    "Thrilled": ("⚡", "Suspense, action, and edge-of-your-seat energy."),
    "Inspired": ("🔥", "Stories that leave you motivated."),
    "Relaxed": ("🍃", "Comfort-watch picks for a cosy night."),
    "Dreamy": ("🌙", "Magical, atmospheric, and imaginative worlds."),
    "Emotional": ("💜", "Heartfelt stories that stay with you."),
    "Hopeful": ("🌱", "Stories about second chances and brighter days."),
    "Curious": ("🔎", "Intriguing stories that make you ask questions."),
    "Intense": ("⚡", "High-stakes stories with a darker edge."),
}
ALL_GENRES = sorted({g for movie in MOVIES for g in movie["genres"]})

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
.stApp { background: radial-gradient(ellipse at 15% 0%, #251c50 0%, #11111c 40%, #0b0c12 100%); color:#f6f3ff; font-family:'DM Sans',sans-serif; }
.block-container { max-width:1280px; padding-top:1.6rem; padding-bottom:3rem; }
h1,h2,h3 { font-family:'Space Grotesk',sans-serif !important; letter-spacing:-.035em; }
.brand { font-family:'Space Grotesk',sans-serif; font-size:1.05rem; font-weight:700; letter-spacing:.16em; color:#fff; }
.brand span { color:#b7a0ff; }
.hero { padding:2.1rem 2.2rem; border:1px solid rgba(255,255,255,.12); border-radius:26px; background:linear-gradient(115deg,rgba(117,76,255,.25),rgba(20,20,35,.7) 55%,rgba(27,184,193,.12)); box-shadow:0 20px 65px rgba(0,0,0,.2); }
.eyebrow { color:#c2b2ff; font-size:.75rem; letter-spacing:.2em; text-transform:uppercase; font-weight:700; }
.hero h1 { font-size:clamp(2.4rem,5vw,4.4rem); line-height:1.02; margin:.55rem 0 .8rem; }
.muted { color:#b7b5ca; }
.movie-card { border:1px solid rgba(255,255,255,.1); border-radius:20px; overflow:hidden; background:linear-gradient(160deg,rgba(255,255,255,.07),rgba(255,255,255,.025)); min-height:300px; }
.poster { height:135px; display:flex; align-items:center; justify-content:center; font-size:3.6rem; }
.movie-body { padding:1rem; }
.movie-title { font-family:'Space Grotesk',sans-serif; font-size:1.04rem; font-weight:700; color:#fff; }
.movie-desc { color:#b8b6c9; font-size:.83rem; line-height:1.45; min-height:3.5em; margin:.5rem 0; }
.rating { color:#ffd479; font-weight:700; font-size:.9rem; }
.pill { display:inline-block; padding:.3rem .6rem; margin:.15rem .15rem .1rem 0; border:1px solid rgba(255,255,255,.13); background:rgba(255,255,255,.06); color:#d9d3f4; border-radius:99px; font-size:.72rem; }
div[data-testid="stButton"] button { border-radius:12px; border:1px solid rgba(184,160,255,.45); background:linear-gradient(100deg,#8c68ff,#6546d8); color:white; font-weight:700; }
div[data-testid="stButton"] button:hover { border-color:#d2c5ff; color:white; background:linear-gradient(100deg,#9a7cff,#7356e8); }
div[data-testid="stSelectbox"] > div > div, div[data-testid="stTextInput"] input { background:#171725; border-color:#37334e; border-radius:12px; }
footer {visibility:hidden;}
/* Remove Streamlit header and top decoration */
[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stDecoration"] {
    display: none;
}

/* Remove the border around the main app */
.stApp {
    border: none !important;
}

/* Remove extra top spacing */
.block-container {
    padding-top: 1rem !important;
}
</style>
""", unsafe_allow_html=True)

if "watchlist" not in st.session_state:
    st.session_state.watchlist = []

st.markdown('<div class="brand">MOOD<span>FLIX</span> <span style="color:#817b9b;font-weight:400;letter-spacing:.06em">/ YOUR VIBE. YOUR MOVIE.</span></div>', unsafe_allow_html=True)
st.write("")
st.markdown("""
<div class="hero">
  <div class="eyebrow">✦ Your personal movie compass</div>
  <h1>What’s your mood<br>tonight?</h1>
  <div class="muted" style="font-size:1.05rem;max-width:600px">Skip the endless scrolling. Pick a feeling and discover a movie for the kind of night you want.</div>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([1.15, 1], gap="large")
with left:
    mood = st.selectbox("01 · Pick your mood", list(MOOD_INFO.keys()))
    st.caption(f"{MOOD_INFO[mood][0]}  {MOOD_INFO[mood][1]}")
    industry = st.selectbox("02 · Movie industry", ["Both industries", "Bollywood", "Hollywood", "International"])
with right:
    genre = st.selectbox("03 · Favourite genre", ["Any genre"] + ALL_GENRES)
    search = st.text_input("04 · Optional keyword", placeholder="Try: space, friendship, mystery…")

c1, c2, c3 = st.columns([1, 1, 2])
with c1:
    min_rating = st.selectbox("Minimum rating", ["Any", "7.0+", "8.0+", "8.5+"])
with c2:
    count = st.selectbox("Recommendations", [3, 6, 9, 12], index=1)
with c3:
    st.write("")
    st.write("")
    find = st.button("✦  Find my vibe", use_container_width=True)

threshold = {"Any": 0, "7.0+": 7.0, "8.0+": 8.0, "8.5+": 8.5}[min_rating]
query = search.strip().lower()
results = []
for movie in MOVIES:
    if mood not in movie["moods"]:
        continue
    if industry != "Both industries" and movie["industry"] != industry:
        continue
    if genre != "Any genre" and genre not in movie["genres"]:
        continue
    if movie["rating"] < threshold:
        continue
    haystack = (movie["title"] + " " + movie["description"] + " " + " ".join(movie["genres"]) + " " + " ".join(movie["tags"]) + " " + movie["industry"]).lower()
    if query and query not in haystack:
        continue
    results.append(movie)

def score(movie):
    s = movie["rating"]
    if mood in movie["moods"]: s += 2
    if genre != "Any genre" and genre in movie["genres"]: s += 1.5
    if query and query in (movie["title"] + " " + movie["description"] + " " + " ".join(movie["tags"])).lower(): s += 2
    return s

results.sort(key=score, reverse=True)
st.write("")
st.markdown(f"<div style='font-family:Space Grotesk;font-size:1.65rem;font-weight:700'>Picked for your {mood.lower()} side <span style='font-size:1rem;color:#b8a8ff'>✦ {len(results)} matches</span></div>", unsafe_allow_html=True)
st.markdown("<div class='muted'>A little recommendation logic, a little movie magic.</div>", unsafe_allow_html=True)
st.write("")

if not results:
    st.info("No exact matches. Try another mood, select 'Both industries', or remove a filter.")
else:
    cols = st.columns(3, gap="medium")
    for i, movie in enumerate(results[:count]):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="movie-card">
              <div class="poster" style="background:radial-gradient(circle at 50% 15%, {movie['color']} 0%, #171522 82%);">{movie['emoji']}</div>
              <div class="movie-body">
                <div class="movie-title">{movie['title']}</div>
                <div class="muted" style="font-size:.78rem">{movie['year']} · {movie['industry']} · {' / '.join(movie['genres'][:2])}</div>
                <div class="movie-desc">{movie['description']}</div>
                <div class="rating">★ {movie['rating']:.1f} <span style="color:#85819b;font-weight:400">/ 10</span></div>
                <div style="margin-top:.5rem">{''.join(f"<span class='pill'>{g}</span>" for g in movie['genres'][:3])}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)
            saved = movie["title"] in st.session_state.watchlist
            if st.button("✓ In watchlist" if saved else "＋ Add to watchlist", key=f"save_{movie['title']}", use_container_width=True):
                if saved:
                    st.session_state.watchlist.remove(movie["title"])
                else:
                    st.session_state.watchlist.append(movie["title"])
                st.rerun()

st.write("")
with st.expander(f"♡ My watchlist ({len(st.session_state.watchlist)})"):
    if st.session_state.watchlist:
        for title in st.session_state.watchlist:
            movie = next((m for m in MOVIES if m["title"] == title), None)
            if movie:
                st.markdown(f"**{movie['emoji']} {movie['title']}** · {movie['year']} · ★ {movie['rating']:.1f}")
        if st.button("Clear watchlist"):
            st.session_state.watchlist = []
            st.rerun()
    else:
        st.caption("Save movies above to keep a watchlist while this app session is open.")

st.markdown("<hr style='border-color:rgba(255,255,255,.1);margin-top:2rem'>", unsafe_allow_html=True)
st.markdown(f"<div class='muted' style='font-size:.8rem;text-align:center'>MOODFLIX · Manual movie catalog · {len(MOVIES)} movies · No database or API key required</div>", unsafe_allow_html=True)
