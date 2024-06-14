import os
import streamlit as st
import requests
from tabulate import tabulate
import config as cf

def check_links(links):
    status_report = []
    for project_name, link in links:
        try:
            response = requests.get(link, timeout=10)
            if response.status_code == 200:
                status = "OK"
            else:
                status = f"Fail: HTTP {response.status_code}"
        except requests.RequestException as e:
            status = f"Fail: {e}"
        
        status_report.append((project_name, link, status))
    return status_report

def generate_report(report):
    headers = ["Project Name", "Demo Link", "Status"]
    table = tabulate(report, headers=headers, tablefmt="grid")
    return table

def status_report_page():
    st.title("Demo Links Status Report")

    demo_links = [
        ("Starzplay video enhancement POC", "https://videocrop.streamlit.app/"),
        ("Starzplay video enhancement POC", "https://videocrop.streamlit.app/"),
        ("Github Bot", "https://gitbott.streamlit.app/"),
        ("FX Sentiment Analysis", "http://3.7.234.8:8000/"),
        ("Financial ChatBot", "https://huggingface.co/spaces/maitykritadhi/Kr_Financial_Chatbot_StreamLitUI")
    ]

    if st.button("Check Links"):
        with st.spinner('Checking links...'):
            report = check_links(demo_links)
            report_table = generate_report(report)
            st.text(report_table)


            st.write("### Status Table")
            st.table(report)
    else:
        st.write("Click the button to check the status of the demo links.")

def project_box(project_name, deployment_links, creator, status, code_repo_link, description, documentation_link, icon_path):
    """
    Function to create a box containing project information.
    """
   
    st.image(icon_path, use_column_width=True)

   
    with st.expander(f"{project_name}"):
        st.write(f"**Deployment Link:** {deployment_links}")
        st.write(f"**Project Lead:** {creator}")
        st.write(f"**Status:** {status}")
        st.write(f"**Code Repository Link:** {code_repo_link}")
        st.write(f"**Description:** {description}")
        st.write(f"[Documentation]({documentation_link})")

