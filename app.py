import streamlit as st
import pandas as pd
import plotly.express as px
import time

# ==============================================================================
# 1. TIETOKANTA
# ==============================================================================

champagne_db = {
    # --- MEIDÄN TUOTE ---
    "le bullet": {
        "name": "Champagne Le Bullet",
        "grapes": {"PN": 46, "PM": 45, "CH": 9},
        "dosage": 9, "malolactic": 1, "price": 35.98,
        "image_url": "https://www.viinitie.fi/cdn/shop/products/bullet.jpg?v=1621854247",
        "alko_url": "https://www.alko.fi/tuotteet/902791/Le-Bullet-Champagne-Brut/"
    },

    # --- SISARVIINI ---
    "la chouette": {
        "name": "La Chouette de Champillon",
        "grapes": {"PN": 10, "PM": 85, "CH": 5},
        "dosage": 9, "malolactic": 1, "price": 34.98
    },

    # --- KILPAILIJAT ---
    "moet": {
        "name": "Moët & Chandon Impérial",
        "grapes": {"PN": 35, "PM": 35, "CH": 30},
        "dosage": 9, "malolactic": 1, "price": 59.90
    },
    "veuve clicquot": {
        "name": "Veuve Clicquot Yellow Label",
        "grapes": {"PN": 50, "PM": 20, "CH": 30},
        "dosage": 10, "malolactic": 1, "price": 62.90
    },
    "lanson": {
        "name": "Lanson Le Black Création",
        "grapes": {"PN": 50, "PM": 15, "CH": 35},
        "dosage": 8, "malolactic": 0, "price": 52.90
    },
    "mumm": {
        "name": "G.H. Mumm Cordon Rouge",
        "grapes": {"PN": 45, "PM": 25, "CH": 30},
        "dosage": 8, "malolactic": 1, "price": 49.90
    },
    "piper-heidsieck": {
        "name": "Piper-Heidsieck Cuvée Brut",
        "grapes": {"PN": 55, "PM": 30, "CH": 15},
        "dosage": 10, "malolactic": 1, "price": 54.90
    },
    "nicolas feuillatte": {
        "name": "Nicolas Feuillatte Réserve",
        "grapes": {"PN": 40, "PM": 40, "CH": 20},
        "dosage": 10, "malolactic": 1, "price": 42.90
    },
    "taittinger": {
        "name": "Taittinger Brut Réserve",
        "grapes": {"PN": 35, "PM": 25, "CH": 40},
        "dosage": 9, "malolactic": 1, "price": 59.90
    },
    "bollinger": {
        "name": "Bollinger Special Cuvée",
        "grapes": {"PN": 60, "PM": 15, "CH": 25},
        "dosage": 7, "malolactic": 1, "price": 74.90
    },
    "pol roger": {
        "name": "Pol Roger Brut Réserve",
        "grapes": {"PN": 33, "PM": 33, "CH": 34},
        "dosage": 9, "malolactic": 1, "price": 64.90
    },
    "laurent-perrier": {
        "name": "Laurent-Perrier La Cuvée",
        "grapes": {"PN": 35, "PM": 15, "CH": 50},
        "dosage": 9, "malolactic": 1, "price": 64.90
    },
    "louis roederer": {
        "name": "Louis Roederer Collection 244",
        "grapes": {"PN": 40, "PM": 18, "CH": 42},
        "dosage": 8, "malolactic": 0, "price": 69.90
    },
    "andre clouet": {
        "name": "André Clouet Grande Réserve",
        "grapes": {"PN": 100, "PM": 0, "CH": 0},
        "dosage": 8, "malolactic": 1, "price": 44.90
    },
    "charles mignon": {
        "name": "Charles Mignon Premium Reserve",
        "grapes": {"PN": 20, "PM": 60, "CH": 20},
        "dosage": 9, "malolactic": 1, "price": 34.90
    },
    "g.h. martel": {
        "name": "G.H. Martel Prestige Brut",
        "grapes": {"PN": 45, "PM": 25, "CH": 30},
        "dosage": 10, "malolactic": 1, "price": 29.90
    },
    "pannier": {
        "name": "Pannier Sélection Brut",
        "grapes": {"PN": 25, "PM": 50, "CH": 25},
        "dosage": 9, "malolactic": 1, "price": 39.90
    },
    "beaumont": {
        "name": "Beaumont des Crayères Grande Réserve",
        "grapes": {"PN": 25, "PM": 60, "CH": 15},
        "dosage": 8, "malolactic": 1, "price": 32.90
    },
    "baron-fuente": {
        "name": "Baron-Fuenté Tradition Brut",
        "grapes": {"PN": 10, "PM": 60, "CH": 30},
        "dosage": 9, "malolactic": 1, "price": 31.90
    },
    "castelnau": {
        "name": "Champagne de Castelnau Brut",
        "grapes": {"PN": 15, "PM": 45, "CH": 40},
        "dosage": 9, "malolactic": 1, "price": 39.90
    },
    "canard-duchene": {
        "name": "Canard-Duchêne Authentic",
        "grapes": {"PN": 45, "PM": 35, "CH": 20},
        "dosage": 9, "malolactic": 1, "price": 39.90
    },
    "drappier": {
        "name": "Drappier Carte d'Or",
        "grapes": {"PN": 80, "PM": 5, "CH": 15},
        "dosage": 7, "malolactic": 1, "price": 52.90
    },
    "louis massing": {
        "name": "Louis Massing Grand Cru",
        "grapes": {"PN": 0, "PM": 0, "CH": 100},
        "dosage": 8, "malolactic": 1, "price": 39.90
    },
    "ayala": {
        "name": "Ayala Brut Majeur",
        "grapes": {"PN": 40, "PM": 20, "CH": 40},
        "dosage": 7, "malolactic": 1, "price": 49.90
    },
    "gosset": {
        "name": "Gosset Grande Réserve",
        "grapes": {"PN": 45, "PM": 10, "CH": 45},
        "dosage": 8, "malolactic": 0, "price": 59.90
    },
    "deutz": {
        "name": "Deutz Brut Classic",
        "grapes": {"PN": 33, "PM": 33, "CH": 33},
        "dosage": 9, "malolactic": 1, "price": 54.90
    },
    "billecart-salmon": {
        "name": "Billecart-Salmon Brut Réserve",
        "grapes": {"PN": 30, "PM": 40, "CH": 30},
        "dosage": 8, "malolactic": 1, "price": 59.90
    },
    "charles heidsieck": {
        "name": "Charles Heidsieck Brut Réserve",
        "grapes": {"PN": 40, "PM": 20, "CH": 40},
        "dosage": 10, "malolactic": 1, "price": 68.90
    },
    "pommery": {
        "name": "Pommery Brut Royal",
        "grapes": {"PN": 33, "PM": 33, "CH": 34},
        "dosage": 9, "malolactic": 1, "price": 49.90
    },
    "ruinart": {
        "name": "Ruinart Blanc de Blancs",
        "grapes": {"PN": 0, "PM": 0, "CH": 100},
        "dosage": 7, "malolactic": 1, "price": 99.90
    },
    "dom perignon": {
        "name": "Dom Pérignon Vintage 2013",
        "grapes": {"PN": 50, "PM": 0, "CH": 50},
        "dosage": 5, "malolactic": 1, "price": 249.90
    },
    "krug": {
        "name": "Krug Grande Cuvée",
        "grapes": {"PN": 45, "PM": 15, "CH": 40},
        "dosage": 6, "malolactic": 0, "price": 269.90
    },
    "philipponnat": {
        "name": "Philipponnat Royale Réserve",
        "grapes": {"PN": 65, "PM": 5, "CH": 30},
        "dosage": 8, "malolactic": 0, "price": 64.90
    },
    "collet": {
        "name": "Champagne Collet Brut",
        "grapes": {"PN": 25, "PM": 50, "CH": 25},
        "dosage": 10, "malolactic": 1, "price": 39.90
    },
    "jacquart": {
        "name": "Jacquart Mosaïque Brut",
        "grapes": {"PN": 35, "PM": 25, "CH": 40},
        "dosage": 9, "malolactic": 1, "price": 44.90
    },
    "tsarine": {
        "name": "Tsarine Brut Premium",
        "grapes": {"PN": 34, "PM": 33, "CH": 33},
        "dosage": 8, "malolactic": 1, "price": 44.90
    }
}


