import smtplib
import ssl
import requests
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from pytz import timezone

port = 465  # For SSL
password = "nfmrjxivowbykzjh"

# Create a secure SSL context
context = ssl.create_default_context()
sender_email = "poc.status.notification@gmail.com"
receiver_emails = ["utkarsh.singh@geminisolutions.com", "sudhanshu.malhotra@geminisolutions.com", "prashant.solanki@geminisolutions.com",
                   "aditya.singh1@geminisolutions.com", "saurav.anand@geminisolutions.com", "sushma.piraka@geminisolutions.com",
                   "anang.tomar@geminisolutions.com", "debarghya.maity@geminisolutions.com", "kritadhi.maity@geminisolutions.com", "akshita.rajain@geminisolutions.com"]
def send_email(report_html):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Demo Links Status Report"
    msg['From'] = sender_email
    msg['To'] = ", ".join(receiver_emails)
    
    body_html = f"""
    <html>
        <body>
            <p>Hi Team,</p>
            <p>Here is an update of the working status of the Deployment Links of the POC projects:</p>
            {report_html}
            <p>Regards,<br>Data Science Team</p>
        </body>
    </html>
    """
    
    part1 = MIMEText(body_html, 'html')
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
    report_with_links = [
        (project_name, project_lead, f'<a href="{link}">{link}</a>' if link != "n/a" else link, status) 
        for project_name, project_lead, link, status in report
    ]
    
    table_html = f"""
    <table style="width:100%; border-collapse: collapse;">
        <thead>
            <tr>
                <th style="border: 1px solid black; padding: 8px; background-color: #f2f2f2;">Project Name</th>
                <th style="border: 1px solid black; padding: 8px; background-color: #f2f2f2;">Project Lead</th>
                <th style="border: 1px solid black; padding: 8px; background-color: #f2f2f2;">Demo Link</th>
                <th style="border: 1px solid black; padding: 8px; background-color: #f2f2f2;">Status</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for row in report_with_links:
        table_html += "<tr>"
        for cell in row:
            table_html += f'<td style="border: 1px solid black; padding: 8px;">{cell}</td>'
        table_html += "</tr>"
    
    table_html += """
        </tbody>
    </table>
    """
    
    return table_html

def daily_task():
    demo_links = [
        ("FinBot - A Financial ChatBot", "Kritadhi Maity", "http://13.232.58.176:8502/"),
        ("Credit Scoring model", "Aditya Singh", "n/a"),
        ("AI Recommendation Bot", "Saurav Anand", "n/a"),
        ("Language Translation Bot", "Sushma Piraka", "n/a"),
        ("Trade Guard", "Aditya Singh/Prashant Solanki", "n/a"),
        ("Gemini Policy Bot", "Debarghya Maity", "n/a"),
        ("Document Information Retrieval Bot", "Debarghya Maity", "http://13.232.58.176:5005/"),
        ("Document Sentiment Insights", "Nitish John Toppo", "https://usairlinessentimentanalysis-asmerbqllmx35uappbcvamo.streamlit.app"),
        ("Document Intelligence Bot", "Kritadhi Maity", "http://52.66.10.81:8502/"),
        ("Organizational Structure Construction", "Debarghya Maity", "http://13.232.58.176:8003/"),
        ("WebInspect AI", "Debarghya Maity", "http://13.232.58.176:8004/"),
        ("Customer Review Sentiment Analysis", "Debarghya Maity", "http://13.232.58.176:8001/"),
        ("Forex Trends", "Debarghya Maity", "http://13.232.58.176:8002/"),
        ("Park Easy", "Akshita Rajain", "http://52.66.10.81:8001/"),
        ("Teams Transcript Bot","Debarghya Maity/Prashant Solanki","https://teams.microsoft.com/l/app/2df02d86-770a-4c51-a6d7-b5def211a1ca?source=app-details-dialog" )
    ]

    report = check_links(demo_links)
    report_table = generate_report(report)
    send_email(report_table)

# Directly call the daily_task function to run the script once
if __name__ == "__main__":
    daily_task()