def main():
   
    st.markdown(
        """
        <style>
        .project-box {
            margin-bottom: 50px;
      
        }
        </style>
        <h1 style='text-align: center;'>Data Science Projects - Demo Repository</h1>
        """,
        unsafe_allow_html=True
    )
    search_query = st.text_input("Search Projects")

   
    projects = [
        {
            "name": "Credit Scoring Model",
            "deployment_links": "n/a",
            "creator": "Aditya Singh",
            "status": "n/a",
            "code_repo_link": "https://drive.google.com/file/d/151v8tZW1mGXcthHeUgshzH2cDsdxq-DR/view?usp=sharing",
            "description": "Model classifies users into either 'Good' or 'Bad' using features with 93% accuracy",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "credit-scoring.jfif")
        },
        {
            "name": "Trade Surveillence POC",
            "deployment_links": "n/a",
            "creator": "Aditya Singh",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "POC for detecting 2 (circular trading and spoofing) market manipulation techniques using synthetically generated data",
            "documentation_link": "https://docs.example.com/project2",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "Starzplay Video Enhancement POC",
            "deployment_links": "https://videocrop.streamlit.app/",
            "creator": "Aditya Singh",
            "status": "Not Running",
            "code_repo_link": "https://github.com/AdityaSingh1574/Video-Enhancement-POC.git",
            "description": "POC for removing in-built black borders from video and to implement 'Smart Zoom'",
            "documentation_link": "https://docs.example.com/project3",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "video.jfif")
        },
        {
            "name": "Starzplay Video Enhancement POC",
            "deployment_links": "https://videocrop.streamlit.app/",
            "creator": "Chaitanya Raj",
            "status": "Running",
            "code_repo_link": "https://github.com/chaitanyaraj53/video_crop",
            "description": "POC for removing in-built black borders from video and to implement 'Smart Zoom'",
            "documentation_link": "https://docs.example.com/project4",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "video.jfif")
        },
        {
            "name": "Generic Search Test",
            "deployment_links": "n/a",
            "creator": "Chaitanya Raj",
            "status": "n/a",
            "code_repo_link": "https://colab.research.google.com/drive/1RXUMhuG_BYgW1mEoi3SdjiAIKU5oeiMI?usp=sharing",
            "description": "Preliminary Test on Generic QA bot",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "search.png")
        },
        {
            "name": "Github Bot",
            "deployment_links": "https://gitbott.streamlit.app/",
            "creator": "Chaitanya Raj",
            "status": "Running",
            "code_repo_link": "https://github.com/chaitanyaraj53/gitbot",
            "description": "Demo on Chatbot to communicate with github repos",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "chatbot.webp")
        },
        {
            "name": "Credit Card Transaction Anomaly",
            "deployment_links": "n/a",
            "creator": "Chaitanya Raj",
            "status": "n/a",
            "code_repo_link": "https://github.com/chaitanyaraj53/credit-card-anomaly",
            "description": "Model training to determine fraud transactions from credit card transaction data",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "credit-card.jfif")
        },
        {
            "name": "Starzplay Multi-modal Search",
            "deployment_links": "n/a",
            "creator": "Sushma Piraka, Saurav Anand, Aditya Singh",
            "status": "n/a",
            "code_repo_link": "https://github.com/Gemini-Solutions/multi-modal-search",
            "description": "POC when given an image as input returns the most relevant videos and when some text is given as input it will give the relevant dataframe",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "i1.jpg")
        },
        {
            "name": "Starzplay Text Translation",
            "deployment_links": "n/a",
            "creator": "Sushma Piraka, Saurav Anand",
            "status": "n/a",
            "code_repo_link": "https://github.com/Gemini-Solutions/text-translation",
            "description": "POC to perform multilingual translations(more specific to MENA languages)",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "translation.webp")
        },
        {
            "name": "Credit Card Transaction Anomaly",
            "deployment_links": "n/a",
            "creator": "Sushma Piraka",
            "status": "n/a",
            "code_repo_link": "https://github.com/chaitanyaraj53/credit-card-anomaly",
            "description": "POC where we extracted historical data and trained a model to detect suspicious credit card transaction",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "credit-card.jfif")
        },
        {
            "name": "Trade Surveillence POC",
            "deployment_links": "n/a",
            "creator": "Sushma Piraka",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "POC to detect spoofing in market manipulation on synthetic data",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "FX-Sentiment-Analysis",
            "deployment_links": "http://3.7.234.8:8000/",
            "creator": "Debarghya Maity",
            "status": "Not Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/fx-sentiment-analysis",
            "description": "POC for Forex Analysis for JPY Currency",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "forex.jfif")
        },
        {
            "name": "Broker-Sentiment-Analysis",
            "deployment_links": "n/a",
            "creator": "Nitish John Toppo",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "Build a demo for a solution that looks at tweets daily from different brokers and performs sentiment analysis",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "broker.jfif")
        },
        {
            "name": "Financial ChatBot",
            "deployment_links": "https://huggingface.co/spaces/maitykritadhi/Kr_Financial_Chatbot_StreamLitUI",
            "creator": "Kritadhi Maity",
            "status": "Running",
            "code_repo_link": "https://huggingface.co/spaces/maitykritadhi/Kr_Financial_Chatbot_StreamLitUI",
            "description": "Build a chatbot which feeds on financial context and will able to answer user's queries based on the context.",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "chatbot.webp")
        },
        {
            "name": "Gemini Policy Bot",
            "deployment_links": "n/a",
            "creator": "Debarghya Maity/Saurav",
            "status": "n/a",
            "code_repo_link": "https://github.com/Gemini-Solutions/Flask_Server",
            "description": "POC for integration of Gemini Policy with chatbot",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "chatbot.webp")
        },
        {
            "name": "AI Virtual Influencer",
            "deployment_links": "n/a",
            "creator": "Goutam Sharma",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "POC for building AI influencer that responds to given instructions.",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "ai-influencer.jfif")
        },
        {
            "name": "FAB demo",
            "deployment_links": "http://52.66.10.81:8002/",
            "creator": "Debarghya Maity/ Prashant Solanki",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "Extraction of entities from commercial banking documents and chatbot creation",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "ai-influencer.jfif")
        },
        {
            "name": "Yen Forex Sentiment Analysis",
            "deployment_links": "http://15.206.189.243:8503/",
            "creator": "Debarghya Maity/ Prashant Solanki",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "ai-influencer.jfif")
        },
        {
            "name": "Sentiment Analysis on PDF Financial Document ",
            "deployment_links": "http://15.206.189.243:8502/",
            "creator": "Debarghya Maity/ Prashant Solanki",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "ai-influencer.jfif")
        },

        {
            "name": "Airline sentiment analysis",
            "deployment_links": "",
            "creator": "Nitish John Toppo",
            "status": "n/a",
            "code_repo_link": "https://colab.research.google.com/drive/1w06g3FS0dG1mfEf2sOy6mu5xpHh8zNeK?usp=sharing"   "https://github.com/NitishJT/us_airlines_sentiment_analysis",
            "description": "",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/utkarsh_singh_geminisolutions_com/_layouts/15/Doc.aspx?sourcedoc=%7B87A7CC4B-9CEB-4BDD-8B89-559314F9AD6E%7D&file=SENTIMENT_ANALYSIS_US_AIRLINES.pptx&action=edit&mobileredirect=true",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "ai-influencer.jfif")
        },
        {
            "name": "Emaar AI Chatbot",
            "deployment_links": "https://huggingface.co/spaces/anang150296/Emaar-AI-chatbot",
            "creator": "",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/utkarsh_singh_geminisolutions_com/Documents/POC%20Docs/EMAAR%20AI%20CHATBOT/Emaar%20IA%20chatbot.pptx?d=w0b9af1d417ac49b8a3c92a23bf206505&csf=1&web=1&e=oWxvl1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "ai-influencer.jfif")
        }
       
    ]

    # Filter projects based on search query
    filtered_projects = [project for project in projects if search_query.lower() in project["name"].lower()]

    # Iterate through the filtered projects and create boxes
    num_cols = 4  # Number of columns to display
    for i in range(0, len(filtered_projects), num_cols):
        row_projects = filtered_projects[i:i+num_cols]
        cols = st.columns(num_cols)
        for col, project in zip(cols, row_projects):
            with col:
                with st.container():
                    st.markdown('<div class="project-box">', unsafe_allow_html=True)
                    project_box(
                        project["name"],
                        project["deployment_links"],
                        project["creator"],
                        project["status"],
                        project["code_repo_link"],
                        project["description"],
                        project["documentation_link"],
                        project["icon_path"]
                    )
                    st.markdown('</div>', unsafe_allow_html=True)

   


if __name__ == "__main__":
    tab1, tab2 = st.tabs(["Repository", "Deployment Link Status Report"])

    with tab1:
        main()

    with tab2:
        status_report_page()
