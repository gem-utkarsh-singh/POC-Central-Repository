import os
import streamlit as st
import requests  
from tabulate import tabulate
import config as cf

st.markdown(
    """
    <style>
    /* Target the expander and remove padding */
    .streamlit-expander {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    /* Target the notification button and hide it */
    .streamlit-expander .css-15dtf11 {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def check_links(links):
    status_report = []
    for project_name, link in links:
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
        
        status_report.append((project_name, link, status))
    return status_report

def generate_report(report):
    headers = ["Project Name", "Demo Link", "Status"]
    table = tabulate(report, headers=headers, tablefmt="html")
    return table

def status_report_page():
    st.title("Demo Links Status Report")
    
    demo_links = [
        ("Starzplay video enhancement POC", "https://videocrop.streamlit.app/"),
        ("Github Bot", "https://gitbott.streamlit.app/"),
        ("FX Sentiment Analysis", "http://3.7.234.8:8000/"),
        ("Financial ChatBot", "https://huggingface.co/spaces/maitykritadhi/Kr_Financial_Chatbot_StreamLitUI"),
        ("Credit Scoring model", "n/a"),
        ("Starzplay Multi-modal Search","n/a"),
        ("Starzplay text translation","n/a"),
        ("Trade Surveillence POC","n/a"),
        ("Gemini Policy Bot","n/a"),
        ("AI virtual Influencer","n/a"),
        ("FAB demo","http://52.66.10.81:8002/"),
        ("Yen Forex Sentiment Analysis","http://15.206.189.243:8503/"),
        ("Sentiment Analysis on PDF Financial Document","http://15.206.189.243:8502/"),
        ("Airline sentiment analysis","https://usairlinessentimentanalysis-asmerbqllmx35uappbcvamo.streamlit.app"),
        ("Emaar AI Chatbot","https://huggingface.co/spaces/anang150296/Emaar-AI-chatbot"),
        ("Org Structure Construction","http://13.232.58.176:8003/"),
        ("QA_GenAI","http://13.232.58.176:8004/"),
        ("Sentiment Demo","http://13.232.58.176:8001/"),
        ("Sentiment Analysis on Company Earnings Call Transcript","http://3.108.236.232:8503/"),
        ("Emaar Valet AI","n/a"),
    ]

    if st.button("Check Links"):
        with st.spinner('Checking links...'):
            report = check_links(demo_links)
            report_table = generate_report(report)
            st.markdown(report_table, unsafe_allow_html=True)
    else:
        st.write("Click the button to check the status of the demo links.")

def main():


    if 'show_notification' not in st.session_state:
        st.session_state.show_notification = True

    st.markdown(
        """
        <style>
        .project-box {
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 20px;
        }
        .notification {
            padding: 10px;
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            border-radius: 5px;
            margin-top: 10px;
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
        }
        .notification-text {
            flex-grow: 1; /* Allow text to expand */
        }
        .close-button {
            cursor: pointer;
            background-color: transparent;
            border: 1px;
            padding: 10px;
            margin-bottom: 15px;
        }
        .project-column {
        display: flex;
        flex-direction: column;
        align-items: center;
        }

        </style>
        <h1 style='text-align: center;'>Data Science Projects - Demo Repository</h1>
        """,
        unsafe_allow_html=True
    )
    search_query = st.text_input("Search Projects")

    # notification
    if st.session_state.show_notification:
        st.markdown("""
            <div class='notification'>
                <div class='notification-text'>
                    Click on the Project Status Report tab to check the status of the Deployment Links.
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Close Notification"):
            st.session_state.show_notification = False
   




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
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "Trade Surveillence POC",
            "deployment_links": "n/a",
            "creator": "Nikhil Goyal",
            "status": "n/a",
            "code_repo_link": "https://github.com/Gemini-Solutions/trade-surveillence",
            "description": "POC for detecting 2 (circular trading and spoofing) market manipulation techniques using synthetically generated data",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "Gemini Policy Bot",
            "deployment_links": "n/a",
            "creator": "Ankit Verma, Sushma Piraka",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "POC for multi-modal chatbot which will answer employees' queries on company policies",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "AI Virtual Influencer",
            "deployment_links": "n/a",
            "creator": "Ashutosh Singh",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "It is a basic POC to display images and caption those images",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "FAB Demo",
            "deployment_links": "http://52.66.10.81:8002/",
            "creator": "Nikhil Goyal",
            "status": "Running",
            "code_repo_link": "n/a",
            "description": "Real-time trend detection and sentiment analysis of MENA-based financial news",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "Yen Forex Sentiment Analysis",
            "deployment_links": "http://15.206.189.243:8503/",
            "creator": "Nikhil Goyal",
            "status": "Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/yen-forex-sentiment-analysis",
            "description": "POC to predict Forex movement based on sentiment from forex-based news articles",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "Sentiment Analysis on PDF Financial Document",
            "deployment_links": "http://15.206.189.243:8502/",
            "creator": "Nikhil Goyal",
            "status": "Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/pdf-sentiment-analysis",
            "description": "Extracts data from financial reports in pdf format, analyzes sentiment at sentence level, and identifies important keywords",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "Airline Sentiment Analysis",
            "deployment_links": "https://usairlinessentimentanalysis-asmerbqllmx35uappbcvamo.streamlit.app",
            "creator": "Nikhil Goyal",
            "status": "Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/airline-sentiment-analysis",
            "description": "Trains model on tweets and identifies sentiments to specific US airlines",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "Emaar AI Chatbot",
            "deployment_links": "https://huggingface.co/spaces/anang150296/Emaar-AI-chatbot",
            "creator": "Anang Kumar",
            "status": "Running",
            "code_repo_link": "n/a",
            "description": "Chatbot trained on emirates policies, contact information and other relevant information",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "chatbot.webp")
        },
        {
            "name": "Organizational Structure Construction",
            "deployment_links": "http://13.232.58.176:8003/",
            "creator": "Ankit Verma",
            "status": "Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/org-structure-construction",
            "description": "Tool to construct org structure based on crawled employee information",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "QA GenAI",
            "deployment_links": "http://13.232.58.176:8004/",
            "creator": "Ankit Verma",
            "status": "Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/QA-GenAI",
            "description": "Generative AI POC for QA bot",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "Sentiment Demo",
            "deployment_links": "http://13.232.58.176:8001/",
            "creator": "Ankit Verma",
            "status": "Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/sentiment-demo",
            "description": "Demo of sentiment analysis on financial news articles",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "Sentiment Analysis on Company Earnings Call Transcript",
            "deployment_links": "http://3.108.236.232:8503/",
            "creator": "Nikhil Goyal",
            "status": "Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/earnings-call-sentiment",
            "description": "Analyzes sentiment in earnings call transcripts of various companies",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "Emaar Valet AI",
            "deployment_links": "n/a",
            "creator": "Anang Kumar",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "Tool to assist Emaar employees with valet services",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
    ]

    filtered_projects = [project for project in projects if search_query.lower() in project["name"].lower()]

    if not filtered_projects:
        st.write("No projects found.")
        return

    cols = st.columns(4)
    col_idx = 0

    for project in filtered_projects:
        with cols[col_idx]:
            st.markdown("<div class='project-column'>", unsafe_allow_html=True)
            st.image(project["icon_path"], use_column_width=True)
            with st.expander(project["name"]):
                st.write(f"**Deployment Link:** {project['deployment_links']}")
                st.write(f"**Project Lead:** {project['creator']}")
                st.write(f"**Status:** {project['status']}")
                st.write(f"**Code Repository Link:** {project['code_repo_link']}")
                st.write(f"**Description:** {project['description']}")
                st.write(f"[Documentation]({project['documentation_link']})")
            st.markdown("</div>", unsafe_allow_html=True)
        col_idx = (col_idx + 1) % 4

if __name__ == "__main__":
    tab1, tab2 = st.tabs(["Project Repository", "Project Status Report"])

    with tab1:
        main()

    
      
    with tab2:
        status_report_page()

   


    


   