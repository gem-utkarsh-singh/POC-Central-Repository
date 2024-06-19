import requests
from tabulate import tabulate
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG, filename='scheduler.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

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

def send_email(report_html):
    sender_email = "u992744@gmail.com"
    receiver_emails = ["Sanjana.Singh@geminisolutions.com"]  # Add your recipients
    password = "Utkarsh@0912"  # Use an app-specific password if 2FA is enabled

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Demo Links Status Report"
    msg['From'] = sender_email
    msg['To'] = ", ".join(receiver_emails)

    part1 = MIMEText(report_html, 'html')
    msg.attach(part1)

    logging.debug("Sending email")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
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
        ("Starzplay video enhancement POC", "Aditya Singh", "https://videocrop.streamlit.app/"),
        ("Github Bot", "Debarghya Maity", "https://gitbott.streamlit.app/"),        
        ("Financial ChatBot", "Kritadhi Maity", "https://huggingface.co/spaces/maitykritadhi/Kr_Financial_Chatbot_StreamLitUI"),
        ("Credit Scoring model", "Aditya Singh", "n/a"),
        ("Starzplay Multi-modal Search", "Aditya Singh/Prashant Solanki", "n/a"),
        ("Starzplay text translation", "Sushma Piraka", "n/a"),
        ("Trade Surveillence POC", "Aditya Singh/Prashant Solanki", "n/a"),
        ("Gemini Policy Bot", "Debarghya Maity", "n/a"),
        ("Facial Expression Manipulation", "Goutam Sharma", "https://huggingface.co/spaces/goutamsharma/facial-expression-manulplation"),
        ("FAB demo", "Debarghya Maity", "http://52.66.10.81:8002/"),
        ("Airline sentiment analysis", "Nitish John Toppo", "https://usairlinessentimentanalysis-asmerbqllmx35uappbcvamo.streamlit.app"),
        ("Emaar IA Chatbot", "Kritadhi Maity", "https://huggingface.co/spaces/anang150296/Emaar-AI-chatbot"),
        ("Org Structure Construction", "Debarghya Maity", "http://13.232.58.176:8003/"),
        ("QA_GenAI", "Debarghya Maity", "http://13.232.58.176:8004/"),
        ("Sentiment Demo", "Debarghya Maity", "http://13.232.58.176:8001/"),
        ("FX Sentiment Analysis", "Debarghya Maity", "http://13.232.58.176:8002/"),
        ("Emaar Valet AI", "Akshita Ranjan", "http://52.66.10.81:8001/"),
    ]

    report = check_links(demo_links)
    report_table = generate_report(report)
    send_email(report_table)
    logging.info("Daily task completed")

if __name__ == "__main__":
    # For testing, call the daily_task function directly
    daily_task()
