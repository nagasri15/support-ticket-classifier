from pathlib import Path
import joblib


# ---------------------------------------------------------
# Load trained model
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "ticket_classifier.pkl"

model = joblib.load(MODEL_PATH)


# ---------------------------------------------------------
# Predict ticket category
# ---------------------------------------------------------

def predict_category(ticket_text):
    """
    Predict the category of a support ticket.
    """

    if not ticket_text or not ticket_text.strip():
        return "Please enter a support ticket."

    prediction = model.predict([ticket_text])[0]

    return prediction


# ---------------------------------------------------------
# Urgency detection
# ---------------------------------------------------------

def predict_urgency(ticket_text):
    """
    Detect ticket urgency using simple keyword rules.
    """

    text = ticket_text.lower()

    high_urgency_words = [
        "urgent",
        "urgently",
        "immediately",
        "asap",
        "emergency",
        "critical",
        "right away"
    ]

    medium_urgency_words = [
        "not working",
        "doesn't work",
        "does not work",
        "failed",
        "failure",
        "problem",
        "issue",
        "error",
        "cannot",
        "can't",
        "unable",
        "locked",
        "crash",
        "crashed",
        "bug",
        "broken",
        "not charging",
        "can't connect",
        "cannot connect"
    ]

    # Check High first
    if any(word in text for word in high_urgency_words):
        return "High"

    # Then Medium
    if any(word in text for word in medium_urgency_words):
        return "Medium"

    # Otherwise Low
    return "Low"


# ---------------------------------------------------------
# Complete ticket classification
# ---------------------------------------------------------

def classify_ticket(ticket_text):
    """
    Return both category and urgency.
    """

    if not ticket_text or not ticket_text.strip():
        return {
            "category": "Unknown",
            "urgency": "Unknown"
        }

    category = predict_category(ticket_text)
    urgency = predict_urgency(ticket_text)

    return {
        "category": category,
        "urgency": urgency
    }