import streamlit as st
import streamlit.components.v1 as components

# Sayfa ayarları
st.set_page_config(page_title="Sana Bir Sorum Var ❤️", page_icon="🏎️", layout="centered")

# CSS ve JavaScript içeren HTML kodu
html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            background-color: #fff5f7;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        }
        .container {
            text-align: center;
            background: white;
            padding: 40px;
            border-radius: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            width: 85%;
            max-width: 450px;
            position: relative;
        }
        h1 { color: #ff4b6b; margin-bottom: 30px; font-size: 24px; }
        .buttons { display: flex; justify-content: center; gap: 20px; height: 60px; align-items: center; }
        button {
            padding: 12px 25px;
            font-size: 18px;
            border-radius: 50px;
            border: none;
            cursor: pointer;
            font-weight: bold;
            transition: 0.2s;
        }
        #yesBtn { background-color: #ff4b6b; color: white; }
        #noBtn { background-color: #f0f0f0; color: #888; position: absolute; }
        #success-content { display: none; text-align: center; }
        .mcqueen-img {
            width: 100%;
            max-width: 320px;
            border-radius: 15px;
            margin-bottom: 20px;
        }
        .message { color: #ff4b6b; font-size: 20px; font-weight: bold; }
    </style>
</head>
<body>

<div class="container" id="mainContainer">
    <div id="content">
        <h1>Beraber kutlayalım mı? ❤️</h1>
        <div class="buttons">
            <button id="yesBtn" onclick="celebrate()">Evet</button>
            <button id="noBtn" onmouseover="moveButton()">Hayır</button>
        </div>
    </div>

    <div id="success-content">
        <img src="https://media.tenor.com/T_7m_G_V67QAAAAC/lightning-mcqueen-cars.gif" class="mcqueen-img">
        <div class="message">Sevgililer günümüz kutlu olsun baliimmm! 🏎️⚡</div>
        <audio id="kachowAudio">
            <source src="https://www.myinstants.com/media/sounds/lightning-mcqueen-kachow.mp3" type="audio/mpeg">
        </audio>
    </div>
</div>

<script>
    function moveButton() {
        const btn = document.getElementById('noBtn');
        const x = Math.random() * (window.innerWidth - btn.offsetWidth);
        const y = Math.random() * (window.innerHeight - btn.offsetHeight);
        btn.style.position = 'fixed';
        btn.style.left = x + 'px';
        btn.style.top = y + 'px';
    }

    function celebrate() {
        document.getElementById('content').style.display = 'none';
        document.getElementById('success-content').style.display = 'block';
        const audio = document.getElementById('kachowAudio');
        audio.play().catch(e => console.log("Ses çalma hatası:", e));
    }
</script>

</body>
</html>
"""

components.html(html_code, height=600)

# Streamlit tasarımını temizle
st.markdown("""
    <style>
    .stApp { background-color: #fff5f7; }
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
