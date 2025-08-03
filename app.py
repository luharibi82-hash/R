import requests

# Telegram Bot Token and Chat ID
TELEGRAM_BOT_TOKEN = "7868347273:AAEl6-fJ_NodbyDnlML0TolyfDNHfDwablw"
CHAT_ID = "-1002280058526"
API_URL = "http://webx.ct.ws/api.php?id=cc6626"

def fetch_text_from_api():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad status codes
        # Assuming the API returns JSON with a 'text' field; adjust based on actual API response
        data = response.json()
        return data.get("text", "No text found in API response")
    except requests.exceptions.RequestException as e:
        return f"Error fetching text: {str(e)}"
    except ValueError:
        # Handle case where response is not JSON
        return response.text if response.text else "Empty response from API"

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"  # Optional: Use "HTML" or remove for plain text
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"ok": False, "description": str(e)}

# Fetch text and send to Telegram
text = fetch_text_from_api()
result = send_to_telegram(text)
if result.get("ok"):
    print("Message sent successfully!")
else:
    print(f"Failed to send message: {result.get('description')}")
