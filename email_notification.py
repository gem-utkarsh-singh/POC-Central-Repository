import smtplib, ssl
import requests
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465  # For SSL
password = "nfmrjxivowbykzjh"

# Create a secure SSL context
context = ssl.create_default_context()
sender_email = "poc.status.notification@gmail.com"
receiver_emails = ["anang.tomar@geminisolutions.com", "utkarsh.singh@geminisolutions.com"]


def send_email(report_html):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Demo Links Status Report"
    msg['From'] = sender_email
    msg['To'] = ", ".join(receiver_emails)

    part1 = MIMEText(report_html, 'html')
    msg.attach(part1)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_emails, msg.as_string())


def check_links(links):
    status_report = []
    for project_name, project_lead, link in links:
        if link == "n/a":
            status = "Project not deployed"
        else:
            try:
                response = requests.get(link, timeout=10)
                if response.status_code == 200:
                    status = "OK"
                else:
                    status = f"Fail: HTTP {response.status_code}"
            except requests.RequestException as e:
                status = f"Fail: {e}"

        status_report.append((project_name, project_lead, link, status))
    return status_report


def generate_report(report):
    headers = ["Project Name", "Project Lead", "Demo Link", "Status"]
    table = tabulate(report, headers=headers, tablefmt="html")
    return table

def daily_task():
    demo_links = [
        ("Starzplay video Enhancement POC", "Aditya Singh", "https://videocrop.streamlit.app/"),
        ("Github Bot", "Chaitanya Raj", "https://gitbott.streamlit.app/"),
        
        ("FinBot - A Financial ChatBot", "Kritadhi Maity", "https://huggingface.co/spaces/maitykritadhi/Kr_Financial_Chatbot_StreamLitUI"),
        ("Credit Scoring model", "Aditya Singh", "n/a"),
        ("Starzplay Multi-modal Search", "Aditya Singh/Prashant Solanki", "n/a"),
        ("LingoBot", "Sushma Piraka", "n/a"),
        ("Trade Guard", "Aditya Singh/Prashant Solanki", "n/a"),
        ("Gemini Policy Bot", "Debarghya Maity", "n/a"),
        ("Facial Expression Manipulation", "Goutam Sharma", "https://huggingface.co/spaces/goutamsharma/facial-expression-manulplation"),
        ("Document Information Retrieval Bot", "Debarghya Maity", "http://52.66.10.81:8002/"),
       
       
        ("Sentiment Insights", "Nitish John Toppo", "https://usairlinessentimentanalysis-asmerbqllmx35uappbcvamo.streamlit.app"),
        ("Document Intelligence Bot", "Kritadhi Maity", "https://huggingface.co/spaces/anang150296/Emaar-AI-chatbot"),
        ("Org Structure Construction", "Debarghya Maity", "http://13.232.58.176:8003/"),
        ("QA_GenAI", "Debarghya Maity", "http://13.232.58.176:8004/"),
        ("Sentiment Demo", "Debarghya Maity", "http://13.232.58.176:8001/"),
        ("Forex Trends", "Debarghya Maity", "http://13.232.58.176:8002/"),
       
        ("Park Easy", "Akshita Ranjan", "http://52.66.10.81:8001/"),
    ]

    report = check_links(demo_links)
    report_table = generate_report(report)
    send_email(report_table)


if __name__ == "__main__":
    daily_task()
