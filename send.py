import json, os, urllib.parse, urllib.request

with open("questions.txt", encoding="utf-8") as f:
    sentences = [line.strip() for line in f if line.strip()]

with open("state.json") as f:
    state = json.load(f)

idx = state["index"] % len(sentences)
message = sentences[idx]

phone = os.environ["CALLMEBOT_PHONE"]
apikey = os.environ["CALLMEBOT_APIKEY"]
text = urllib.parse.quote(message)

url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={text}&apikey={apikey}"
urllib.request.urlopen(url)

state["index"] = (idx + 1) % len(sentences)
with open("state.json", "w") as f:
    json.dump(state, f)
