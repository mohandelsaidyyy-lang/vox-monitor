import requests

BOT_TOKEN = ""
CHAT_ID = ""

URL = "https://egy.voxcinemas.com/showtimes?c=city-centre-almaza&m=spider-man-brand-new-day&d=20260805"

html = requests.get(URL, timeout=30).text.lower()

keywords = [
    "12:00",
    "book",
    "available",
    "imax",
    "standard",
    "vip",
    "dolby"
]

opened = any(word in html for word in keywords)

if opened:
    message = (
        "🎉 Spider-Man bookings for Thursday 6 August "
        "are now available at VOX City Centre Almaza!\n\n"
        + URL
    )

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=30
    )
