
import io
LIMIT = 1300
for num in range(0,5217):
    url_list = []
    order = 0
    open_name = "F:/Data/CodeData/code_" + str(num) + ".java"
    with io.open(open_name,'r',encoding='utf-8') as f:
        for line in f:
            url_list.append(line)
            if len(url_list) < LIMIT:
                continue
            file_name = "F:/Data/CodeData01/code_" + str(num) + "_" + str(order)+ ".java"
            order += 1
            with io.open(file_name,'w',encoding='utf-8') as file:
                for url in url_list[:-1]:
                    file.write(url)
                file.write(url_list[-1].strip())
                url_list=[]
    if url_list:
        file_name = "F:/Data/CodeData01/code_" + str(num) + "_" + str(order)+ ".java"
        with io.open(file_name,'w',encoding='utf-8') as file:
            for url in url_list:
                file.write(url)
print("done")
