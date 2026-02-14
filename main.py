import streamlit as st
import streamlit.components.v1 as components

# Sayfa ayarları
st.set_page_config(page_title="Sana Bir Sorum Var ❤️", page_icon="🏎️", layout="centered")

# HTML kodu
html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            background-color: #fff5f7; 
            font-family: 'Arial', sans-serif; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            min-height: 100vh; 
            padding: 20px;
        }
        .container { 
            text-align: center; 
            background: white; 
            padding: 40px; 
            border-radius: 30px; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.1); 
            width: 100%; 
            max-width: 500px; 
            position: relative; 
        }
        h1 { 
            color: #ff4b6b; 
            margin-bottom: 30px; 
            font-size: 24px; 
        }
        .buttons { 
            display: flex; 
            justify-content: center; 
            gap: 20px; 
            min-height: 60px; 
            align-items: center; 
            position: relative;
        }
        button { 
            padding: 12px 25px; 
            font-size: 18px; 
            border-radius: 50px; 
            border: none; 
            cursor: pointer; 
            font-weight: bold; 
            transition: 0.2s; 
        }
        #yesBtn { 
            background-color: #ff4b6b; 
            color: white; 
            position: relative;
            z-index: 10;
        }
        #yesBtn:hover {
            background-color: #ff3355;
            transform: scale(1.05);
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
            width: 100%; 
            height: auto;
            max-width: 400px; 
            border-radius: 20px; 
            margin-bottom: 20px; 
            box-shadow: 0 5px 15px rgba(255, 75, 107, 0.2);
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        .message { 
            color: #ff4b6b; 
            font-size: 20px; 
            font-weight: bold; 
            animation: pulse 1.5s infinite; 
            margin-top: 15px;
        }
        @keyframes pulse { 
            0% { transform: scale(1); } 
            50% { transform: scale(1.05); } 
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
        <img src="https://media.tenor.com/T_7m_G_V67QAAAAC/lightning-mcqueen-cars.gif" 
             class="mcqueen-img" 
             alt="Lightning McQueen">
        <div class="message">Sevgililer günümüz kutlu olsun baliimmm! 🏎️⚡</div>
        <audio id="kachowAudio">
            <source src="https://www.myinstants.com/media/sounds/lightning-mcqueen-kachow.mp3" type="audio/mpeg">
        </audio>
    </div>
</div>
<script>
    function moveButton() {
        const btn = document.getElementById('noBtn');
        const container = document.getElementById('mainContainer');
        const containerRect = container.getBoundingClientRect();
        
        const maxX = containerRect.width - btn.offsetWidth - 40;
        const maxY = containerRect.height - btn.offsetHeight - 40;
        
        const x = Math.random() * maxX + 20;
        const y = Math.random() * maxY + 20;
        
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

# HTML component'i daha yüksek bir height ile render et
components.html(html_code, height=700, scrolling=False)

# Streamlit stil düzenlemeleri
st.markdown("""
    <style>
    .stApp { background-color: #fff5f7; }
    #MainMenu, footer, header {visibility: hidden;}
    iframe { border: none !important; }
    </style>
    """, unsafe_allow_html=True)
