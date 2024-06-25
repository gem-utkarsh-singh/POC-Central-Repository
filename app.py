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


def status_report_page():
    st.title("Demo Links Status Report")
    
    demo_links = [
       
      
        
        ("FinBot - A Financial ChatBot", "Kritadhi Maity", "https://huggingface.co/spaces/maitykritadhi/Kr_Financial_Chatbot_StreamLitUI"),
        ("Credit Scoring model", "Aditya Singh", "n/a"),
        ("AI Recommendation Bot", "Aditya Singh/Prashant Solanki", "n/a"),
        ("Language Translation Bot", "Sushma Piraka", "n/a"),
        ("Trade Guard", "Aditya Singh/Prashant Solanki", "n/a"),
        ("Gemini Policy Bot", "Debarghya Maity", "n/a"),
       
        ("Document Information Retrieval Bot", "Debarghya Maity", "http://52.66.10.81:8002/"),
       
       
        ("Document Sentiment Insights", "Nitish John Toppo", "https://usairlinessentimentanalysis-asmerbqllmx35uappbcvamo.streamlit.app"),
        ("Document Intelligence Bot", "Kritadhi Maity", "https://huggingface.co/spaces/maitykritadhi/Document_Intelligence_Bot"),
        ("Organizational Structure Construction", "Debarghya Maity", "http://13.232.58.176:8003/"),
        ("WebInspect AI", "Debarghya Maity", "http://13.232.58.176:8004/"),
        ("Customer Review Sentiment Analysis", "Debarghya Maity", "http://13.232.58.176:8001/"),
        ("Forex Trends", "Kritadhi Maity", "http://13.232.58.176:8002/"),
       
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
            "documentation_link": "n/a",
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
            "name": "AI Recommendation Bot",
            "deployment_links": "n/a",
            "creator": "Saurav Anand, Aditya Singh",
            "status": "n/a",
            "code_repo_link": "n/a",
            "description": "Recommendation system based on text, image and video input created using multi-model architecture",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/AI%20Recommendation%20Bot.pptx?d=wa137bca0b6e34091a304463df50bf13e&csf=1&web=1&e=RGDmbQ",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "i1.jpg")
        },
        {
            "name": "Language Translation Bot",
            "deployment_links": "n/a",
            "creator": "Sushma Piraka",
            "status": "n/a",
            "code_repo_link": "n/a",
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
            "documentation_link": "n/a",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "policy.webp")
        },
        
        {
            "name": "Document Information Retrieval Bot",
            "deployment_links": "http://52.66.10.81:8002/",
            "creator": "Debarghya Maity",
            "status": "Running",
            "code_repo_link": "n/a",
            "description": "Retrieve important key matrices from the documents as per client usecase and document type",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:f:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/Document%20Information%20Retrieval%20Bot?csf=1&web=1&e=ubGaEl",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "documentRetrieval.png")
        },
        
        {
            "name": "Customer Review Sentiment Analysis",
            "deployment_links": "https://usairlinessentimentanalysis-asmerbqllmx35uappbcvamo.streamlit.app",
            "creator": "Nitish John Toppo",
            "status": "Running",
            "code_repo_link": "n/a",
            "description": "Trains model on tweets and identifies sentiments to specific US airlines",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/SENTIMENT%20INSIGHT.pptx?d=wa5b5259586e547178c0c1f0e2b1c7de1&csf=1&web=1&e=KJ0kIO",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "sentimentInsights.svg")
        },
        {
            "name": "Document Intelligence Bot",
            "deployment_links": "https://huggingface.co/spaces/maitykritadhi/Document_Intelligence_Bot",
            "creator": "Kritadhi Maity",
            "status": "Running",
            "code_repo_link": "n/a",
            "description": "Retrieve important key matrices from the documents as per client use case and document type.",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:f:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/Document%20Intelligence%20Bot?csf=1&web=1&e=ECkTpV",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "intelligence.jpg")
        },
        {
            "name": "Organizational Structure Construction",
            "deployment_links": "http://13.232.58.176:8003/",
            "creator": "Debarghya Maity",
            "status": "Running",
            "code_repo_link": "n/a",
            "description": "To create an organizational structure based on the information about owners/ share holders and the companies that they are linked to.",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:f:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/Organizational%20Structure%20Construction?csf=1&web=1&e=h5MkFK",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "org.jpeg")
        },
        {
            "name": "WebInspect AI",
            "deployment_links": "http://13.232.58.176:8004/",
            "creator": "Debarghya Maity",
            "status": "Running",
            "code_repo_link": "n/a",
            "description": "Scrapes and parses the HTML (of the input URL) and extracts important features. Creates test cases for the identified features.",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:f:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/WebInspect%20AI?csf=1&web=1&e=7vqWff",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "genai.jfif")
        },
        {
            "name": "Document Sentiment Insights",
            "deployment_links": "http://13.232.58.176:8001/",
            "creator": "Debarghya Maity",
            "status": "Running",
            "code_repo_link": "n/a",
            "description": "Analyzes the ECT report (earnings call transcript) and  extracts important topics discussed. Gives the information on what is said on each topic and generates a sentiment report for each topic.",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:f:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/Document%20Sentiment%20Insights?csf=1&web=1&e=nCyFuu",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "sentimentInsights.svg")
        },
        
        {
            "name": "Park Easy",
            "deployment_links": "http://52.66.10.81:8001/",
            "creator": "Akshita Ranjan",
            "status": "Running",
            "code_repo_link": "n/a",
            "description": "Extract features of the Car such as model, color, registration number, defects and scratches from the input car image using image processing models.",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:f:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/Park%20Easy?csf=1&web=1&e=jeD3yX",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "valet-keys.jpg")
        },
        {
            "name": "FinBot - A Financial ChatBot",
            "deployment_links": "https://huggingface.co/spaces/maitykritadhi/Kr_Financial_Chatbot_StreamLitUI",
            "creator": "Kritadhi Maity",
            "status": "Running",
            "code_repo_link": "https://huggingface.co/spaces/maitykritadhi/Groq_Financial_Chatbot_Streamlit_UI/tree/main",
            "description": "Analyzes the financial reports of different companies and provide a QA functionality where user can query the bot to get different financial metrics information from documents and perform comparative analysis based on multiple financial reports.",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:w:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/Financial%20Chatbot%20documentation.docx?d=wb650909fbb9d4c7988422c47bb385ee3&csf=1&web=1&e=9LxapJ",
            "icon_path": os.path.join(cf.BASE_PATH, "icons", "Chatbots-for-financial-services.jpg")
        },
        {
            "name": "Forex Trends",
            "deployment_links": "http://13.232.58.176:8002/",
            "creator": "Kritadhi Maity",
            "status": "Running",
            "code_repo_link": "n/a",
            "description": "Bot analyzes online articles and reports to provide daily summarized and latest updates in the Forex market to the user. It also provides dashboard where user can compare and track the general sentiments and trends in the market. ",
            "documentation_link": "https://geminisolutionsindpvtltd-my.sharepoint.com/:p:/r/personal/anang_tomar_geminisolutions_com/Documents/POC%20Documentation/FOREX%20TRENDS.pptx?d=w73fedaa4c39d4877bdad5859889e6484&csf=1&web=1&e=mmKchF",
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
                st.write(f"**Document:** {project['documentation_link']}")
            st.markdown("</div>", unsafe_allow_html=True)
        col_idx = (col_idx + 1) % 4

if __name__ == "__main__":
    tab1, tab2 = st.tabs(["Project Repository", "Project Status Report"])

    with tab1:
        main()

    
      
    with tab2:
        status_report_page()

   


    


   