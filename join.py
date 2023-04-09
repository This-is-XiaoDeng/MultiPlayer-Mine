from PySide6.QtWidgets import *
from ui_join import *
import sys
import getpass
import logging
import PySide6.QtCore

logging.basicConfig(
    format="[%(asctime)s][%(name)s / %(levelname)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level = logging.DEBUG
)
# logger = logging.getLogger("join_window")
logger = logging.getLogger(__name__)



class Join(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 绑定事件
        self.commandLinkButton.clicked.connect(self.join_game)
        self.lineEdit_2.setText(getpass.getuser())
        self.lineEdit_6.setText(getpass.getuser())
        self.setWindowTitle("Multiplayer Mine v1.0.0-dev (By This-is-XiaoDeng)")
        self.spinBox_2.setValue(25760)
        self.spinBox.setValue(25760)
        
        # 显示窗口
        self.show()
        logger.info("窗口已加载")
    
    def join_game(self):
        logger.info("点击按钮：立即加入")
        self.tabWidget.setEnabled(False)
        self.client_type = self.toolBox.currentIndex()
        self.host_addr = self.get_host_addr()
        self.username = self.get_username()
        self.passwd = self.get_password()
        
        # 输出信息
        logger.debug(f"客户端类型：{self.client_type}")
        logger.debug(f"主机信息：{self.host_addr}")
        logger.debug(f"用户名：{self.username}")
        logger.debug(f"加入密钥：{self.passwd}")
        logger.info("正在关闭窗口 ...")
        self.close()
    
    def get_host_addr(self):
        if self.client_type:
            ip = self.lineEdit_3.text()
        else:
            ip = self.lineEdit.text()
        
        if self.client_type:
            port = self.spinBox_2.value()
        else:
            port = self.spinBox.value()
            
        return (ip, int(port))
            
    def get_username(self):
        if self.client_type:
            return self.lineEdit_6.text()
        else:
            return self.lineEdit_2.text()
            
    def get_password(self):
        if self.client_type:
            return self.lineEdit_4.text()
        else:
            return self.lineEdit_5.text()
        
        
    
    def __del__(self):
        logger.info("窗口关闭")
        
def show():
    logger.info("正在加载窗口 ...")
    
    app = QApplication(sys.argv)
    window = Join()
    app.exec()
    return {
        "type": window.client_type,
        "addr": window.host_addr,
        "username": window.username,
        "password": window.passwd
    }
    

PySide6.QtCore.QCoreApplication.addLibraryPath(r"c:\users\这里是小邓\appdata\local\programs\python\python310\lib\site-packages\PySide6\plugins")

if __name__ == "__main__":
    logger.warning("请使用 main.py 启动程序")
    # 从 main.py 启动主类
    import main, os
    app = main.Main()
    logger.info("程序执行完毕，正在退出 ...")
    os._exit(0)

