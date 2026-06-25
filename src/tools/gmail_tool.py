from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import os

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]


def get_gmail_service():

    creds = None

    if os.path.exists("../../secrets/token.pickle"):
        with open("../../secrets/token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds:

        flow = InstalledAppFlow.from_client_secrets_file(
            "../../secrets/credentials.json",
            SCOPES
        )

        creds = flow.run_local_server(port=0)

        with open("../../secrets/token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build(
        "gmail",
        "v1",
        credentials=creds
    )

    return service

def get_top_emails(limit=5):
    try:
        service = get_gmail_service()

        results = service.users().messages().list(
            userId="me",
            maxResults=limit
        ).execute()

        messages = results.get("messages", [])
        emails = []

        for msg in messages:
            message = service.users().messages().get(
                userId="me",
                id=msg["id"]
            ).execute()

            headers = message["payload"]["headers"]

            subject = next(
                (h["value"] for h in headers if h["name"] == "Subject"),
                "No Subject"
            )

            sender = next(
                (h["value"] for h in headers if h["name"] == "From"),
                "Unknown Sender"
            )

            emails.append({
                "sender": sender,
                "subject": subject,
                "snippet": message.get("snippet", "")
            })

        return emails

    except FileNotFoundError:
        return [{
            "sender": "System",
            "subject": "Gmail not configured on Streamlit Cloud",
            "snippet": "Gmail works locally because credentials.json and token.pickle exist on your Mac. For cloud deployment, Gmail OAuth needs separate setup."
        }]