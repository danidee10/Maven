__author__ = 'danidee'
import os
import sys
import time
from paths import criticalPath, QtGui



def main():
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('img/icon.png'))
    if os.name == 'nt':
        # This is needed to display the app icon on the taskbar on Windows 7,8 and 10
        import ctypes
        myappid = 'Maven....version 1.0'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
            
    pixmap = QtGui.QPixmap('img/splash.png')
    splash = QtGui.QSplashScreen(pixmap)
    splash.show()
    app.processEvents()
    time.sleep(3)
    activity = criticalPath()
    splash.finish(activity)
    activity.get_num_act()
    activity.show()
    sys.exit(app.exec_())

if __name__ == '__main__': main()
