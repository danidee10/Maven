__author__ = 'danidee'
import os
import sys
import time
from paths import *



def main():
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('img/icon.png'))
    if os.name == 'nt':
        # This is needed to display the app icon on the taskbar on Windows 7,8 and 10
        import ctypes
        myappid = 'MavenIcon...version 1.0'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
            
    pixmap = QtGui.QPixmap('img/splash.png')
    splash = QtGui.QSplashScreen(pixmap)
    splash.show()
    app.processEvents()
    time.sleep(3)
    activity = criticalPath()
    activity.get_num_act()
    activity.show()
    splash.finish(activity)
    sys.exit(app.exec_())

if __name__ == '__main__': main()
