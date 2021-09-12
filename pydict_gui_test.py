# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from pydict_gui import Yiceng


if __name__ == '__main__':
    app = QApplication(sys.argv)
    zhidian = {8989: 55, 'b': [66, 55, 22, 33], 'c': 77, 'd': {'aa': 88, 'bb': 77},
               'e': {1: 666, 2: 333, 3: {"xxxs": 888}}}
    win = Yiceng(zhidian)
    win.show()
    sys.exit(app.exec_())
