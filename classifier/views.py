from django.shortcuts import render

history = []

def index(request):
    result = None
    suspicious_words = []
    spam_score = 0
    category = "Safe"

    spam_keywords = {
        "win": 15,
        "free": 10,
        "offer": 10,
        "money": 15,
        "click": 10,
        "urgent": 15,
        "prize": 15,
        "lottery": 20,
        "claim": 10,
        "limited": 10,
        "bonus": 10,
        "discount": 10,
        "cash": 15,
        "congratulations": 15,
    }

    if request.method == "POST":
        message = request.POST.get("message", "")
        lower_message = message.lower()

        suspicious_words = [word for word in spam_keywords if word in lower_message]
        spam_score = sum(spam_keywords[word] for word in suspicious_words)

        if spam_score > 100:
            spam_score = 100

        if spam_score >= 40:
            result = "Spam"
        else:
            result = "Not Spam"

        if "lottery" in lower_message or "prize" in lower_message:
            category = "Prize Scam"
        elif "offer" in lower_message or "discount" in lower_message:
            category = "Promotional"
        elif "urgent" in lower_message or "claim" in lower_message:
            category = "Urgent Alert"
        else:
            category = "General"

        history.insert(0, {
            "text": message[:50] + ("..." if len(message) > 50 else ""),
            "result": result,
            "score": spam_score,
            "category": category
        })

        if len(history) > 5:
            history.pop()

    return render(request, "classifier/index.html", {
        "result": result,
        "suspicious_words": suspicious_words,
        "spam_score": spam_score,
        "category": category,
        "history": history
    })