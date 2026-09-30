import requests
import streamlit as st
import html

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Al Quran Kareem",
    page_icon="🕌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= PROFESSIONAL UI =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Inter:wght@400;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(circle at 85% 5%, rgba(185,149,75,.12), transparent 28%),
        linear-gradient(135deg, #071812 0%, #0a2118 50%, #071812 100%);
    color: #f5f1e8;
}

.block-container {
    max-width: 1180px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* Header */
.quran-header {
    padding: 26px 30px;
    border-radius: 22px;
    background: linear-gradient(135deg, #0c6f49, #063a29);
    border: 1px solid rgba(218,188,105,.45);
    box-shadow: 0 15px 45px rgba(0,0,0,.22);
    margin-bottom: 24px;
}
.quran-brand {
    font-family: Inter, sans-serif;
    font-size: 30px;
    font-weight: 800;
    color: white;
}
.quran-brand span {
    color: #dfc576;
}
.quran-tagline {
    color: #d4e1da;
    margin-top: 5px;
    font-size: 13px;
    letter-spacing: 1px;
}

/* Hero */
.hero {
    min-height: 300px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 42px;
    border-radius: 26px;
    background:
        radial-gradient(circle at 85% 30%, rgba(222,197,118,.22), transparent 25%),
        linear-gradient(135deg, #0b6b46, #082f22);
    border: 1px solid rgba(218,188,105,.35);
    margin-bottom: 28px;
    overflow: hidden;
}
.hero-label {
    color: #dfc576;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 4px;
}
.hero h1 {
    color: white !important;
    font-family: Inter, sans-serif;
    font-size: clamp(38px, 5vw, 64px);
    line-height: 1;
    margin: 13px 0;
}
.hero h1 span {
    color: #dfc576;
}
.hero p {
    color: #d7e4dd;
    max-width: 650px;
    line-height: 1.7;
    font-size: 16px;
}

/* Cards */
.quran-card {
    background: #ffffff;
    color: #17231e;
    border: 1px solid #d5b86c;
    border-radius: 20px;
    padding: 28px;
    margin: 18px 0;
    box-shadow: 0 10px 35px rgba(0,0,0,.17);
}
.surah-name {
    color: #0b6b46;
    font-size: 26px;
    font-weight: 800;
}
.surah-meta {
    color: #967532;
    font-size: 12px;
    margin-top: 4px;
}
.ayah-number {
    display: inline-block;
    background: #0b6b46;
    color: white;
    border-radius: 50%;
    min-width: 34px;
    height: 34px;
    line-height: 34px;
    text-align: center;
    font-weight: 700;
}
.arabic {
    direction: rtl;
    text-align: right;
    font-family: "Amiri", "Noto Naskh Arabic", serif;
    font-size: 34px;
    line-height: 2.25;
    color: #111;
    padding: 18px 0;
}
.translation {
    background: #f3f7f4;
    border-left: 4px solid #0b6b46;
    padding: 17px;
    border-radius: 10px;
    color: #33423a;
    line-height: 1.8;
    margin-bottom: 12px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #081c14;
    border-right: 1px solid #9d7c37;
}
section[data-testid="stSidebar"] * {
    color: #f5f1e8;
}

/* Inputs */
div[data-baseweb="select"] > div {
    background: #102a20;
    border: 1px solid #526f61;
    border-radius: 10px;
}
.stTextInput input {
    background: #102a20;
    color: white;
    border: 1px solid #526f61;
    border-radius: 10px;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 11px;
    border: 1px solid #b9954b;
    background: #0b6b46;
    color: white;
    font-weight: 700;
    min-height: 44px;
}
.stButton > button:hover {
    background: #b9954b;
    color: #071812;
}

/* Section */
.section-title {
    color: #dfc576;
    font-size: 23px;
    font-weight: 800;
    margin: 25px 0 10px;
}

/* Footer */
.footer {
    margin-top: 45px;
    padding: 25px;
    text-align: center;
    color: #9eafa6;
    border-top: 1px solid #29463a;
}
.footer strong {
    color: #dfc576;
}

/* Mobile */
@media (max-width: 700px) {
    .hero {
        padding: 30px 23px;
    }
    .arabic {
        font-size: 27px;
    }
    .quran-card {
        padding: 20px;
    }
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("""
<div class="quran-header">
    <div class="quran-brand">🕌 Al Quran <span>Kareem</span></div>
    <div class="quran-tagline">READ • LISTEN • UNDERSTAND • REFLECT</div>
</div>

<div class="hero">
    <div class="hero-label">THE HOLY QURAN</div>
    <h1>Read. Listen.<br><span>Reflect.</span></h1>
    <p>
        A peaceful and modern Quran experience with Arabic text,
        translations and beautiful recitations.
    </p>
</div>
""", unsafe_allow_html=True)

# ================= API =================
@st.cache_data(ttl=3600)
def get_surahs():
    response = requests.get("https://api.alquran.cloud/v1/surah", timeout=20)
    response.raise_for_status()
    return response.json()["data"]

surahlist = get_surahs()

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("## 🕌 Quran Menu")
    st.markdown("---")

    options = [f'{s["number"]} | {s["name"]} — {s["englishName"]}' for s in surahlist]

    item = st.selectbox("📖 Choose Surah", options)
    surah_num = int(item.split("|")[0])

    languages = {
        "Urdu": "ur.jalandhry",
        "English": "en.sahih",
        "Turkish": "tr.diyanet",
        "Spanish": "es.cortes",
        "Hindi": "hi.hindi",
        "Farsi": "fa.makarem"
    }

    language = st.selectbox("🌍 Translation", list(languages.keys()))

    reciters = {
        "Abdur Rahman As-Sudais": "ar.abdurrahmaansudais",
        "Mishary Rashid Alafasy": "ar.alafasy",
        "Maher Al-Muaiqly": "ar.mahermuaiqly",
        "Saad Al-Ghamdi": "ar.saadalghamidi",
        "Ahmed Al-Ajmi": "ar.ahmedajamy"
    }

    selected_reciter = st.selectbox("🎧 Qari", list(reciters.keys()))

    st.markdown("---")
    st.caption("Al Quran Kareem")
    st.caption("Read • Listen • Reflect")

# ================= DATA =================
@st.cache_data(ttl=3600)
def get_surah_data(number, translation_edition, audio_edition):
    arabic = requests.get(
        f"https://api.alquran.cloud/v1/surah/{number}/quran-uthmani",
        timeout=20
    ).json()["data"]

    translation = requests.get(
        f"https://api.alquran.cloud/v1/surah/{number}/{translation_edition}",
        timeout=20
    ).json()["data"]["ayahs"]

    audio = requests.get(
        f"https://api.alquran.cloud/v1/surah/{number}/{audio_edition}",
        timeout=20
    ).json()["data"]["ayahs"]

    return arabic, translation, audio

arabic, translation, audio = get_surah_data(
    surah_num,
    languages[language],
    reciters[selected_reciter]
)

# ================= SURAH HEADER =================
st.markdown(f"""
<div class="quran-card">
    <div class="surah-name">{html.escape(arabic["name"])}</div>
    <div class="surah-meta">
        {html.escape(arabic["englishName"])} ·
        {html.escape(arabic["englishNameTranslation"])} ·
        {arabic["numberOfAyahs"]} Ayahs ·
        {html.escape(arabic["revelationType"])}
    </div>
    <div style="text-align:center;font-family:Amiri;font-size:48px;color:#0b6b46;margin-top:18px;">
        بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<div class="section-title">Surah {surah_num} — {html.escape(arabic["englishName"])}</div>',
    unsafe_allow_html=True
)

# ================= AYahs =================
for ar, tr, au in zip(arabic["ayahs"], translation, audio):

    st.markdown(f"""
    <div class="quran-card">
        <span class="ayah-number">{ar["numberInSurah"]}</span>
        <div class="arabic">{html.escape(ar["text"])}</div>
        <div class="translation">{html.escape(tr["text"])}</div>
    </div>
    """, unsafe_allow_html=True)

    if au.get("audio"):
        st.audio(au["audio"])
    else:
        st.warning("Audio not available for this Qari.")

# ================= FOOTER =================
st.markdown("""
<div class="footer">
    <strong>🕌 Al Quran Kareem</strong><br>
    Read • Listen • Understand • Reflect
</div>
""", unsafe_allow_html=True)
