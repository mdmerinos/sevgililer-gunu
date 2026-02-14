import streamlit as st
import streamlit.components.v1 as components

# Sayfa ayarları
st.set_page_config(page_title="Sana Bir Sorum Var ❤️", page_icon="🏎️", layout="centered")

# CSS, JavaScript ve McQueen Medya İçeren HTML kodu
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
            padding: 50px;
            border-radius: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            width: 80%;
            max-width: 500px;
            position: relative;
        }
        h1 {
            color: #ff4b6b;
            margin-bottom: 30px;
        }
        .buttons {
            display: flex;
            justify-content: center;
            gap: 20px;
            height: 60px;
            align-items: center;
        }
        button {
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 50px;
            border: none;
            cursor: pointer;
            font-weight: bold;
            transition: transform 0.2s;
        }
        #yesBtn {
            background-color: #ff4b6b;
            color: white;
        }
        #noBtn {
            background-color: #f0f0f0;
            color: #888;
            position: absolute;
        }
        #success-content {
            display: none;
            text-align: center;
        }
        .mcqueen-img {
            width: 250px;
            border-radius: 15px;
            margin-bottom: 20px;
        }
        .message {
            color: #ff4b6b;
            font-size: 24px;
            font-weight: bold;
            animation: heartBeat 1.2s infinite;
        }
        @keyframes heartBeat {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
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
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXF4eXJueXF4eXJueXF4eXJueXF4eXJueXF4eXJueXF4&ep=v1_gifs_search&rid=giphy.gif&ct=g" class="mcqueen-img">
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
        // Eski içeriği gizle
        document.getElementById('content').style.display = 'none';
        // Yeni içeriği göster
        document.getElementById('success-content').style.display = 'block';
        // Sesi çal
        const audio = document.getElementById('kachowAudio');
        audio.play();
    }
</script>

</body>
</html>
"""

# HTML'i Streamlit içine gömüyoruz
components.html(html_code, height=600)

# Streamlit tasarım düzenlemeleri
st.markdown("""
    <style>
    .stApp {
        background-color: #fff5f7;
    }
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
