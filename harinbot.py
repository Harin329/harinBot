from dotenv import load_dotenv
load_dotenv()

## For Adding Context
# import os
# import time
# from chromadb.utils import embedding_functions
from embedchain.config import QueryConfig
from string import Template

from embedchain import App

bot_name = "Harin Wu"
speaking_to = "Anna"

harin_bot = App()
query_config = QueryConfig(template=Template(f"""
Use the following pieces of context to continue the conversation. Use slangs from the context.

$context

{speaking_to}: $query

{bot_name}:
"""
))

# Embed Online Resources
# harin_bot.add("youtube_video", "https://www.youtube.com/watch?v=3qHkcs3kG44")
# harin_bot.add("pdf_file", "https://navalmanack.s3.amazonaws.com/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf")
# harin_bot.add("web_page", "https://nav.al/feedback")
# harin_bot.add("web_page", "https://nav.al/agi")
# Embed Local Resources
# harin_bot.add_local("qna_pair", ("Who is Naval Ravikant?", "Naval Ravikant is an Indian-American entrepreneur and investor."))

# f = open("chatData/FullChat.txt", "r")
# whatsapp = f.read()
# f.close()

# harin_bot.add_local("text", whatsapp)

# def get_txt_files():
#     txt_files = []
#     for root, _, files in os.walk("chatData/FB"):
#         for file in files:
#             if file.endswith(".txt"):
#                 txt_files.append(os.path.join(root, file))
#     return txt_files

# fbFiles = get_txt_files()

# for file in fbFiles:
#     fb = open(file, "r")
#     facebook = fb.read()
#     harin_bot.add_local("text", facebook)
#     fb.close()
#     time.sleep(10)

query = None
while (query == None):
    query = input("Enter your query: ")

    if (query == "exit"):
        print("Thanks for using Harin Bot!")
        break

    answer = harin_bot.query(query, query_config)
    print(answer)

    query = None