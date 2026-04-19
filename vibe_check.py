import requests
import datetime

# 1. Get data using your NewsAPI key
try:
    # We use your specific key here to fetch the latest top headlines
    api_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=cabd2f02b1904b94a275e060dfd3cc3d'
    response = requests.get(api_url)
    data = response.json()
    
    # Pick the very first headline found
    headline = data['articles'][0]['title']
except Exception as e:
    headline = "The world is in a transition state..."

# 2. Determine the "Vibe" based on keywords in the headline
vibe = "Steady"
color = "#34495e" # A neutral dark blue/grey

# This is the 'logic' that makes the site feel alive
low_headline = headline.lower()
if any(word in low_headline for word in ["good", "win", "discovery", "save", "happy"]):
    vibe = "Optimistic"
    color = "#2ecc71" # Bright Green
elif any(word in low_headline for word in ["war", "crisis", "fire", "bad", "loss", "crash"]):
    vibe = "Hectic"
    color = "#e74c3c" # Warning Red
elif any(word in low_headline for word in ["new", "launch", "space", "future"]):
    vibe = "Progressive"
    color = "#9b59b6" # Royal Purple

# 3. Build the actual HTML page
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
        .container {{ padding: 20px; }}
        h1 {{ font-size: clamp(3rem, 10vw, 6rem); margin: 0; text-transform: uppercase; letter-spacing: 5px; }}
        p {{ font-size: 1.2rem; opacity: 0.9; }}
        .headline {{ font-style: italic; margin-top: 20px; max-width: 600px; line-height: 1.4; }}
        .footer {{ position: absolute; bottom: 20px; font-size: 0.8rem; opacity: 0.6; }}
    </style>
</head>
<body>
    <div class="container">
        <p>THE CURRENT WORLD VIBE IS</p>
        <h1>{vibe}</h1>
        <p class="headline">"{headline}"</p>
    </div>
    <div class="footer">
        Last synced: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} UTC | Fully Autonomous
    </div>
</body>
</html>
"""

# 4. Save the file so GitHub can host it
with open("index.html", "w") as f:
    f.write(html_content)
