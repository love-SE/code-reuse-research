from datetime import datetime
import time
import os

# if os.path.isfile(r"F:\\CCFinder\\outModification.txt"):
#     os.remove(r"F:\\CCFinder\\outModification.txt")


allModifyCommit = 0
projects = ['\\AdapterDelegates','\\Album','\\Alink','\\android-beacon-library','\\android-iconify','\\AndroidPicker','\\Android-skin-support','\\Aria','\\cim','\\FileDownloader','\\FlexibleAdapter','\\simplify','\\spring-cloud-alibaba','\\springfox','\\VirtualXposed','\\android-advancedrecyclerview','\\android-betterpickers','\\android-oss','\\BottomBar','\\butterknife','\\camerakit-android','\\cordova-android','\\curator','\\DanmakuFlameMaster','\\dex2jar','\\FastHub','\\feign','\\AndroidSlidingUpPanel','\\flutter_boost','\\GeekNews','\\go-lang-idea-plugin','\\google-java-format','\\gson','\\interview','\\jib','\\AndroidAsync','\\Android-BluetoothKit','\\android-classyshark','\\javamelody','\\JsonPath','\\jsoup','\\jvm-serializers','\\android-gif-drawable','\\Android-IMSI-Catcher-Detector','\\android-priority-jobqueue','\\Android-Terminal-Emulator','\\Android-Universal-Image-Loader','\\lettuce-core','\\light-4j','\\Awesome-WanAndroid','\\blade','\\litemall','\\LitePal','\\lombok-intellij-plugin','\\maxwell','\\MusicDNA','\\nanohttpd','\\NetGuard','\\nokogiri','\\okhttp','\\PhotoView','\\physical-web','\\picasso','\\quartz','\\react-native-camera','\\RecyclerViewPager','\\RePlugin','\\retrolambda','\\RxJava-Android-Samples','\\scribejava','\\smile','\\uhabits','\\conductor','\\CtCI-6th-Edition','\\docker-maven-plugin','\\Douya','\\eladmin','\\Fast-Android-Networking','\\flyway','\\glide','\\jacoco','\\javacpp','\\joda-time','\\JustAuth','\\Material-Movies','\\mp4parser','\\parceler','\\react-native-video','\\RxEasyHttp','\\Sentinel','\\spring-cloud-gateway','\\spring-security-oauth','\\storio','\\tablesaw','\\transferee','\\usb-serial-for-android','\\VasSonic','\\volley','\\WebCollector','\\webmagic','\\xUtils3','\\zheng','\\AgentWeb','\\android-gpuimage','\\android-times-square','\\AndroidUtilCode','\\apollo-android','\\armeria','\\aurora-imui','\\auto','\\Bastillion','\\bilibili-android-client','\\bistoury','\\canal','\\Carbon','\\ChatKit','\\easyexcel','\\FizzBuzzEnterpriseEdition','\\Fragmentation','\\greenDAO','\\greys-anatomy','\\hsweb-framework','\\http-request','\\hutool','\\IJPay','\\initializr','\\JSON-java','\\jvm-sandbox','\\light-task-scheduler','\\Algorithms','\\AndroidAutoSize','\\Android-Bootstrap','\\android-job','\\Android-PickerView','\\ansj_seg','\\apollo','\\arthas','\\Auto.js','\\BlurView','\\bytecode-viewer','\\ByteTCC','\\caffeine','\\clojure','\\cucumber','\\dddsample-core','\\DeepLinkDispatch','\\flow','\\frontend-maven-plugin','\\GmsCore','\\incubator-heron','\\zuul','\\yuicompressor','\\xxl-job','\\vlayout','\\vjtools','\\VirtualApp','\\vavr','\\Transitions-Everywhere','\\tape','\\stetho','\\springside4','\\SpringCloud','\\spring-boot-starter','\\SpringBoot-Labs','\\spring-boot-demo','\\sofa-rpc','\\SlidingMenu','\\SimpleCropView','\\ShortcutBadger','\\Shadow','\\server','\\RxAndroidBle','\\RxAndroid','\\rocketmq-externals','\\ribbon','\\rejoiner','\\rabbitmq-tutorials','\\powermock','\\plantuml','\\algs4','\\AndPermission','\\Android-Image-Cropper','\\Android-ObservableScrollView','\\APIJSON','\\atlas','\\BasePopup','\\BookReader','\\cachecloud','\\Crouton','\\Dexter','\\elasticsearch-jdbc','\\epoxy','\\error-prone','\\eureka','\\FrameworkBenchmarks','\\jedis','\\jsonschema2pojo','\\LeafPic','\\libsvm','\\material-components-android','\\MaterialEditText','\\metrics','\\piggymetrics','\\PictureSelector','\\Phonograph','\\PermissionsDispatcher','\\opentsdb','\\onemall','\\gnirehtet','\\Mycat-Server','\\mybatis-3','\\MPAndroidChart','\\interviews','\\java-algorithms-implementation','\\jadx','\\igniter','\\Hystrix','\\hope-boot','\\hmily','\\hive','\\halo','\\graphhopper','\\java-design-patterns','\\javapoet','\\jetcache','\\mall-swarm','\\jjwt','\\JSqlParser','\\lombok','\\mapdb','\\Mapper','\\mockito','\\mybatis','\\objectbox-java','\\okdownload','\\ReactiveNetwork','\\reactive-streams-jvm','\\react-native-svg','\\resilience4j','\\roboguice','\\roncoo-pay','\\shiro','\\smali','\\Small','\\soul','\\spruce-android','\\Timber','\\weiciyuan','\\ahbottomnavigation','\\andOTP','\\Android-CleanArchitecture','\\android-menudrawer','\\android-mvp-mvvm-flytour','\\cglib','\\AndEngine','\\AndResGuard','\\Android-Debug-Database','\\AppUpdate','\\baritone','\\BaseRecyclerViewAdapterHelper','\\binnavi','\\bitcoinj','\\brigadier','\\btrace','\\capacitor','\\CloudReader','\\Conversations','\\crawler4j','\\cryptomator','\\cw-omnibus','\\dagger','\\DependencyCheck','\\disruptor','\\dropwizard','\\dubbo-admin','\\elasticsearch-sql','\\fastjson','\\zxing-android-embedded','\\XUI','\\wiremock','\\vertx-examples','\\UltimateRecyclerView','\\androidannotations','\\android-async-http','\\android-mvp-architecture','\\Android-Week-View','\\angel','\\awaitility','\\azkaban','\\99-problems','\\ActiveAndroid','\\agera','\\AlgoDS','\\android-maps-utils','\\AndroidTVLauncher','\\antlr4','\\banner','\\blueocean-plugin','\\Calligraphy','\\CameraView','\\ChipsLayoutManager','\\Conductor1','\\config','\\data-transfer-project','\\disconf','\\Discovery','\\DKVideoPlayer','\\DoraemonKit','\\DroidPlugin','\\dubbo','\\dynamic-load-apk','\\easy-rules','\\EdXposed','\\EventBus','\\facebook-android-sdk','\\failsafe','\\FirebaseUI-Android','\\flink-learning','\\fresco','\\GCViewer','\\generator','\\Genius-Android','\\google-services','\\gpmall','\\GraphView','\\groupie','\\GSYVideoPlayer','\\guice','\\Guns','\\haven','\\hawk','\\hellocharts-android','\\HikariCP','\\HMCL','\\ice','\\immutables','\\ion','\\Java','\\javacv','\\javaee7-samples','\\javassist','\\java-tron','\\Java-WebSocket','\\JCSprout','\\JCTools','\\jd-gui','\\Jetpack-MVVM-Best-Practice','\\jfinal','\\JFoenix','\\jna','\\jodd','\\jOOR','\\junit4','\\junit5','\\jvm-tools','\\karate','\\keywhiz','\\learning-spark','\\Leetcode1','\\librec','\\libstreaming','\\LifeHelper','\\lottie-android','\\LRecyclerView','\\lucida','\\Luyten','\\MagicIndicator','\\mall','\\malmo','\\mapstruct','\\material','\\material-calendarview','\\MaterialDateTimePicker','\\material-theme-jetbrains','\\MaterialViewPager','\\mockserver','\\moco','\\mosby','\\motan','\\MovieGuide','\\mpush','\\MultiImageSelector','\\MvpApp','\\MVPArms','\\MVVMHabit','\\mybatis-generator-gui','\\Mybatis-PageHelper','\\MyBookshelf','\\nacos','\\NewPipe','\\NullAway','\\nutz','\\okhttp-OkGo','\\onedev','\\OpenHub','\\OpenRefine','\\PageIndicatorView','\\PhotoEditor','\\PhotoPicker','\\picocli','\\PlayerBase','\\PowerJob','\\PreviewSeekBar','\\quasar','\\react-native-image-picker','\\react-native-push-notification','\\react-native-share','\\red5-server','\\requery','\\rest-assured','\\retrofit','\\RichText','\\robotium','\\Robust','\\RoundedImageView','\\RxPermissions','\\seata','\\SimianArmy','\\simple-binary-encoding','\\SmartRefreshLayout','\\socket.io-client-java','\\sofa-boot','\\spock','\\spring-boot-admin','\\SpringBoot-Learning','\\spring-cloud-netflix','\\Spring-Cloud-Platform','\\spring-data-examples','\\spring-petclinic','\\spring-security','\\StickyListHeaders','\\subsampling-scale-image-view','\\sugar','\\swagger-core','\\TableView','\\Tangram-Android','\\testcontainers-java','\\thumbnailator','\\T-MVP','\\tray','\\Twitter4J','\\tx-lcn','\\u2020','\\uCrop','\\UETool','\\web3j','\\WheelPicker','\\xboot','\\XCL-Charts','\\XPopup','\\XposedInstaller','\\YCSB','\\ysoserial','\\zeppelin','\\zipkin','\\zookeeper','\\AndroidPhotoFilters','\\AndroidResideMenu','\\AndroidSwipeLayout','\\BubbleSeekBar','\\CalendarView','\\DataMiningAlgorithm','\\FloatingActionButton','\\HTextView','\\ImagePicker','\\InfiniteCycleViewPager','\\JamsMusicPlayer','\\LoganSquare','\\MarqueeView','\\MasteringAndroidDataBinding','\\NoHttp','\\Play-with-Algorithms','\\RxGalleryFinal','\\RxLifecycle','\\SmoothProgressBar','\\StatusBarUtil','\\StylishMusicPlayer','\\SuperRecyclerView','\\SwipeDelMenuLayout','\\VideoPlayerManager','\\ViewPagerIndicator','\\XhsEmoticonsKeyboard','\\ZLayoutManager','\\baseAdapter','\\bottomsheet','\\coursera-android','\\deeplearning4j','\\dexposed','\\dialogplus','\\floatingsearchview','\\google-authenticator','\\ignite','\\lanproxy','\\react-native-fbsdk','\\rocketmq','\\smartTable','\\spring-loaded','\\tsunami-security-scanner','\\vhr','\\ARouter','\\Android-ZBLibrary','\\AndroidPdfViewer','\\AndroidPerformanceMonitor','\\AndroidProcess','\\BigData-Notes','\\CityPicker','\\CommonUtilLibrary','\\Depth-LIB-Android-','\\FadingActionBar','\\FlowLayout','\\Grav','\\JAViewer','\\Material-Animations','\\MaterialSearchView','\\Matisse','\\MinimalistWeather','\\PagerBottomTabStrip','\\SeeWeather','\\SlidingTutorial-Android','\\SoloPi','\\TakePhoto','\\TinyPinyin','\\VBlog','\\airpal','\\android-crop','\\android-flip','\\android-saripaar','\\android-stackblur','\\android-vision','\\cordova-plugin-local-notifications','\\databus','\\drag-sort-listview','\\easypermissions','\\gradle-retrolambda','\\graphql-java','\\hover','\\incubator-dolphinscheduler','\\java-jwt','\\jeecg-boot','\\jwt-spring-security-demo','\\lottie-react-native','\\lwjgl3','\\material-intro-screen','\\okhttputils','\\shimmer-android','\\spring-boot-projects','\\spring-boot','\\AVLoadingIndicatorView','\\CustomActivityOnCrash','\\DDComponentForAndroid','\\DropDownMenu','\\ExpectAnim','\\GravitySnapHelper','\\InstaMaterial','\\JsBridge','\\MaterialDesignLibrary','\\NineGridView','\\Phoenix','\\QLExpress','\\RIBs','\\Slidr','\\SpringCloudLearning','\\Sunshine-Version-2','\\TwinklingRefreshLayout','\\VirtualAPK','\\android-Ultra-Pull-To-Refresh','\\android-common','\\android-floating-action-button','\\android-mvvm-architecture','\\android-pathview','\\archi','\\condom','\\effective-java-3e-source-code','\\java-learning','\\java8-tutorial','\\kkFileView','\\nice-spinner','\\shopping-management-system','\\spring-analysis','\\spring-boot-api-project-seed','\\testing-samples','\\xmall','\\zxing','\\AndroidImageSlider','\\AndroidTutorialForBeginners','\\CheckVersionLib','\\FlowingDrawer','\\ForestBlog','\\GT','\\Highlight','\\HomeMirror','\\PRDownloader','\\ShineButton','\\SimplifyReader','\\SpringBlade','\\SwipeMenuListView','\\TapTargetView','\\android-process-button','\\android-shape-imageview','\\androidmvp','\\dockerfile-maven','\\emojicon','\\epic','\\excelPanel','\\jackson-databind','\\miaosha','\\overscroll-decor','\\pixel-dungeon','\\metersphere','\\springboot-guide','\\sticky-headers-recyclerview','\\ticker','\\tiny-spring','\\AndroidChromium','\\AndroidVideoCache','\\BottomNavigationViewEx','\\BottomNavigation','\\COLA','\\DeepLearning','\\DiscreteScrollView','\\EffectiveAndroidUI','\\FEBS-Shiro','\\FloatWindow','\\IntelliJ-Key-Promoter-X','\\JKeyboardPanelSwitch','\\LiveEventBus','\\PLDroidPlayer','\\RecyclerViewItemAnimators','\\RxJava2Examples','\\SpringIndicator','\\StickerCamera','\\StickyHeaderListView','\\SuperTextView','\\SystemBarTint','\\android-pdfview','\\ffmpeg-android-java','\\micrometer','\\netty-learning','\\otter','\\reflections','\\webporter','\\AndroidHttpCapture','\\AndroidStaggeredGrid','\\BadgeView','\\Blurry','\\DSBridge-Android','\\FastBle','\\GreenDroid','\\GuideView','\\JJSearchViewAnim','\\Leaf','\\LikeButton','\\MagicaSakura','\\MaterialIntroView','\\OsmAnd','\\RxJava2-Android-Samples','\\SwipeBackLayout','\\VitamioBundle','\\android-open-source-project-analysis','\\aws-sdk-java','\\blurkit-android','\\boxing','\\chuck','\\cropper','\\grafika','\\jetty.project','\\jstorm','\\logger','\\mall-learning','\\sensey','\\springboot-learning-example','\\AarogyaSetu','\\Android-ConvenientBanner','\\AndroidTreeView','\\AnimationEasingFunctions','\\CircleIndicator','\\DiskLruCache','\\LayoutManagerGroup','\\LoadSir','\\NiftyDialogEffects','\\RippleEffect','\\RxJavaSamples','\\ShadowImageView','\\Skeleton','\\SlidingRootNav','\\StepView','\\WoWoViewPager','\\awesome-java-leetcode','\\cobar','\\ctci','\\elasticsearch-analysis-ik','\\ksql','\\loaderviewlibrary','\\netty-socketio','\\paascloud-master','\\richeditor-android','\\tcc-transaction','\\termex-app','\\vespa','\\ActivityRouter','\\Android-Skin-Loader','\\AndroidAutoLayout','\\AndroidFire','\\BackgroundLibrary','\\BigImageViewer','\\CC','\\CircularReveal','\\Cockroach','\\DiagonalLayout','\\FlycoTabLayout','\\GalleryFinal','\\GsonFormat','\\JavaVerbalExpressions','\\ListenerMusicPlayer','\\Luban','\\MagicCamera','\\MaterialChipsInput','\\MaterialShowcaseView','\\Nuwa','\\RecyclerView-FlexibleDivider','\\ShapeOfView','\\SopCastComponent','\\SwitchButton','\\ThreeTenABP','\\Toasty','\\UltraViewPager','\\android-zxingLibrary','\\cardslib','\\dubbo-spring-boot-project','\\fnlp','\\freeline','\\linuxdeploy','\\material-menu','\\v9porn','\\Android-SpinKit','\\AndroidProject','\\AndroidViewAnimations','\\BGABanner-Android','\\BGARefreshLayout-Android','\\BoomMenu','\\CircleProgress','\\CoordinatorBehaviorExample','\\Java8InAction','\\KenBurnsView','\\NavigationTabBar','\\NewbieGuide','\\PatternLockView','\\ProgressManager','\\PullZoomView','\\SmartTabLayout','\\Unblock163MusicClient-Xposed','\\XRecyclerView','\\afinal','\\android-hidden-api','\\android-signaturepad','\\best-pay-sdk','\\cassandra','\\glide-transformations','\\graal','\\native-navigation','\\spring-cloud-rest-tcc','\\understand-plugin-framework','\\wechat','\\wildfly','\\AndServer','\\Android-Material-Examples','\\AndroidTagGroup','\\BGABadgeView-Android','\\CoCoin','\\FabulousFilter','\\FastDev4Android','\\FlyRefresh','\\GuillotineMenu-Android','\\ImmersionBar','\\LoadingDrawable','\\MyBatis-Spring-Boot','\\RecyclerViewCardGallery','\\SuperCalendar','\\SwipeRecyclerView','\\ViewAnimator','\\android-material-design-icon-generator-plugin','\\ballerina-lang','\\hugo','\\joda-time-android','\\packer-ng-plugin','\\remusic','\\spring-boot-examples','\\spring-mvc-showcase','\\springBoot','\\sweet-alert-dialog','\\LoadingView','\\spring-data-elasticsearch','\\AmazeFileManager']
#projects = ['\\AarogyaSetu']
for project in projects:
    print(project)

    fileName = []
    realFileName = []
    clonePairs = []
    clonePairs1 = []

    creationStr = "//CreationDate = "

    def readSO(fileInfo):
        sp1 = fileInfo.split('.')
        fileIndex = int(sp1[0]) - 1
        SOfile = open(fileName[fileIndex],'r', encoding='UTF-8')
        for line in SOfile:
            if creationStr in line:
                return line[17:27]
        return "2008-01-01"

    def readCommit(fileInfo):
        sp1 = fileInfo.split('.')
        fileIndex = int(sp1[0]) - 1
        SOfile = open(fileName[fileIndex],'r', encoding='UTF-8')
        line = SOfile.readline()
        SOfile.close()
        pretime = line[12:]
        time = datetime.strptime(pretime, '%a %b %d %H:%M:%S CST %Y\n').strftime('%Y-%m-%d')
        return time,fileName[fileIndex]
        return "2008-01-01"





    file = open(r"F:\CCFinder\\testAns" + project + ".txt")
    allCommit = 0
    numOfFile = 0
    # allCommit = [0 for i in range(4)] #add delete update other
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
                numOfFile = numOfFile + 1
                if "NewData" in listName[1]:
                    file1 = open(listName[1],'r', encoding='UTF-8')
                    line1 = file1.readline()
                    line1 = file1.readline()
                    name = line1.split('/new/')[1]
                    realFileName.append(name)
                    # allCommit[typeIndex] = allCommit[typeIndex] + 1
                    file1.close()

        if line == 'clone_pairs {\n':
            while 1:
                PairsLine = file.readline()
                if PairsLine == '}\n':
                    break
                clonePairs1.append(PairsLine)
    file.close()

    numOfFile = int(numOfFile/2)
    existFile = []
    modificationFile = []
    for i in range(len(clonePairs1)//2):
        listPair = clonePairs1[i].split('\t')
        fileNo1 = int(listPair[1].split('.')[0])
        fileNo2 = int(listPair[2].split('.')[0]) - numOfFile
        if fileNo1 == fileNo2:
            # print(clonePairs1[i])
            continue
        if realFileName[fileNo1] != realFileName[fileNo2]:
            continue
        if fileNo1 in existFile:
            if fileNo2 not in existFile:
                existFile.append(fileNo2)
                allModifyCommit = allModifyCommit + 1
            continue
        allCommit = allCommit + 1
        modificationFile.append(fileNo1)
        existFile.append(fileNo1)
        existFile.append(fileNo2)
        allModifyCommit = allModifyCommit + 2
        # modificationFile.append(fileNo2)
        # print(fileNo1)







    file = open(r"F:\CCFinder\NewAns" + project + ".txt")
    find = 0
    firstNo = 0
    # allCommit = [0 for i in range(4)] #add delete update other
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
                if find == 0 and "NewData" in listName[1]:
                    find = 1
                    firstNo = int(listName[0]) - 1

        if line == 'clone_pairs {\n':
            while 1:
                PairsLine = file.readline()
                if PairsLine == '}\n':
                    break
                clonePairs.append(PairsLine)
    file.close()

    # print('firstNo:',firstNo)
    res = 0
    hashTable = {}

    for i in range(len(clonePairs)//2):
        listPair = clonePairs[i].split('\t')

        fileNo = int(listPair[2].split('.')[0]) - firstNo
        # print(fileNo)
        if fileNo not in modificationFile:
            continue
        time1 = readSO(listPair[1])
        time2,Commitfile = readCommit(listPair[2])
        # print(time1,time2)
        #print(time2)
        if(time1 < time2):
            if hashTable. __contains__(Commitfile):
                hashTable[Commitfile] = hashTable[Commitfile] + 1
            else:
                hashTable[Commitfile] = 1
                # sp = Commitfile.split('\\')
                # yearIndex = sp[4]
                res = res + 1
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
    Output = open(r"F:\\CCFinder\\outModification.txt",'a+')
    Output.write(str(allCommit))
    Output.write('\t')
    Output.write(str(res))
    Output.write('\n')
    Output.close()
print(str(allModifyCommit))