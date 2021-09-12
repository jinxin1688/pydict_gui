# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QTableWidget, QApplication, QTableWidgetItem, QPushButton, \
    QTextBrowser, QMenu


class Yiceng(QWidget):
    """第一层字典"""
    def __init__(self, zhidian: dict):
        super(Yiceng, self).__init__()
        self.zhidian = zhidian
        self.__initUI()  # 初始化ui
        self.anniubaocun = []  # 按钮保存
        self.jubuzhidian = []  # 局部字典保存
        self.xianchengbiaoji = []  # 启动另外一个窗口时线程标记
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # 将右键菜单绑定到槽函数generateMenu
        self.tableWidget.customContextMenuRequested.connect(self.youjian)

        self.erceng = Erceng()  # 初始化第二层表格
        self.sanceng = Sanceng()  # 初始化第三层显示
        self.chushihua()  # 初始化数据

    def __initUI(self):
        self.setWindowTitle("pydict_gui")
        self.resize(1200, 680)
        layout = QHBoxLayout()
        self.tableWidget = QTableWidget()  # 初始化一个表
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

    def closeEvent(self, QCloseEvent):
        """主窗口关闭事件"""
        self.close()

    def chushihua(self):
        """根据字典初始化行"""
        cd = len(self.zhidian)
        # 初始列
        self.tableWidget.setColumnCount(cd)  # 初始化列
        # 设置标题
        key = [str(x) for x in self.zhidian.keys()]
        self.tableWidget.setHorizontalHeaderLabels(key)
        vol = self.zhidian.values()

        cd = [0, 1]
        for i, v in enumerate(vol):
            if isinstance(v, dict):
                pass
            else:
                if isinstance(v, list):
                    cd.append(len(v))
                else:
                    pass
        cd = max(cd)
        self.tableWidget.setRowCount(cd)  # 初始化行

        bianhao = 0
        for i, v in enumerate(vol):
            if isinstance(v, dict):
                # 又是一个字典
                dataBtn = QPushButton('字典_'+str(bianhao))
                # dateBtn.setStyleSheet(''' text-align : center;
                #                                   background-color : DarkSeaGreen;
                #                                   height : 30px;
                #                                   border-style: outset;
                #                                   font : 13px; ''')

                dataBtn.clicked.connect(lambda: self.chakan2(dataBtn.sender().text()))  # 绑定chakan2函数
                self.anniubaocun.append(dataBtn)
                self.jubuzhidian.append(v)
                self.tableWidget.setCellWidget(0, i, dataBtn)
                bianhao += 1
            else:
                if isinstance(v, list):
                    for ii, vv in enumerate(v):
                        self.tableWidget.setItem(ii, i, QTableWidgetItem(str(vv)))
                else:
                    self.tableWidget.setItem(0, i, QTableWidgetItem(str(v)))

    def chakan2(self, bianhao: str):
        """查看下一层字典"""
        xb = int(bianhao.split("_")[1])
        print(self.jubuzhidian[xb])
        self.erceng.zhidian = self.jubuzhidian[xb]
        self.erceng.run()
        self.erceng.show()

        # t1 = threading.Thread(target=main2, args=(self.jubuzhidian[xb],)).start()

    def youjian(self, pos):
        """右键菜单,显示完整字典"""
        # 计算有多少条数据，默认-1,
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        hangshu = self.tableWidget.rowCount()  # 获取有多少行
        # 表格中只有两条有效数据，所以只在前两行支持右键弹出菜单
        if row_num == -1:
            return
        if row_num < hangshu:  # and row_num >=0 如表格无行row_NUM为-1
            menu = QMenu()
            item1 = menu.addAction(u'查看完整字典')
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
            if action == item1:
                self.sanceng.zhidian = self.zhidian
                self.sanceng.run()
                self.sanceng.show()


class Erceng(QWidget):
    """第二层字典"""
    def __init__(self,):
        super(Erceng, self).__init__()
        self.zhidian = {}
        self.__initUI()  # 初始化ui
        self.anniubaocun = []  # 按钮保存
        self.jubuzhidian = []  # 局部字典保存
        self.xianchengbiaoji = []  # 启动另外一个窗口时线程标记

        # self.chushihua()  # 初始化数据

    def __initUI(self):
        self.setWindowTitle("pydict_gui_2c")
        self.resize(800, 400)
        layout = QHBoxLayout()
        self.tableWidget = QTableWidget()  # 初始化一个表
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)
        self.sanceng = Sanceng()  # 初始化第三层显示

    def closeEvent(self, QCloseEvent):
        """主窗口关闭事件"""
        self.close()

    def run(self):
        """根据字典初进行运行"""
        cd = len(self.zhidian)
        # 初始列
        self.tableWidget.setColumnCount(cd)  # 初始化列
        # 设置标题
        key = [str(x) for x in self.zhidian.keys()]
        self.tableWidget.setHorizontalHeaderLabels(key)
        vol = self.zhidian.values()

        cd = [0, 1]
        for i, v in enumerate(vol):
            if isinstance(v, dict):
                pass
            else:
                if isinstance(v, list):
                    cd.append(len(v))
                else:
                    pass
        cd = max(cd)
        self.tableWidget.setRowCount(cd)  # 初始化行

        bianhao = 0
        for i, v in enumerate(vol):
            if isinstance(v, dict):
                # 又是一个字典
                dataBtn = QPushButton('字典_'+str(bianhao))
                # dateBtn.setStyleSheet(''' text-align : center;
                #                                   background-color : DarkSeaGreen;
                #                                   height : 30px;
                #                                   border-style: outset;
                #                                   font : 13px; ''')

                dataBtn.clicked.connect(lambda: self.chakan2(dataBtn.sender().text()))  # 绑定chakan2函数
                self.anniubaocun.append(dataBtn)
                self.jubuzhidian.append(v)
                self.tableWidget.setCellWidget(0, i, dataBtn)
                bianhao += 1
            else:
                if isinstance(v, list):
                    for ii, vv in enumerate(v):
                        self.tableWidget.setItem(ii, i, QTableWidgetItem(str(vv)))
                else:
                    self.tableWidget.setItem(0, i, QTableWidgetItem(str(v)))

    def chakan2(self, bianhao: str):
        """查看下一层字典"""
        xb = int(bianhao.split("_")[1])
        print(self.jubuzhidian[xb])
        self.sanceng.zhidian = self.jubuzhidian[xb]
        self.sanceng.run()
        self.sanceng.show()


class Sanceng(QWidget):
    def __init__(self,):
        super(Sanceng, self).__init__()
        self.__initUI()  # 初始化ui
        self.zhidian = {}  # 需要显示的字典

    def __initUI(self):
        self.setWindowTitle("pydict_gui_3c")
        self.resize(1000, 400)
        layout = QHBoxLayout()
        self.textBrowser = QTextBrowser()  # 初始化一个文本显示
        layout.addWidget(self.textBrowser)
        self.setLayout(layout)

    def run(self):
        self.textBrowser.setText(str(self.zhidian))


def main2(zhidian: dict):
    app1 = QApplication(sys.argv)
    win2 = Yiceng(zhidian)
    win2.show()
    sys.exit(app1.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    zhidian = {8989: 55, 'b': [66, 55, 22, 33], 'c': 77, 'd': {'aa': 88, 'bb': 77},
               'e': {1: 666, 2: 333, 3: {"xxxs": 888}}}
    win = Yiceng(zhidian)
    win.show()

    sys.exit(app.exec_())