# ==============================================================================
# 2. LOGIIKKA (LASKENTA)
# ==============================================================================

class ChampagneDNA:
    def __init__(self, db):
        self.database = db
        self.weights = {
            "grapes": 0.60,
            "dosage": 0.20,
            "style": 0.20,
        }

    def calculate_grape_match(self, w1_grapes, w2_grapes):
        diff = 0
        for grape in ["PN", "PM", "CH"]:
            diff += abs(w1_grapes.get(grape, 0) - w2_grapes.get(grape, 0))
        return 100 - (diff / 2)

    def compare(self, target_key, verrokki_key):
        w1 = self.database.get(target_key)
        w2 = self.database.get(verrokki_key)

        score_grapes = self.calculate_grape_match(w1['grapes'], w2['grapes'])
        diff_dosage = abs(w1['dosage'] - w2['dosage'])
        score_dosage = max(0, 100 - (diff_dosage * 10))
        score_style = 100 if w1['malolactic'] == w2['malolactic'] else 0

        total_score = (
                (score_grapes * self.weights['grapes']) +
                (score_dosage * self.weights['dosage']) +
                (score_style * self.weights['style'])
        )

        price_diff = w2['price'] - w1['price']

        return {
            "wine1": w1,
            "wine2": w2,
            "match_percent": round(total_score, 1),
            "price_diff": price_diff,
            "grapes_score": round(score_grapes, 1)
        }


