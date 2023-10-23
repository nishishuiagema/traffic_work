from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPen, QColor
from PyQt5.QtWidgets import QLabel,QWidget,QMainWindow
from dijkstra import dijkstra, matrix


point = [[0, 310, "汉字主题文化公园"],
        [290, 30, "香溢华府"],
        [260, 80, "黄金家园"],
        [90, 130, "倞华菲尔雪公司"],
        [170, 240, "赣南医学院第一附属医院"],
        [250, 320, "金湾广场"],
        [200, 440, "联泰天璞"],
        [290, 750, "新旅中书文旅城"],
        [120, 730, "阳光金色春城"],
        [220, 650, "赣州师范高等专科学校"],
        [270, 490, "滨江公园"],
        [340, 620, "新世纪公园"],
        [450, 610, "江山里榕府"],
        [150, 480, "中建三局"],
        [390, 510, "赣州自然博物馆"],
        [340, 360, "紫金广场"],
        [530, 520, "赣州中央公园"],
        [680, 410, "章江湿地公园"],
        [450, 440, "万象城"],
        [440, 390, "章贡区人民法院"],
        [450, 300, "中国建设银行"],
        [390, 270, "赣南科技学院"],
        [370, 210, "杨梅渡公园"],
        [550, 320, "体育馆"],
        [540, 260, "长征广场"],
        [480, 190, "渔湾里美食广场"],
        [500, 460, "中创购物广场"],
        [540, 400, "赣州商会大厦"],
        [610, 490, "赣州市人民医院"],
        [760, 420, "赣州站"],
        [710, 310, "巨亿广场"],
        [820, 260, "赣州森林动物园"],
        [710, 220, "赣州汽车站"],
        [770, 180, "赣州应用技术职业学校"],
        [720, 140, "天竺山公园"],
        [570, 10, "八境公园"],
        [490, 120, "江西理工大学红旗校区"],
        [340, 150, "锦江国际酒店"],
        [420, 130, "大润发"],
        [500, 160, "赣南师范大学科技学院"]]


spoint = 0 # 起点
epoint = 0 # 终点
distance = 0 # 距离
a=[] # 存储路径


