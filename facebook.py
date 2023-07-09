import os
from bs4 import BeautifulSoup

def get_html_files():
    html_files = []
    for root, _, files in os.walk("chatData/inbox"):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files

files = get_html_files()
num_files = len(files)

for fileNum in range(num_files):
    file = files[fileNum]
    # write to file
    f = open("chatData/FB/FBChat" + str(fileNum) + ".txt", "w")

    print(file)
    with open(file, 'r') as file:
        beautifulSoupText = BeautifulSoup(file.read(), 'html.parser')
            
        divs = beautifulSoupText.find_all("div", {"class": "_3-95 _a6-g"})
        for div in divs:
            sender = div.find("div", {"class": "_2ph_ _a6-h _a6-i"})
            if (sender and sender.text == "Harin Wu"):
                div2 = div.find("div", {"class": "_2ph_ _a6-p"})
                msgLine = sender.text + ": " + div2.text + "\n\n"
                # write to file
                f.write(msgLine)

    f.close()

    