# ==============================================================================
# 3. KÄYTTÖLIITTYMÄ
# ==============================================================================

st.set_page_config(page_title="Le Bullet DNA Matcher", page_icon="🍾", layout="centered")

# CSS: Tyylittely
st.markdown("""
    <style>
    .big-font { font-size: 70px !important; color: #d63031; font-weight: 800; text-align: center; margin-bottom: 0px; }
    .sub-text { text-align: center; font-size: 22px; font-style: italic; color: #636e72; margin-top: -10px; }
    .card { background-color: #fff; border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); overflow: hidden; text-align: center; margin-bottom: 20px; padding-bottom: 20px;}
    .card-content { padding: 20px; padding-bottom: 10px; }

    /* TUOTENIMEN TYYLI: MUSTA VÄRI */
    .wine-name-text { 
        font-size: 24px; 
        font-weight: bold; 
        color: #000000 !important;
        margin-bottom: 10px; 
        min-height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .wine-price { font-size: 20px; font-weight: normal; color: #2d3436; margin-bottom: 20px; }
    div.stButton > button:first-child { background-color: #d63031; color: white; font-size: 20px; font-weight: bold; border-radius: 8px; padding: 10px; width: 100%; border: none;}
    div.stButton > button:hover { background-color: #b71c1c; color: white; border: none;}

    /* Alko-napin tyyli */
    .alko-button {
        display: inline-block;
        padding: 10px 20px;
        background-color: #27ae60;
        color: white !important;
        text-decoration: none;
        border-radius: 5px;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .alko-button:hover { background-color: #2ecc71; }

    /* Kuvan tyyli */
    .wine-image { 
        width: 100%; 
        height: 300px; 
        object-fit: contain; 
        background-color: #f8f9fa; 
        padding: 20px; 
        border-bottom: 1px solid #eee;
    }
    </style>
    """, unsafe_allow_html=True)

# OTSIKKO
st.title("Champagne DNA Matcher 🧬")
st.markdown("""
**Onko lasissasi kaksoisolento?** Valitse mikä tahansa samppanja, niin algoritmi vertaa sen reseptiä (rypäleet, sokeri, valmistus) **Le Bulletiin**.
""")
st.divider()

# VALMISTELU
competitors = {k: v for k, v in champagne_db.items() if k != 'le bullet'}
sorted_competitors = sorted(competitors.items(), key=lambda x: x[1]['name'])
competitor_names = [v['name'] for k, v in sorted_competitors]
name_to_key = {v['name']: k for k, v in competitors.items()}

# SARAKKEET
col1, col2 = st.columns([1, 1])

