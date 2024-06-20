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
       
      
        
        ("FinBot - A Financial ChatBot", "Kritadhi Maity", "https://huggingface.co/spaces/maitykritadhi/Kr_Financial_Chatbot_StreamLitUI"),
        ("Credit Scoring model", "Aditya Singh", "n/a"),
        ("Multi-modal Search", "Aditya Singh/Prashant Solanki", "n/a"),
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
            "name": "Trade Guard",
            "deployment_links": "n/a",
            "creator": "Aditya Singh",
            "status": "n/a",
            "code_repo_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/personal/aditya_singh1_geminisolutions_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Faditya%5Fsingh1%5Fgeminisolutions%5Fcom%2FDocuments%2FTrade%2DSurveillance%2DProject&ga=1",
            "description": "POC for detecting 2 (circular trading and spoofing) market manipulation techniques using synthetically generated data",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/Trade%20Guard.pptx?d=w575e23307d6348cea506ad14eb0e87f4&csf=1&web=1&e=mNtx0r",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "forex.jfif")
        },
      
        
    
        {
            "name": "Multi-modal Search",
            "deployment_links": "n/a",
            "creator": "Saurav Anand, Aditya Singh",
            "status": "n/a",
            "code_repo_link": "https://github.com/Gemini-Solutions/multi-modal-search",
            "description": "POC when given an image as input returns the most relevant videos and when some text is given as input it will give the relevant dataframe",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/_MULTI-MODAL.pptx?d=w03ae50b9cce141a781b71f84466236d7&csf=1&web=1&e=ciElNO",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "i1.jpg")
        },
        {
            "name": "LingoBot",
            "deployment_links": "n/a",
            "creator": "Sushma Piraka",
            "status": "n/a",
            "code_repo_link": "https://github.com/Gemini-Solutions/text-translation",
            "description": "POC to perform multilingual translations(more specific to MENA languages)",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/LingoBot.pptx?d=w881811c36097402ab3b0c15f89462b81&csf=1&web=1&e=3vjqm6",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "translation.webp")
        },
        
        {
            "name": "Gemini Policy Bot",
            "deployment_links": "n/a",
            "creator": "Debarghya Maity",
            "status": "n/a",
            "code_repo_link": "https://github.com/prashantsolanki975/PolicyGemChat",
            "description": "POC for multi-modal chatbot which will answer employees' queries on company policies",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "policy.webp")
        },
        
        {
            "name": "Document Information Retrieval Bot",
            "deployment_links": "http://52.66.10.81:8002/",
            "creator": "Debarghya Maity",
            "status": "Running",
            "code_repo_link": "n/a",
            "description": "Real-time trend detection and sentiment analysis of MENA-based financial news",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "documentRetrieval.png")
        },
        
        {
            "name": "Sentiment Insights",
            "deployment_links": "https://usairlinessentimentanalysis-asmerbqllmx35uappbcvamo.streamlit.app",
            "creator": "Nitish John Toppo",
            "status": "Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/airline-sentiment-analysis",
            "description": "Trains model on tweets and identifies sentiments to specific US airlines",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/SENTIMENT%20INSIGHT.pptx?d=wa5b5259586e547178c0c1f0e2b1c7de1&csf=1&web=1&e=KJ0kIO",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "sentimentInsights.svg")
        },
        {
            "name": "Document Intelligence Bot",
            "deployment_links": "https://huggingface.co/spaces/anang150296/Emaar-AI-chatbot",
            "creator": "Debarghya Maity",
            "status": "Running",
            "code_repo_link": "n/a",
            "description": "n/a",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/Document%20Intelligence%20Bot.pptx?d=w7cc81d1f43bc40edb56e0597ec3bc2d3&csf=1&web=1&e=LXpO7T",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "intelligence.jpg")
        },
        {
            "name": "Organizational Structure Construction",
            "deployment_links": "http://13.232.58.176:8003/",
            "creator": "Debarghya Maity",
            "status": "Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/org-structure-construction",
            "description": "Tool to construct org structure based on crawled employee information",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "org.jpeg")
        },
        {
            "name": "QA GenAI",
            "deployment_links": "http://13.232.58.176:8004/",
            "creator": "Debarghya Maity",
            "status": "Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/QA-GenAI",
            "description": "Generative AI POC for QA bot",
            "documentation_link": "https://docs.example.com/project1",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "genai.jfif")
        },
        {
            "name": "Sentiment Demo",
            "deployment_links": "http://13.232.58.176:8001/",
            "creator": "Debarghya Maity",
            "status": "Running",
            "code_repo_link": "https://github.com/Gemini-Solutions/sentiment-demo",
            "description": "n/a",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/SENTIMENT%20DEMO.pptx?d=w31846e216824499bbe64d6636a57e15c&csf=1&web=1&e=7BURmL",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "sentimentInsights.svg")
        },
        
        {
            "name": "Park Easy",
            "deployment_links": "http://52.66.10.81:8001/",
            "creator": "Debarghya Maity",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "Tn/a",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/PARK%20EASY.pptx?d=wfc683bd65193407a9263d13878e4022d&csf=1&web=1&e=csv5hq",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "valet-keys.jpg")
        },
        {
            "name": "FinBot - A Financial ChatBot",
            "deployment_links": "https://huggingface.co/spaces/maitykritadhi/Kr_Financial_Chatbot_StreamLitUI",
            "creator": "Kritadhi Maity",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "n/a",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:w:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/Financial%20Chatbot%20documentation.docx?d=wb650909fbb9d4c7988422c47bb385ee3&csf=1&web=1&e=9LxapJ",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "Chatbots-for-financial-services.jpg")
        },
        {
            "name": "Forex Trends",
            "deployment_links": "http://13.232.58.176:8002/",
            "creator": "Kritadhi Maity",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "n/a",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/FOREX%20TRENDS.pptx?d=w73fedaa4c39d4877bdad5859889e6484&csf=1&web=1&e=kgLmpM",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "forex.jfif")
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

   


    


   