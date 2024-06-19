import os
import streamlit as st
import requests  
from tabulate import tabulate
import config as cf

st.markdown(
    """
    <style>
    
    .streamlit-expander {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
   
    .streamlit-expander .css-15dtf11 {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
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
            "code_repo_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/personal/aditya_singh1_geminisolutions_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Faditya%5Fsingh1%5Fgeminisolutions%5Fcom%2FDocuments%2FTrade%2DSurveillance%2DProject&ga=1",
            "description": "POC for detecting 2 (circular trading and spoofing) market manipulation techniques using synthetically generated data",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/Trade%20Surveillance%20(1).pptx?d=w71f30a40057d4f63920d2bd460480ad8&csf=1&web=1&e=pPqlPU",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "Starzplay Video Enhancement POC",
            "deployment_links": "https://videocrop.streamlit.app/",
            "creator": "Aditya Singh",
            "status": "Not Running",
            "code_repo_link": "https://github.com/AdityaSingh1574/Video-Enhancement-POC.git",
            "description": "POC for removing in-built black borders from video and to implement 'Smart Zoom'",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/STARZPLAY%20VIDEO%20ENHANCEMENT%20(1).pptx?d=w063f7f75bdfc4da7b82150e19644eba9&csf=1&web=1&e=ppr54h",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "video.jfif")
        },
        
        
        {
            "name": "Github Bot",
            "deployment_links": "https://gitbott.streamlit.app/",
            "creator": "Debarghya Maity",
            "status": "Running",
            "code_repo_link": "https://github.com/chaitanyaraj53/gitbot",
            "description": "Demo on Chatbot to communicate with github repos",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "chatbot.webp")
        },
        
        {
            "name": "Starzplay Multi-modal Search",
            "deployment_links": "n/a",
            "creator": "Saurav Anand, Aditya Singh",
            "status": "n/a",
            "code_repo_link": "https://github.com/Gemini-Solutions/multi-modal-search",
            "description": "POC when given an image as input returns the most relevant videos and when some text is given as input it will give the relevant dataframe",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/STARZPLAY%20MULTI-MODAL%20(1).pptx?d=w36a378dc59264da7982855e70848bffd&csf=1&web=1&e=WvS8RK",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "i1.jpg")
        },
        {
            "name": "Starzplay Text Translation",
            "deployment_links": "n/a",
            "creator": "Sushma Piraka",
            "status": "n/a",
            "code_repo_link": "https://github.com/Gemini-Solutions/text-translation",
            "description": "POC to perform multilingual translations(more specific to MENA languages)",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/Translation-Starzplay.pptx?d=wfda2aa657580483cac8de6cd3d3c733a&csf=1&web=1&e=sY0KvU",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        
        {
            "name": "Gemini Policy Bot",
            "deployment_links": "n/a",
            "creator": "Debarghya Maity",
            "status": "n/a",
            "code_repo_link": "https://github.com/prashantsolanki975/PolicyGemChat",
            "description": "POC for multi-modal chatbot which will answer employees' queries on company policies",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": " Facial Expression Manipulation.",
            "deployment_links": "https://huggingface.co/spaces/goutamsharma/facial-expression-manulplation",
            "creator": "Goutam Sharma",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "It is a basic POC to display images and caption those images",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:f:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/FACIAL%20EXPRESSION%20MANIPULATION?csf=1&web=1&e=FORse7",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "FAB Demo",
            "deployment_links": "http://52.66.10.81:8002/",
            "creator": "Debarghya Maity",
            "status": "Running",
            "code_repo_link": "n/a",
            "description": "Real-time trend detection and sentiment analysis of MENA-based financial news",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        
        {
            "name": "Airline Sentiment Analysis",
            "deployment_links": "https://usairlinessentimentanalysis-asmerbqllmx35uappbcvamo.streamlit.app",
            "creator": "Nitish John Toppo",
            "status": "Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/airline-sentiment-analysis",
            "description": "Trains model on tweets and identifies sentiments to specific US airlines",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/SENTIMENT_ANALYSIS_US_AIRLINES.pptx?d=w6f3d8b1cd90c4a998eebd095bad892bd&csf=1&web=1&e=aiayU9",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "Emaar IA Chatbot",
            "deployment_links": "https://huggingface.co/spaces/anang150296/Emaar-AI-chatbot",
            "creator": "Debarghya Maity",
            "status": "Running",
            "code_repo_link": "n/a",
            "description": "n/a",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/Emaar%20IA%20chatbot.pptx?d=wf2b7902213704f50b249d8879613bc2e&csf=1&web=1&e=dvlUJC",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "chatbot.webp")
        },
        {
            "name": "Organizational Structure Construction",
            "deployment_links": "http://13.232.58.176:8003/",
            "creator": "Debarghya Maity",
            "status": "Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/org-structure-construction",
            "description": "Tool to construct org structure based on crawled employee information",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "QA GenAI",
            "deployment_links": "http://13.232.58.176:8004/",
            "creator": "Debarghya Maity",
            "status": "Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/QA-GenAI",
            "description": "Generative AI POC for QA bot",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "Sentiment Demo",
            "deployment_links": "http://13.232.58.176:8001/",
            "creator": "Debarghya Maity",
            "status": "Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/sentiment-demo",
            "description": "n/a",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/SENTIMENT%20DEMO.pptx?d=w31846e216824499bbe64d6636a57e15c&csf=1&web=1&e=7BURmL",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        
        {
            "name": "Emaar Valet AI",
            "deployment_links": "http://52.66.10.81:8001/",
            "creator": "Debarghya Maity",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "Tn/a",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/Emaar_Valet_Use_case_info.pptx?d=we25f572754de45b990cc2b8fbf9079a9&csf=1&web=1&e=qbbs6k",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "Financial ChatBot",
            "deployment_links": "https://huggingface.co/spaces/maitykritadhi/Kr_Financial_Chatbot_StreamLitUI",
            "creator": "Kritadhi Maity",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "n/a",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "trade.png")
        },
        {
            "name": "FX Sentiment Analysis",
            "deployment_links": "http://13.232.58.176:8002/",
            "creator": "Kritadhi Maity",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "n/a",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/FX%20SENTIMENT%20ANALYSIS.pptx?d=wdd5d6aec05a845d2a37bca1150e9d78d&csf=1&web=1&e=NZLGtQ",
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

   


    


   