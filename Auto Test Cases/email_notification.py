import smtplib
import ssl
import requests
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from pytz import timezone
import time

# Import individual scripts
from document_information import func1
from britvic import britvic
from fx_sentiment import fx
from park_easy import park_easy
from financial_chatbot import financial_chatbot
from document_intelligence import doc_intelligence
from document_insight import doc_insight
from Organization_structure import org_struc
from WebInspect_AI import web_inspect
from airline_sentiment import airline_sentiment

# Email settings
port = 465  # For SSL
password = "nfmrjxivowbykzjh"

# Create a secure SSL context
context = ssl.create_default_context()
sender_email = "poc.status.notification@gmail.com"
receiver_emails = ["utkarsh.singh@geminisolutions.com","sudhanshu.malhotra@geminisolutions.com", "prashant.solanki@geminisolutions.com",
                   "aditya.singh1@geminisolutions.com", "saurav.anand@geminisolutions.com", "sushma.piraka@geminisolutions.com",
                   "anang.tomar@geminisolutions.com", "debarghya.maity@geminisolutions.com", "kritadhi.maity@geminisolutions.com", "akshita.rajain@geminisolutions.com", "sumit.kumar@geminisolutions.com"]
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
                    status = "Link is working"
                else:
                    status = f"Fail: HTTP {response.status_code}"
            except requests.RequestException as e:
                status = f"Fail: {e}"

        status_report.append([project_name, project_lead, link, status])
    return status_report

def generate_report(report):
    headers = ["Project Name", "Project Lead", "Demo Link", "Link Status", "Working Status"]
    
    table_html = f"""
    <table style="width:100%; border-collapse: collapse;">
        <thead>
            <tr>
                {" ".join(f'<th style="border: 1px solid black; padding: 8px; background-color: #f2f2f2;">{header}</th>' for header in headers)}
            </tr>
        </thead>
        <tbody>
    """
    
    for row in report:
        table_html += "<tr>"
        for idx, cell in enumerate(row):
            if idx == 2:  # For the Demo Link column
                link = cell if cell != "n/a" else ""
                if link:
                    table_html += f'<td style="border: 1px solid black; padding: 8px;"><a href="{link}" target="_blank">{link}</a></td>'
                else:
                    table_html += f'<td style="border: 1px solid black; padding: 8px;">{link}</td>'
            else:
                table_html += f'<td style="border: 1px solid black; padding: 8px;">{cell}</td>'
        table_html += "</tr>"
    
    table_html += """
        </tbody>
    </table>
    """
    
    return table_html

def daily_task():
    demo_links = [
        ("FinBot - A Financial ChatBot", "Kritadhi Maity", "http://13.232.253.41:8502/"),
        ("Credit Scoring model", "Aditya Singh", "n/a"),
        ("AI Recommendation Bot", "Saurav Anand", "n/a"),
        ("Language Translation Bot", "Sushma Piraka", "n/a"),
        ("Trade Guard", "Aditya Singh/Prashant Solanki", "n/a"),
        ("Gemini Policy Bot", "Debarghya Maity", "n/a"),
        ("Document Information Retrieval Bot", "Debarghya Maity", "http://13.232.253.41:8005/"),
        ("Document Sentiment Insights", "Debarghya Maity", "http://13.232.253.41:8002/"),
        ("Document Intelligence Bot", "Kritadhi Maity", "http://52.66.10.81:8502/"),
        ("Organizational Structure Construction", "Debarghya Maity", "http://13.232.253.41:8001/"),
        ("WebInspect AI", "Debarghya Maity", "http://13.232.253.41:8003/"),
        ("Customer Review Sentiment Analysis", "Nitish John Toppo", " http://52.66.10.81:8503/"),
        ("Forex Trends", "Debarghya Maity", "http://13.232.253.41:8004"),
        ("Park Easy", "Akshita Rajain", "http://52.66.10.81:8001/"),
        ("Teams Transcript Bot", "Debarghya Maity/Prashant Solanki", "https://teams.microsoft.com/l/app/2df02d86-770a-4c51-a6d7-b5def211a1ca?source=app-details-dialog"),
        ("Product Reviews Sentiment Analysis BOT", "Sumit Kumar", "http://52.66.10.81:8501/")
    ]

    status_report = check_links(demo_links)
    
    # Input files
    file_doc_info = r'/home/ubuntu/POC-Central-Repository/DOCS/POCs Sample documents/Document Information Retrieval Bot/bol.pdf'
    text_to_enter1 = "2017/04/01"
    text_to_enter2 = "2024/07/01"
    file_park_easy = r'/home/ubuntu/POC-Central-Repository/DOCS/POCs Sample documents/Park Easy/toyota_fortuner_front.jpg'
    file_doc_intelligence = r'/home/ubuntu/POC-Central-Repository/DOCS/POCs Sample documents/Document Intelligence Bot/environmental-statement-pune-phase1-2022.pdf'
    file_doc_insight = r'/home/ubuntu/POC-Central-Repository/DOCS/POCs Sample documents/earnings call report docs/META-Q1-2023-Earnings-Call-Transcript.pdf'
    file_org1 = r'/home/ubuntu/POC-Central-Repository/DOCS/POCs Sample documents/organization structure docs/ex_3_document_1.pdf'
    file_org2 = r'/home/ubuntu/POC-Central-Repository/DOCS/POCs Sample documents/organization structure docs/ex_3_document_2.pdf'
    text_to_enter = "https://www.saucedemo.com/"

    # Function calls and appending results
    results = {
        "FinBot - A Financial ChatBot": financial_chatbot(),
        "Credit Scoring model": "N/A",
        "AI Recommendation Bot": "N/A",
        "Language Translation Bot": "N/A",
        "Trade Guard": "N/A",
        "Gemini Policy Bot": "N/A",
        "Document Information Retrieval Bot": func1(file_doc_info),
        "Document Sentiment Insights": doc_insight(file_doc_insight),
        "Document Intelligence Bot": doc_intelligence(file_doc_intelligence),
        "Organizational Structure Construction": org_struc(file_org1, file_org2),
        "WebInspect AI": web_inspect(text_to_enter),
        "Customer Review Sentiment Analysis": airline_sentiment(),
        "Forex Trends": fx(text_to_enter1, text_to_enter2),
        "Park Easy": park_easy(file_park_easy),
        "Teams Transcript Bot": "N/A",
        "Product Reviews Sentiment Analysis BOT": britvic()        
    }

    for project in status_report:
        project_name = project[0]
        project_result = results.get(project_name, "N/A")
        project.append(project_result)

    report_table = generate_report(status_report)
    send_email(report_table)

# Directly call the daily_task function to run the script once
if __name__ == "__main__":
    daily_task()
