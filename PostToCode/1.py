
import io
LIMIT = 10000
file_count = 0

url_list = []
with io.open('Posts.xml','r',encoding='utf-8') as f:
      for line in f:
            url_list.append(line)
            if len(url_list) < LIMIT:
                continue
            file_name = "F:/Data/PostData/Posts_" + str(file_count) + ".xml"
            with io.open(file_name,'w',encoding='utf-8') as file:
                file.write("<posts>\n")
                for url in url_list[:-1]:
                    file.write(url)
                file.write(url_list[-1].strip())
                file.write("\n")
                file.write("</posts>")
                url_list=[]
                file_count+=1
if url_list:
    file_name = "F:/Data/PostData/Posts_" + str(file_count) + ".xml"
    with io.open(file_name,'w',encoding='utf-8') as file:
        file.write("<posts>\n")
        for url in url_list:
            file.write(url)
print("done")
