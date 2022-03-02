from datetime import datetime
import time
import os
from tqdm import tqdm
if os.path.isfile(r"F:\\CCFinder\\outType.txt"):
    os.remove(r"F:\\CCFinder\\outType.txt")


# projects = ['\\SmartTabLayout','\\Unblock163MusicClient-Xposed','\\XRecyclerView','\\afinal','\\android-hidden-api','\\android-signaturepad','\\best-pay-sdk','\\cassandra','\\glide-transformations','\\graal','\\native-navigation','\\spring-cloud-rest-tcc','\\understand-plugin-framework','\\wechat','\\wildfly','\\AndServer','\\Android-Material-Examples','\\AndroidTagGroup','\\BGABadgeView-Android','\\CoCoin','\\FabulousFilter','\\FastDev4Android','\\FlyRefresh','\\GuillotineMenu-Android','\\ImmersionBar','\\LoadingDrawable','\\MyBatis-Spring-Boot','\\RecyclerViewCardGallery','\\SuperCalendar','\\SwipeRecyclerView','\\ViewAnimator','\\android-material-design-icon-generator-plugin','\\ballerina-lang','\\hugo','\\joda-time-android','\\packer-ng-plugin','\\remusic','\\spring-boot-examples','\\spring-mvc-showcase','\\springBoot','\\sweet-alert-dialog','\\LoadingView','\\spring-data-elasticsearch']
# projects = ['\\Album']

projects = os.listdir('F:\\CCFinder\\NewAns')
projects = list(set(['\\'+i.split('.txt')[0] for i in projects if i.endswith('.txt')]))
projects.sort()


with open('F:\\CCFinder\\Type_names.txt','w') as f:
    text = '\n'.join([i.split('\\')[1] for i in projects])
    f.write(text)



for project in tqdm(projects):
    print(project)

    fileName = []
    clonePairs = []

    creationStr = "//CreationDate = "

    def readSO(fileInfo):
        sp1 = fileInfo.split('.')
        fileIndex = int(sp1[0]) - 1

        file_name = fileName[fileIndex]


        if 'xxx' in file_name:
            file_name = file_name.replace('\\wt', 'CCFinder')

        SOfile = open(file_name,'r', encoding='UTF-8')
        for line in SOfile:
            if creationStr in line:
                return line[17:27]
        return "2008-01-01"

    def readCommit(fileInfo):
        sp1 = fileInfo.split('.')
        fileIndex = int(sp1[0]) - 1
        SOfile = open(fileName[fileIndex],'r', encoding='UTF-8')
        line = SOfile.readline()
        line1 = SOfile.readline()
        line1 = SOfile.readline()
        SOfile.close()
        pretime = line[12:]
        time = datetime.strptime(pretime, '%a %b %d %H:%M:%S CST %Y\n').strftime('%Y-%m-%d')
        typeIndex = 3

        typeIndex = 3
        if "ADD" in line1 or "INSERT" in line1:
            typeIndex = 0
        if "DELETE" in line1 or "REMOVED" in line1 or 'REMOVING' in line1 or 'MOVE' in line1:
            typeIndex = 1
        if "UPDATE" in line1 or 'CHANGE' in line1 or 'RENAMING' in line1:
            typeIndex = 2


        return time,fileName[fileIndex],typeIndex
        return "2008-01-01"


    # Commitdir = r'F:\CCFinder\NewData' + project
    # CommitList = os.listdir(Commitdir)
    # IndexToYear = [0 for i in range(len(CommitList)-1)]
    # for i in range(1, len(CommitList)):
    #     FilePath = os.path.join(Commitdir, CommitList[i])
    #     FirstFileName = os.listdir(FilePath)
    #     FirstFile = os.path.join(FilePath, FirstFileName[0])

    #     SOfile = open(FirstFile, 'r', encoding = 'UTF-8')
    #     line = SOfile.readline()
    #     SOfile.close()
    #     pretime = line[12:]
    #     year = datetime.strptime(pretime, '%a %b %d %H:%M:%S CST %Y\n').strftime('%Y')
    #     year = int(year) - 2001

    #     sp0 = FirstFile.split('\\')
    #     yearIndex1 = sp0[4]
    #     IndexToYear[int(yearIndex1)] = year
    #     print(IndexToYear)


    file = open(r"F:\CCFinder\NewAns" + project + ".txt")
    allCommit = [0 for i in range(3)] #add delete update other
    while 1:
        line = file.readline()
        if not line:
            break

        if line == 'source_files {\n':
            while 1:
                fileLine = file.readline()
                if fileLine == '}\n':
                    break
                listName = fileLine.split('\t')
                fileName.append(listName[1])
                if "NewData" in listName[1]:
                    file1 = open(listName[1],'r', encoding='UTF-8')
                    line1 = file1.readline()
                    line1 = file1.readline()
                    line1 = file1.readline()
                    typeIndex = 3
                    if "ADD" in line1 or "INSERT" in line1:
                        typeIndex = 0
                    if "DELETE" in line1 or "REMOVED" in line1 or 'REMOVING' in line1 or 'MOVE' in line1:
                        typeIndex = 1
                    if "UPDATE" in line1 or 'CHANGE' in line1 or 'RENAMING' in line1:
                        typeIndex = 2
                    allCommit[typeIndex] = allCommit[typeIndex] + 1
                    file1.close()

        if line == 'clone_pairs {\n':
            while 1:
                PairsLine = file.readline()
                if PairsLine == '}\n':
                    break
                clonePairs.append(PairsLine)
    file.close()

    res = [0 for i in range(3)]
    hashTable = {}

    for i in range(len(clonePairs)//2):
        listPair = clonePairs[i].split('\t')

        time1 = readSO(listPair[1])
        time2,Commitfile,typeIndex = readCommit(listPair[2])
        #print(time2)



        if(time1 < time2):
            if hashTable. __contains__(Commitfile):
                hashTable[Commitfile] = hashTable[Commitfile] + 1
            else:
                hashTable[Commitfile] = 1
                # sp = Commitfile.split('\\')
                # yearIndex = sp[4]
                res[typeIndex] = res[typeIndex] + 1
    #             print(yearIndex + "IndexToYear" + str(IndexToYear[int(yearIndex)]))
    #             print("time1:" + time1 + "    time2:" + time2)
    # print(allCommit)
    # print(res)
    # ratio = [0 for i in range(20)]
    # for i in range(20):
    #     if(allCommit[i] != 0):
    #         ratio[i] = round(res[i]/allCommit[i],4)
    # print(ratio)
    # print(IndexToYear)



    Output = open(r"F:\\CCFinder\\outType.txt",'a+')
    for i in range(len(allCommit)):
        Output.write(str(allCommit[i]))
        Output.write('\t')
    Output.write('\t\t')
    for i in range(len(res)):
        Output.write(str(res[i]))
        Output.write('\t')
    Output.write('\n')
    Output.close()
