from pathlib import Path


MESSAGES_FILE = Path(__file__).with_name("sample_messages.txt")


def load_messages(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    messages = content.split("---")

    cleaned_messages = []

    for message in messages:
        message = message.strip()

        if message:
            cleaned_messages.append(message)

    return cleaned_messages


def classify_risk(score):
    if score >= 6:
        return "High Risk"
    elif score >= 3:
        return "Medium Risk"
    else:
        return "Low Risk"


def analyze_message(message):
    lower_message = message.lower()

    score = 0
    red_flags = []

    urgency_keywords = [
        "urgent", "immediately", "act now", "within 30 minutes",
        "limited-time", "failure to act", "permenant suspension"
    ]

    sensitive_keywords = [
        "password", "mfa code", "otp", "username",
        "personal details", "payment confirmation"
    ]

    reward_keywords = [
        "congratulations", "winner", "prize", "free gift",
        "claim your prize"
    ]

    authority_keywords = [
        "ceo", "wire transfer", "stricktly confidential",
        "do not discuss", "process this transfer"
    ]

    suspicious_link_keywords = [
        "http://", "secure-login", "verify-account", 
        "free-gift-claim", "company-security-check"
    ]

    if any(keyword in lower_message for keyword in urgency_keywords):
        score += 2
        red_flags.append("Urgent or pressure-based language detected")

    if any(keyword in lower_message for keyword in sensitive_keywords):
        score += 4 
        red_flags.append("Request for sensitive information detected")

    if any(keyword in lower_message for keyword in reward_keywords):
        score += 2
        red_flags.append("Reward or prize lure detected")

    if any(keyword in lower_message for keyword in authority_keywords):
        score += 3
        red_flags.append("Authority impersonation or financial request detected")

    if any(keyword in lower_message for keyword in suspicious_link_keywords):
        score += 3
        red_flags.append("Suspicious link or suspicious domain pattern")

    risk_level = classify_risk(score)

    return score, risk_level, red_flags


def generate_explanation(risk_level, red_flags):
    if not red_flags:
        return "This message appears low risk because no major phishing red flags were detected."

    explanation_parts = []

    for flag in red_flags:
        if "Urgent" in flag:
            explanation_parts.append("it uses urgent or pressure-based language to push the user to act quickly")

        elif "sensitive information" in flag:
            explanation_parts.append("it asks for sensitive information such as passwords, MFA codes, personal details, or payment confirmation")
        
        elif "Reward" in flag:
            explanation_parts.append("it uses a reward or prize lure to attract the user")

        elif "Authority" in flag:
            explanation_parts.append("it uses authority impersonation or financial pressure")
        
        elif "Suspicious" in flag:
            explanation_parts.append("it contains a suspicious link or domain pattern")

    return f"This message is classified as {risk_level} because " + "; ".join(explanation_parts) + "."


def display_analysis(messages):
    print("\nPhishing Awareness Analysis:")

    for index, message in enumerate(messages, start=1):
        score, risk_level, red_flags = analyze_message(message)
        explanation = generate_explanation(risk_level, red_flags)

        print(f"\nMessage {index}:")
        print(f"Risk Score: {score}")
        print(f"Risk Level: {risk_level}")

        if red_flags:
            print("Red Flags Found:")
            for flag in red_flags:
                print(f"- {flag}")

        else:
            print("Red Flags Found: None")

        print("Explanation:")
        print(explanation)

        print("-" * 50)


def display_messages(messages):
    print("\nLoaded Messages:")

    for index, message in enumerate(messages, start=1):
        print(f"\nMessage {index}:")
        print(message)
        print("-" * 50)


def main():
    messages = load_messages(MESSAGES_FILE)

    print(f"\nTotal Messages Loaded: {len(messages)}")

    display_analysis(messages)


if __name__ == "__main__":
    main()