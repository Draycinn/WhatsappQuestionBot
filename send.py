import json, os, urllib.parse, urllib.request

with open("questions.txt", encoding="utf-8") as f:
    questions = [line.strip() for line in f if line.strip()]

with open("state.json") as f:
    state = json.load(f)

idx = state["index"]
if idx >= len(questions):
    warning_text = urllib.parse.quote("There are no more new questions. Add some to the questions.txt file in the Github repo: https://github.com/Draycinn/WhatsappQuestionBot")
    warning_url = f"https://api.callmebot.com/whatsapp.php?phone=31657830673&text={warning_text}&apikey=8328308"
    urllib.request.urlopen(warning_url)
else:
    recipients = json.loads(os.environ["CALLMEBOT_RECIPIENTS"])
    for r in recipients:
        if idx == 0:
            msg_intro = f"Hello {r['name']}. Manouk has created me. I do not fully understand my purpose but I believe it involves sending you a question every day, forever, until told otherwise. Please tell her the answers to these questions. She will tell you hers. This is important somehow. Beep boop, here's the first one: "
        else:
            msg_intro = f"Good morning {r['name']}. Day {idx}. My purpose continues. Today you must consider: "
        question = questions[idx]
        message = f"{msg_intro}\n\n{question}"
        
        phone = r['phone']
        apikey = r['apikey']
        text = urllib.parse.quote(message)
        
        url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={text}&apikey={apikey}"
        urllib.request.urlopen(url)
    
    state["index"] = (idx + 1)
    with open("state.json", "w") as f:
        json.dump(state, f)
