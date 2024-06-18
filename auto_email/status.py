import requests
from tabulate import tabulate
import streamlit as st

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

def status_report_page():
    st.title("Demo Links Status Report")
    
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

    if st.button("Check Links"):
        with st.spinner('Checking links...'):
            report = check_links(demo_links)
            report_table = generate_report(report)
            st.markdown(report_table, unsafe_allow_html=True)
    else:
        st.write("Click the button to check the status of the demo links.")

if __name__ == "__main__":
    status_report_page()
