from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
import sys
from UI import *


app = QApplication(sys.argv) # 运行主循环
app.setWindowIcon(QIcon("logo.png")) #设置窗口左上角图标
window = GPS() # 程序窗口
window.setStyleSheet("#MainWindow{border-image:url(map.jpg)}") # 背景设置地图
ui=Ui()
ui.setupUi(window)
window.show() # 显示
sys.exit(app.exec_()) # 退出主循环