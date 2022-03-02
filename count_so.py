import os 


for file_num in range(10):
    path = "data"+str(file_num)
    print(path)
    projects = os.listdir(path)
    for i, project in enumerate(projects):
        sofilenum = 0
        commitnum = 0
        filenum = 0
        project_path = path+'/'+project
        iterations = os.listdir(project_path)
        for j,iteration in enumerate(iterations):
            diff_path = project_path + '/' + iteration + '/diff_sort.txt'
            if os.path.isfile(diff_path):
                with open(diff_path,'r') as f:
                    try:
                        lines = f.readlines()
                    except:
                        continue
                    else:
                        commitnum += 1
                        for line in lines:
                            if line[0:4] == 'diff' or line[0:8] == 'new file' or line[0:12] == 'deleted file':
                                find = 0
                                filenum += 1
                                continue
                            if line[0:1] == '+':
                                if find == 0 and 'https://stackoverflow.com' in line:
                                    find = 1
                                    sofilenum += 1
        with open('./count_so_link.txt','a+',encoding='utf-8') as w:
            w.write(project + ' ')
            w.write(str(commitnum) + ' ')
            w.write(str(filenum) + ' ')
            w.write(str(sofilenum))
            w.write('\n')