from dotenv import load_dotenv
load_dotenv()

from embedchain import App

harin_bot = App()

# Embed Online Resources
# harin_bot.add("youtube_video", "https://www.youtube.com/watch?v=3qHkcs3kG44")
# harin_bot.add("pdf_file", "https://navalmanack.s3.amazonaws.com/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf")
# harin_bot.add("web_page", "https://nav.al/feedback")
# harin_bot.add("web_page", "https://nav.al/agi")

# Embed Local Resources
# harin_bot.add_local("qna_pair", ("Who is Naval Ravikant?", "Naval Ravikant is an Indian-American entrepreneur and investor."))
f = open("chatData/FullChat.txt", "r")
whatsapp = f.read()
f.close()

harin_bot.add_local("text", whatsapp)

query = None
while (query == None):
    query = input("Enter your query: ")

    if (query == "exit"):
        print("Thanks for using Harin Bot!")
        break

    answer = harin_bot.query(query)
    print(answer)

    query = None