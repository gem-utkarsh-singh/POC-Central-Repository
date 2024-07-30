import time
from document_information import func1
from britvic import britvic
from fx_sentiment import fx
from park_easy import park_easy
from financial_chatbot import financial_chatbot
from document_intelligence import doc_intelligence
from document_insight import doc_insight
from Organization_structure import org_struc
from WebInspect_AI import web_inspect

# input files
file_doc_info = r'/home/ubuntu/POC-Central-Repository/DOCS/POCs Sample documents/Document Information Retrieval Bot/bol.pdf'
text_to_enter1 = "2017/04/01"
text_to_enter2 = "2024/07/01"
file_park_easy = r'/home/ubuntu/POC-Central-Repository/DOCS/POCs Sample documents/Park Easy/toyota_fortuner_front.jpg'
file_doc_intelligence = r'/home/ubuntu/POC-Central-Repository/DOCS/POCs Sample documents/Document Intelligence Bot/environmental-statement-pune-phase1-2022.pdf'
file_doc_insight = r'/home/ubuntu/POC-Central-Repository/DOCS/POCs Sample documents/earnings call report docs/META-Q1-2023-Earnings-Call-Transcript.pdf'
file_org1 = r'/home/ubuntu/POC-Central-Repository/DOCS/POCs Sample documents/organization structure docs/ex_3_document_1.pdf'
file_org2 = r'/home/ubuntu/POC-Central-Repository/DOCS/POCs Sample documents/organization structure docs/ex_3_document_2.pdf'
text_to_enter = "https://www.saucedemo.com/"





# function calls


result1 = func1(file_doc_info)
print(f"{result1}")
time.sleep(5)

result2 = britvic()
print(f"{result2}")
time.sleep(5)

result3 = fx(text_to_enter1, text_to_enter2)
print(f"{result3}")
time.sleep(5)

result4 = park_easy(file_park_easy)
print(f"{result4}")
time.sleep(5)

result5 = financial_chatbot()
print(f"{result5}")
time.sleep(10)

result6 = doc_intelligence(file_doc_intelligence)
print(f"{result6}")
time.sleep(5)

result7 = doc_insight(file_doc_insight)
print(f"{result7}")
time.sleep(10)

result8 = org_struc(file_org1, file_org2)
print(f"{result8}")
time.sleep(10)

result9 = web_inspect(text_to_enter)
print(f"{result9}")
time.sleep(5)