# --- VASEN SARAKE: LE BULLET ---
with col1:
    bullet_data = champagne_db['le bullet']
    st.markdown(f"""
    <div class='card'>
        <img src="{bullet_data['image_url']}" class="wine-image">
        <div class='card-content'>
            <div class='wine-name-text'>{bullet_data['name']}</div>
            <div class='wine-price'>{bullet_data['price']} €</div>
            <a href="{bullet_data['alko_url']}" target="_blank" class="alko-button">Osta Alkosta 🛒</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- OIKEA SARAKE: HAASTAJA ---
with col2:
    selected_name = st.selectbox("Valitse samppanja:", competitor_names, index=None, placeholder="Valitse listasta...")

    if selected_name:
        verrokki_key = name_to_key[selected_name]
        verrokki_data = champagne_db[verrokki_key]
        st.markdown(f"""
        <div class='card'>
            <div class='card-content'>
                <div class='wine-name-text'>{verrokki_data['name']}</div>
                <div class='wine-price'>{verrokki_data['price']} €</div>
                </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class='card' style='height: 480px; display: flex; align-items: center; justify-content: center; color: #ccc;'>
            <h2>Valitse<br>samppanja<br>ylhäältä 👆</h2>
        </div>
        """, unsafe_allow_html=True)

st.write("")

# ACTION BUTTON
if selected_name:
    if st.button("SUORITA VERTAILU 🧬"):

        with st.spinner('Analysoidaan rypäleprofiilia...'):
            time.sleep(0.5)
        with st.spinner('Lasketaan hintaeroa...'):
            time.sleep(0.3)

        matcher = ChampagneDNA(champagne_db)
        res = matcher.compare("le bullet", verrokki_key)

        st.divider()

        st.balloons()
        st.markdown(f"<p class='big-font'>{res['match_percent']} %</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='sub-text'>Samaa makuprofiilia (Resepti-DNA)</p>", unsafe_allow_html=True)

        st.divider()

        m1, m2 = st.columns(2)
        with m1:
            st.metric("💰 HINTAERO", f"{res['price_diff']:.2f} €",
                      delta="Säästösi per pullo" if res['price_diff'] > 0 else "Verrokki halvempi")
        with m2:
            st.metric("🍇 Rypäleiden vastaavuus", f"{res['grapes_score']} %",
                      help="Kuinka samanlainen rypälesekoitus on?")

        st.subheader("🔬 Reseptit rinnakkain")

        data = {
            'Rypäle': ['Pinot Noir', 'Pinot Meunier', 'Chardonnay'] * 2,
            'Osuus %': [
                res['wine1']['grapes']['PN'], res['wine1']['grapes']['PM'], res['wine1']['grapes']['CH'],
                res['wine2']['grapes']['PN'], res['wine2']['grapes']['PM'], res['wine2']['grapes']['CH']
            ],
            'Viini': ['Le Bullet'] * 3 + [res['wine2']['name']] * 3
        }
        df = pd.DataFrame(data)

        fig = px.bar(df, x="Rypäle", y="Osuus %", color="Viini", barmode="group",
                     color_discrete_map={'Le Bullet': '#d63031', res['wine2']['name']: '#636e72'},
                     height=350)
        st.plotly_chart(fig, use_container_width=True)

        # ----------------------------------------
        # UUSI ANALYYSITEKSTIN LOGIIKKA ALKAA TÄSTÄ
        # ----------------------------------------
        analysis_text = f"**Analyysi:** Le Bullet ja {res['wine2']['name']} jakavat {res['grapes_score']} % saman rypälepohjan. "

        # Tyylivertailu (Malolaktinen)
        if res['wine1']['malolactic'] == res['wine2']['malolactic']:
            if res['wine1']['malolactic'] == 1:
                analysis_text += "Molemmat viinit edustavat pehmeää ja helposti lähestyttävää tyyliä (malolaktinen käyminen sallittu), jossa hapot eivät ole liian kireitä. "
            else:
                analysis_text += "Molemmat ovat hapokkaampia ja ryhdikkäämpiä, koska malolaktinen käyminen on estetty. "
        else:
            analysis_text += "Viineissä on selkeä tyyliero: Le Bullet on suutuntumaltaan pehmeämpi ja pyöreämpi, kun taas verrokki on profiililtaan hapokkaampi ja terävämpi. "

        # Yhteenveto prosentin mukaan
        if res['match_percent'] > 90:
            analysis_text += "Matemaattisesti katsoen reseptit ovat lähes identtiset. Sokkotestissä näiden erottaminen toisistaan vaatisi todellista harjaantuneisuutta, sillä aromimaailman perusta on sama."
        elif res['match_percent'] > 80:
            analysis_text += "Makuprofiileissa on paljon samaa sukulaisuutta. Vaikka pieniä eroja löytyy, Le Bullet tarjoaa hyvin samankaltaisen elämyksen huomattavasti edullisempaan hintaan."
        else:
            analysis_text += "Vaikka molemmat ovat samppanjoita, niiden luonne on erilainen. Le Bullet on todennäköisesti näistä kahdesta hedelmäisempi ja runsaampi, kun taas verrokki edustaa eri koulukuntaa (esim. enemmän Chardonnayta tai eri valmistustyyli)."

        st.info(analysis_text)

else:
    st.info("Valitse ensin samppanja pudotusvalikosta.")

st.divider()
st.caption(
    "Tämä työkalu on tehty viihdekäyttöön. Laskelmat perustuvat rypälesuhteiden, sokerimäärän ja valmistustavan matemaattiseen vertailuun. Hinnat ja linkit ovat viitteellisiä.")