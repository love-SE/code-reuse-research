
from xml.dom.minidom import parse
import xml.dom.minidom
import re
from tqdm import tqdm

all_num = 0
sum_num = 0
java_num = 0
p = re.compile(r'<code>([\s\S]*?)</code>')

for postnum in tqdm(range(0,5217)):
    codefile = "F:/Data/CodeData/code_" + str(postnum) + ".java"
    with open(codefile, 'wt', encoding='utf-8') as f:

        file_name = "F:/Data/PostData/Posts_" + str(postnum) + ".xml"
        DOMTree = xml.dom.minidom.parse(file_name)
        collection = DOMTree.documentElement

        rows = collection.getElementsByTagName("row")
        for row in rows:
            all_num += 1
            flag = 0
            if row.hasAttribute("Body"):
                if row.hasAttribute("Tags"):
                    if "<java>" in row.getAttribute("Tags"):
                        sum_num += 1
                        mylist = p.findall(row.getAttribute("Body"))
                        for i in mylist:
                            if len(i) > 30:
                                print(i, file = f)
                                flag = 1
                        if flag == 1:
                            java_num += 1
                            if row.hasAttribute("CreationDate"):
                                print("//CreationDate = " + row.getAttribute("CreationDate") ,end = "", file = f)
                            print("//Tags = " + row.getAttribute("Tags"),end = "",file = f)
                            if row.hasAttribute("row Id"):
                                print("//row Id = " + row.getAttribute("row Id") ,end = "", file = f)
                            if row.hasAttribute("Score"):
                                print("//Score = " + row.getAttribute("Score") ,end = "",file = f)
                            if row.hasAttribute("Title"):
                                print("//Title = " + row.getAttribute("Title"),end = "",file = f)
                            if row.hasAttribute("AnswerCount"):
                                print("//AnswerCount = " + row.getAttribute("AnswerCount") ,end = "",file = f)
                            if row.hasAttribute("CommentCount"):
                                print("//CommentCount = " + row.getAttribute("CommentCount"),end = "",file = f)
                            if row.hasAttribute("FavoriteCount"):
                                print("//FavoriteCount = " + row.getAttribute("FavoriteCount"),end = "",file = f)
                            print("",file = f)
print(all_num)
print(sum_num)
print(java_num)
