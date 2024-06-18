import requests
from tabulate import tabulate
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from datetime import datetime
import pytz

# Setup logging
logging.basicConfig(level=logging.DEBUG, filename='scheduler.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_links(links):
    status_report = []
    for project_name, project_lead, link in links:
        logging.debug(f"Checking link for project: {project_name}")
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
    logging.debug("Generated report table")
    return table

def send_email(report_html):
    sender_email = "Utkarsh.Singh@geminisolutions.com"
    receiver_emails = ["Sanjana.Singh@geminisolutions.com"]  # Add your recipients
    password = "Dell@123"  # Use your Outlook password or app-specific password if 2FA is enabled

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Demo Links Status Report"
    msg['From'] = sender_email
    msg['To'] = ", ".join(receiver_emails)

    part1 = MIMEText(report_html, 'html')
    msg.attach(part1)

    logging.debug("Sending email")
    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_emails, msg.as_string())
        server.quit()
        logging.info("Email sent successfully")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def daily_task():
    logging.info("Starting daily task")
    demo_links = [
        ("Starzplay video enhancement POC", "", "https://videocrop.streamlit.app/"),
        ("Github Bot", "", "https://gitbott.streamlit.app/"),
        ("FX Sentiment Analysis", "", "http://3.7.234.8:8000/"),
        ("Financial ChatBot", "", "https://huggingface.co/spaces/maitykritadhi/Kr_Financial_Chatbot_StreamLitUI"),
        ("Credit Scoring model", "", "n/a"),
        ("Starzplay Multi-modal Search", "", "n/a"),
        ("Starzplay text translation", "", "n/a"),
        ("Trade Surveillence POC", "", "n/a"),
        ("Gemini Policy Bot", "", "n/a"),
        ("AI virtual Influencer", "", "n/a"),
        ("FAB demo", "", "http://52.66.10.81:8002/"),
        ("Yen Forex Sentiment Analysis", "", "http://15.206.189.243:8503/"),
        ("Sentiment Analysis on PDF Financial Document", "", "http://15.206.189.243:8502/"),
        ("Airline sentiment analysis", "", "https://usairlinessentimentanalysis-asmerbqllmx35uappbcvamo.streamlit.app"),
        ("Emaar AI Chatbot", "", "https://huggingface.co/spaces/anang150296/Emaar-AI-chatbot"),
        ("Org Structure Construction", "", "http://13.232.58.176:8003/"),
        ("QA_GenAI", "", "http://13.232.58.176:8004/"),
        ("Sentiment Demo", "", "http://13.232.58.176:8001/"),
        ("Sentiment Analysis on Company Earnings Call Transcript", "", "http://3.108.236.232:8503/"),
        ("Emaar Valet AI", "", "n/a"),
    ]

    report = check_links(demo_links)
    report_table = generate_report(report)
    send_email(report_table)
    logging.info("Daily task completed")

# For immediate testing, call the task directly
logging.info("Script started")
daily_task()
logging.info("Script finished")
