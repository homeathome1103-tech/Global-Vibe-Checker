import requests
import datetime

# 1. Get News Data (Your original API)
try:
    api_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=cabd2f02b1904b94a275e060dfd3cc3d'
    response = requests.get(api_url)
    data = response.json()
    headline = data['articles'][0]['title']
except Exception as e:
    headline = "The world is in a transition state..."

# 2. NEW: Get Space Data! (How many people are in space right now?)
try:
    space_res = requests.get('http://api.open-notify.org/astros.json')
    space_data = space_res.json()
    people_in_space = space_data['number']
except:
    people_in_space = "an unknown number of"

# 3. Determine the "Vibe"
vibe = "Steady"
color = "#34495e" # Neutral dark blue/grey

low_headline = headline.lower()
if any(word in low_headline for word in ["good", "win", "discovery", "save", "happy"]):
    vibe = "Optimistic"
    color = "#2ecc71" # Bright Green
elif any(word in low_headline for word in ["war", "crisis", "fire", "bad", "loss", "crash", "defeat"]):
    vibe = "Hectic"
    color = "#e74c3c" # Warning Red
elif any(word in low_headline for word in ["new", "launch", "space", "future"]):
    vibe = "Progressive"
    color = "#9b59b6" # Royal Purple

# 4. Build the Upgraded HTML Page
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Vibe Check</title>
    <style>
        body {{ 
            background-color: {color}; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            height: 100vh; 
            margin: 0;
            color: white; 
            text-align: center; 
            transition: background-color 3s ease; 
        }}
        .container {{ padding: 20px; width: 100%; }}
        h1 {{ font-size: clamp(3rem, 10vw, 6rem); margin: 0; text-transform: uppercase; letter-spacing: 5px; }}
        p {{ font-size: 1.2rem; opacity: 0.9; }}
        .headline {{ font-style: italic; margin-top: 20px; max-width: 600px; line-height: 1.4; margin-left: auto; margin-right: auto; }}
        
        /* New CSS for the cool extra stuff */
        .extras-box {{ margin-top: 40px; padding: 15px 30px; background: rgba(0,0,0,0.2); border-radius: 10px; display: inline-block; font-size: 1.1rem; }}
        .donation-btn {{ margin-top: 30px; }}
        .donation-btn a {{ 
            background-color: #ff813f; 
            color: white; 
            padding: 12px 24px; 
            text-decoration: none; 
            border-radius: 8px; 
            font-weight: bold; 
            transition: 0.2s; 
            display: inline-block;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }}
        .donation-btn a:hover {{ background-color: #e06d35; transform: translateY(-2px); }}
        
        .footer {{ position: absolute; bottom: 20px; font-size: 0.8rem; opacity: 0.6; width: 100%; text-align: center; left: 0; }}
    </style>
</head>
<body>
    <div class="container">
        <p>THE CURRENT WORLD VIBE IS</p>
        <h1>{vibe}</h1>
        <p class="headline">"{headline}"</p>
        
        <div class="extras-box">
            🚀 Humans currently in space: <strong>{people_in_space}</strong>
        </div>

        <br>

        <div class="donation-btn">
            <a href="https://ko-fi.com/" target="_blank">☕ Buy the Robot a Coffee</a>
        </div>
    </div>
    <div class="footer">
        Last synced: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} UTC | Fully Autonomous
    </div>
</body>
</html>
"""

# 5. Save it
with open("index.html", "w") as f:
    f.write(html_content)
