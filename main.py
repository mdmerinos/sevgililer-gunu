import streamlit as st
import streamlit.components.v1 as components

# Sayfa ayarları
st.set_page_config(page_title="Sana Bir Sorum Var ❤️", page_icon="❤️", layout="centered")

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
        #success-message {
            display: none;
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
    <div id="success-message">
        Sevgililer günümüz kutlu olsun baliimmm! 🎀✨
    </div>
</div>

<script>
    function moveButton() {
        const btn = document.getElementById('noBtn');
        // Butonun ekran dışına taşmaması için sınırlar
        const x = Math.random() * (window.innerWidth - btn.offsetWidth);
        const y = Math.random() * (window.innerHeight - btn.offsetHeight);
        
        btn.style.position = 'fixed';
        btn.style.left = x + 'px';
        btn.style.top = y + 'px';
    }

    function celebrate() {
        document.getElementById('content').style.display = 'none';
        document.getElementById('success-message').style.display = 'block';
        
        // Konfeti efekti (isteğe bağlı)
        const duration = 5 * 1000;
        const animationEnd = Date.now() + duration;
    }
</script>

</body>
</html>
"""

# HTML'i Streamlit içine gömüyoruz
components.html(html_code, height=600)

# Streamlit üzerinden arka planı da temizleyelim
st.markdown("""
    <style>
    .stApp {
        background-color: #fff5f7;
    }
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)