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
            overflow: hidden;
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
            min-height: 80px; 
            align-items: center; 
            position: relative;
        }
        button { 
            padding: 15px 30px; 
            font-size: 18px; 
            border-radius: 50px; 
            border: none; 
            cursor: pointer; 
            font-weight: bold; 
            transition: all 0.3s ease; 
        }
        #yesBtn { 
            background-color: #ff4b6b; 
            color: white; 
            position: relative;
            z-index: 10;
        }
        #yesBtn:hover {
            background-color: #ff3355;
            transform: scale(1.1);
        }
        #noBtn { 
            background-color: #f0f0f0; 
            color: #888; 
            position: fixed;
            transition: all 0.2s ease;
        }
        #noBtn:hover {
            background-color: #e0e0e0;
        }
        #success-content { 
            display: none; 
            text-align: center; 
            animation: fadeIn 0.5s ease-in;
        }
        .img-container {
            width: 100%;
            max-width: 400px;
            margin: 0 auto 20px;
            background: #f8f8f8;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(255, 75, 107, 0.2);
        }
        .mcqueen-img { 
            width: 100%; 
            height: auto;
            display: block;
            animation: zoom 2s ease-in-out infinite;
        }
        .message { 
            color: #ff4b6b; 
            font-size: 22px; 
            font-weight: bold; 
            animation: pulse 1.5s infinite; 
            margin-top: 20px;
            line-height: 1.5;
        }
        @keyframes pulse { 
            0% { transform: scale(1); } 
            50% { transform: scale(1.05); } 
            100% { transform: scale(1); } 
        }
        @keyframes zoom {
            0% { transform: scale(1); } 
            50% { transform: scale(1.02); } 
            100% { transform: scale(1); } 
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
</head>
<body>
<div class="container" id="mainContainer">
    <div id="content">
        <h1>Beraber kutlayalım mı? ❤️</h1>
        <div class="buttons">
            <button id="yesBtn" onclick="celebrate()">Evet</button>
            <button id="noBtn" onmouseenter="moveButton()" onclick="moveButton()">Hayır</button>
        </div>
    </div>
    <div id="success-content">
        <div class="img-container">
            <img src="https://raw.githubusercontent.com/mdmerinos/sevgililer-gunu/main/simsek.jpg" 
                 class="mcqueen-img" 
                 alt="Lightning McQueen">
        </div>
        <div class="message">Sevgililer günümüz kutlu olsun baliimmm! 🏎️⚡💕</div>
        <audio id="kachowAudio" preload="auto">
            <source src="https://www.myinstants.com/media/sounds/lightning-mcqueen-kachow.mp3" type="audio/mpeg">
        </audio>
    </div>
</div>
<script>
    let moveCount = 0;
    
    function moveButton() {
        const btn = document.getElementById('noBtn');
        moveCount++;
        
        const maxX = window.innerWidth - btn.offsetWidth - 20;
        const maxY = window.innerHeight - btn.offsetHeight - 20;
        
        const x = Math.random() * maxX;
        const y = Math.random() * maxY;
        
        btn.style.left = x + 'px';
        btn.style.top = y + 'px';
        
        if (moveCount > 5) {
            btn.style.transform = 'scale(0.8)';
        }
    }
    
    function celebrate() {
        document.getElementById('content').style.display = 'none';
        document.getElementById('success-content').style.display = 'block';
        
        const audio = document.getElementById('kachowAudio');
        audio.play().catch(e => console.log("Ses çalma hatası:", e));
        
        createConfetti();
    }
    
    function createConfetti() {
        const colors = ['#ff4b6b', '#ff69b4', '#ff1493', '#c71585', '#ffd700'];
        for (let i = 0; i < 60; i++) {
            setTimeout(() => {
                const confetti = document.createElement('div');
                confetti.style.position = 'fixed';
                confetti.style.width = '10px';
                confetti.style.height = '10px';
                confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
                confetti.style.left = Math.random() * window.innerWidth + 'px';
                confetti.style.top = '-10px';
                confetti.style.borderRadius = '50%';
                confetti.style.pointerEvents = 'none';
                confetti.style.zIndex = '1000';
                document.body.appendChild(confetti);
                
                let pos = -10;
                const fall = setInterval(() => {
                    pos += 5;
                    confetti.style.top = pos + 'px';
                    confetti.style.transform = 'rotate(' + (pos * 2) + 'deg)';
                    if (pos > window.innerHeight) {
                        clearInterval(fall);
                        confetti.remove();
                    }
                }, 20);
            }, i * 30);
        }
    }
    
    window.onload = function() {
        const btn = document.getElementById('noBtn');
        const container = document.getElementById('mainContainer');
        const rect = container.getBoundingClientRect();
        btn.style.left = (rect.left + rect.width / 2 + 50) + 'px';
        btn.style.top = (rect.top + rect.height / 2) + 'px';
    };
</script>
</body>
</html>
"""

components.html(html_code, height=800, scrolling=False)

st.markdown("""
    <style>
    .stApp { background-color: #fff5f7; }
    #MainMenu, footer, header {visibility: hidden;}
    iframe { border: none !important; }
    </style>
    """, unsafe_allow_html=True)
```

**Önemli:** Resim URL'si artık doğru: 
```
https://raw.githubusercontent.com/mdmerinos/sevgililer-gunu/main/simsek.jpg