class Ui(object): #ui界面设计
    def setupUi(self, MainWindow): # 建立窗口
        global spoint, epoint, distance
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1231, 791)
        MainWindow.setFixedSize(1231, 791)
        self.centralwidget = QtWidgets.QWidget(MainWindow) # 中心布局
        self.centralwidget.setObjectName("centralwidget")
        self.rB=[0 for i in range(len(point))] # 存储点绘制点
        for i in range(len(point)):
            self.rB[i] = QtWidgets.QRadioButton(self.centralwidget) # 可选按钮
            self.rB[i].setGeometry(QtCore.QRect(point[i][0],point[i][1], 31, 31))
            self.rB[i].setObjectName("radioButton_"+str(i))
            if i == 0:
                self.rB[i].setChecked(True) #初始选择位置
            self.rB[i].setStyleSheet("QRadioButton{border-image: url(location.png)}") # 图标


        self.start=QLabel(self.centralwidget) # 起点标签
        self.start.move(990, 130)
        self.start.resize(141, 61)
        font1 = QtGui.QFont()
        font1.setPointSize(12)
        self.start.setFont(font1)
        self.start.setWordWrap(True)
        self.start.setText("起点是：")


        self.spoint=QLabel(self.centralwidget) # 起点
        self.spoint.move(1060, 130)
        self.spoint.resize(141, 61)
        self.spoint.setFont(font1)
        self.spoint.setWordWrap(True)


        self.end = QLabel(self.centralwidget) # 终点
        self.end.move(990, 340)
        self.end.resize(141, 61)
        self.end.setFont(font1)
        self.end.setWordWrap(True)
        self.end.setText("终点是：")


        self.epoint=QLabel(self.centralwidget) # 终点标签
        self.epoint.move(1060, 340)
        self.epoint.resize(141, 61)
        self.epoint.setFont(font1)
        self.epoint.setWordWrap(True)


        self.distance = QLabel(self.centralwidget) # 距离
        self.distance.move(990, 540)
        self.distance.resize(201, 21)
        self.distance.setFont(font1)
        self.distance.setText("距离约：")


        self.set_spoint=QtWidgets.QPushButton(self.centralwidget) # 选择起点按钮
        self.set_spoint.setText("将选中点设为起点")
        self.set_spoint.resize(201, 81)
        self.set_spoint.move(990, 40)
        font2 = QtGui.QFont()
        font2.setPointSize(13)
        self.set_spoint.setFont(font2)
        self.set_spoint.clicked.connect(self.start_)


        self.set_epoint = QtWidgets.QPushButton(self.centralwidget) # 选择终点按钮
        self.set_epoint.setText("将选中点设为终点")
        self.set_epoint.resize(201, 81)
        self.set_epoint.move(990, 240)
        self.set_epoint.setFont(font2)
        self.set_epoint.clicked.connect(self.end_)


        self.nav = QtWidgets.QPushButton(self.centralwidget) # 运行导航按钮
        self.nav.setText("开始导航")
        self.nav.resize(201, 81)
        self.nav.move(991, 440)
        self.nav.setFont(font2)
        self.nav.clicked.connect(MainWindow.navigation)
        self.nav.clicked.connect(self.dis)


        self.re_ = QtWidgets.QPushButton(self.centralwidget) # 重新选择按钮
        self.re_.setText("重新选择")
        self.re_.resize(181, 51)
        self.re_.move(1010, 670)
        font3 = QtGui.QFont()
        font3.setPointSize(11)
        self.re_.setFont(font3)
        self.re_.clicked.connect(self.clear)
        self.re_.clicked.connect(MainWindow.restart)


        self.close = QtWidgets.QPushButton(self.centralwidget) # 关闭系统按钮
        self.close.setText("关闭系统")
        self.close.resize(181, 51)
        self.close.move(1010, 740)
        font3.setPointSize(11)
        self.close.setFont(font3)
        self.close.clicked.connect(MainWindow.close)

        MainWindow.setCentralWidget(self.centralwidget)


    def clear(self): # 重新选择的执行
        global spoint, epoint
        self.spoint.setText("")
        self.epoint.setText("")
        self.distance.setText("距离约：")
        spoint = 0
        epoint = 0
        self.rB[0].setChecked(True)


    def dis(self): # 导航的距离显示
        self.distance.setText("距离约：" + str(round(distance, 2)) + "公里")


    def start_(self): # 设置起点的显示
        global spoint
        for i in range(len(point)):
            if self.rB[i].isChecked() == True:
                spoint=i
                self.spoint.setText(str(point[spoint][2]))
                break


    def end_(self): # 设置终点的显示
        global epoint
        for i in range(len(point)):
            if self.rB[i].isChecked() == True:
                epoint=i
                self.epoint.setText(str(point[epoint][2]))
                break


class GPS(QMainWindow): # 主窗口
    def __init__(self,parent=None): # 初始化
        super(GPS,self).__init__(parent)
        self.setObjectName("MainWindow")
        self.resize(1231, 791)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setWindowTitle("赣州市交通路径导航系统")
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        ui=Ui()
        ui.setupUi(self)


    def paintEvent(self,event): # 绘制路径
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw(qp, a)
        qp.end()


    def draw(self, qb, a=[]):
        pen = QPen(QColor(0, 180, 0), 4)
        qb.setPen(pen)  # 对画笔进行颜色设置，大小设置
        for i in range(len(a)-1): # 开始绘制
            qb.drawLine(point[a[i]][0] + 16, point[a[i]][1] + 16, point[a[i+1]][0] + 16, point[a[i+1]][1] + 16)


    def navigation(self): # 导航 dijkstra算法
        global a, spoint, epoint, distance
        res = dijkstra(matrix, spoint + 1, epoint + 1)
        a = res[1] # 路径
        distance = res[0] # 路径距离
        QWidget.repaint(self)


    def restart(self): # 清除绘制
        global a
        a.clear()
        QWidget.repaint(self)

