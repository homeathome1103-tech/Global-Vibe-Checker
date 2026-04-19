import requests
import datetime

# 1. Fetch News
try:
    api_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=cabd2f02b1904b94a275e060dfd3cc3d'
    response = requests.get(api_url)
    data = response.json()
    headline = data['articles'][0]['title']
except Exception as e:
    headline = "The world is resting right now."

# 2. Fetch Space Data
try:
    space_res = requests.get('http://api.open-notify.org/astros.json')
    space_data = space_res.json()
    people_in_space = space_data['number']
except:
    people_in_space = "?"

# 3. Vibe Logic & Colors (Upgraded to Gradients!)
vibe = "Steady"
theme_gradient = "linear-gradient(135deg, #2c3e50, #000000)" # Dark Space

low_headline = headline.lower()
if any(word in low_headline for word in ["good", "win", "discovery", "save", "happy", "growth"]):
    vibe = "Optimistic"
    theme_gradient = "linear-gradient(135deg, #0ba360, #3cba92)" # Cyber Green
elif any(word in low_headline for word in ["war", "crisis", "fire", "bad", "loss", "crash", "defeat"]):
    vibe = "Hectic"
    theme_gradient = "linear-gradient(135deg, #ff416c, #ff4b2b)" # Alert Red
elif any(word in low_headline for word in ["new", "launch", "space", "future", "ai", "tech"]):
    vibe = "Progressive"
    theme_gradient = "linear-gradient(135deg, #8E2DE2, #4A00E0)" # Neon Purple

# 4. The "Way Cooler" HTML Dashboard
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
    <title>Global Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; }}
        body {{
            margin: 0;
            padding: 0;
            min-height: 100vh;
            font-family: 'Space Grotesk', sans-serif;
            background: {theme_gradient};
            color: #ffffff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            overflow-x: hidden;
        }}
        /* The Glass Panel Effect */
        .glass-panel {{
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 40px;
            max-width: 800px;
            width: 90%;
            text-align: center;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            animation: float 6s ease-in-out infinite;
        }}
        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-10px); }}
            100% {{ transform: translateY(0px); }}
        }}
        h2 {{ font-size: 1.2rem; text-transform: uppercase; letter-spacing: 4px; opacity: 0.7; margin-bottom: 10px; }}
        h1 {{ font-size: clamp(3rem, 8vw, 5rem); margin: 0 0 20px 0; text-shadow: 0 0 20px rgba(255,255,255,0.4); }}
        .news-ticker {{
            font-size: 1.2rem;
            font-style: italic;
            padding: 20px;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 12px;
            margin-bottom: 30px;
            border-left: 4px solid rgba(255,255,255,0.5);
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: rgba(0, 0, 0, 0.2);
            padding: 20px;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.05);
            transition: 0.3s;
        }}
        .stat-card:hover {{ background: rgba(255,255,255,0.1); }}
        .stat-value {{ font-size: 2.5rem; font-weight: bold; margin: 10px 0; }}
        .stat-label {{ font-size: 0.9rem; opacity: 0.7; text-transform: uppercase; letter-spacing: 2px; }}
        
        /* The upgraded Donation Button */
        .donate-btn {{
            background: linear-gradient(45deg, #ff6b6b, #ff8e53);
            color: white;
            text-decoration: none;
            padding: 15px 30px;
            border-radius: 30px;
            font-weight: bold;
            font-size: 1.1rem;
            display: inline-block;
            transition: transform 0.3s, box-shadow 0.3s;
            border: none;
        }}
        .donate-btn:hover {{
            transform: scale(1.05);
            box-shadow: 0 0 20px rgba(255, 107, 107, 0.6);
        }}
        
        .footer {{ margin-top: 30px; font-size: 0.8rem; opacity: 0.5; }}
        
        /* Green pulsing dot for "Live" status */
        .pulse {{
            display: inline-block;
            width: 12px;
            height: 12px;
            background-color: #4ade80;
            border-radius: 50%;
            margin-right: 10px;
            animation: pulsing 2s infinite;
        }}
        @keyframes pulsing {{
            0% {{ box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7); }}
            70% {{ box-shadow: 0 0 0 10px rgba(74, 222, 128, 0); }}
            100% {{ box-shadow: 0 0 0 0 rgba(74, 222, 128, 0); }}
        }}
    </style>
</head>
<body>
    <div class="glass-panel">
        <h2><span class="pulse"></span>Live Global Vibe</h2>
        <h1>{vibe}</h1>
        
        <div class="news-ticker">
            "{headline}"
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-label">Humans in Space</div>
                <div class="stat-value">🧑‍🚀 {people_in_space}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">System Status</div>
                <div class="stat-value">⚡ Online</div>
            </div>
        </div>

        <a href="https://ko-fi.com/vibecheck111" target="_blank" class="donate-btn">☕ Support the Robot</a>
        
        <div class="footer">
            Autonomous Update: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} UTC
        </div>
    </div>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)
