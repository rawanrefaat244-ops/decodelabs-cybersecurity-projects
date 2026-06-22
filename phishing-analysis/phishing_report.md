# Phishing Awareness Analysis Report

## Project
DecodeLabs Cyber Security Project 3: Phishing Awareness Analysis

## Project Objective
The objective of this project is to analyze sample emails or messages to identify possible phishing attempts.

The analysis focuses on detecting suspicious keywords, suspicious links or domain patterns, phishing red flags, and explaining why each suspicious message may be unsafe.

---

## Project Files

- `sample_messages.txt`: Contains the sample messages used for analysis.
- `phishing_analyzer.py`: Python script used to analyze messages and detect phishing indicators.
- `phishing_report.md`: Final report summarizing the project logic, results, and findings.

---

## Methodology

The project uses a simple rule-based phishing analyzer.

The script reads sample messages from `sample_messages.txt`, separates them into individual messages, converts each message to lowercase, and checks for common phishing indicators.

The analyzer checks for:

- Urgent or pressure-based language
- Requests for sensitive information
- Reward or prize lures
- Authority impersonation or financial requests
- Suspicious links or suspicious domain patterns

Each detected indicator adds to the message risk score. The final score is used to classify the message as Low Risk, Medium Risk, or High Risk.

---

## Risk Scoring System

| Indicator | Score |
|---|---:|
| Urgent or pressure-based language | +2 |
| Request for sensitive information | +4 |
| Reward or prize lure | +2 |
| Authority impersonation or financial request | +3 |
| Suspicious link or suspicious domain pattern | +3 |

## Risk Levels

| Score Range | Risk Level |
|---|---|
| 0–2 | Low Risk |
| 3–5 | Medium Risk |
| 6 or more | High Risk |

---

## Analysis Results

| Message | Risk Score | Risk Level | Main Red Flags |
|---|---:|---|---|
| Message 1 | 0 | Low Risk | No major phishing red flags detected |
| Message 2 | 9 | High Risk | Urgency, sensitive information request, suspicious link/domain pattern |
| Message 3 | 11 | High Risk | Reward lure, urgency, sensitive information request, suspicious link/domain pattern |
| Message 4 | 9 | High Risk | Authority impersonation, urgent wire transfer request, secrecy |
| Message 5 | 7 | High Risk | Request for username, password, MFA code, suspicious domain pattern |

---

## Message Findings

### Message 1
Message 1 was classified as Low Risk because no major phishing indicators were detected. It appears to be a normal team meeting reminder.

### Message 2
Message 2 was classified as High Risk because it creates urgency by warning that the account will be locked. It also asks the user to verify a password through a suspicious link.

### Message 3
Message 3 was classified as High Risk because it uses a prize or gift card lure to attract the user. It also asks for personal details through a suspicious link.

### Message 4
Message 4 was classified as High Risk because it appears to impersonate a CEO and requests an immediate wire transfer. It also uses secrecy by saying the request is confidential and should not be discussed.

### Message 5
Message 5 was classified as High Risk because it asks for a username, password, and MFA code. A real IT support team should never ask users to send passwords or MFA codes by email.

---

## Key Phishing Red Flags Identified

The project identified the following phishing red flags:

1. Urgent language that pressures the user to act quickly
2. Requests for passwords, usernames, MFA codes, or personal information
3. Suspicious links or suspicious domain patterns
4. Prize or reward-based lures
5. CEO or authority impersonation
6. Financial requests such as wire transfers
7. Secrecy-based wording such as strictly confidential or do not discuss

---

## Security Awareness Lessons

Users should follow these security practices:

- Do not share passwords by email.
- Do not share MFA codes with anyone.
- Do not click suspicious links.
- Verify the sender’s email address carefully.
- Be careful with urgent messages that pressure immediate action.
- Verify financial requests using a trusted communication channel.
- Report suspicious messages to the IT or security team.

---

## Limitations

This project uses a simple rule-based analyzer. It can detect common phishing indicators, but it has some limitations:

- It may not detect advanced phishing messages.
- It may flag normal messages if they contain suspicious words.
- It does not analyze real email headers.
- It does not check live domain reputation.
- It does not open or scan links.
- It does not use machine learning.

The purpose of this project is phishing awareness and basic threat identification, not full enterprise-level phishing detection.

---

## Conclusion

This project demonstrates how sample messages can be analyzed to identify possible phishing attempts.

The analyzer detected suspicious keywords, sensitive information requests, suspicious domain patterns, reward lures, urgency tactics, and authority impersonation.

Out of five messages, one message was classified as Low Risk and four messages were classified as High Risk.

Overall, this project shows how phishing red flags can be detected, scored, classified, and explained in a structured and professional way.