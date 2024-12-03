import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QMenuBar, QFileDialog, QMessageBox, QAction
)
from PySide6.QtGui import QIcon

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和图标
        self.setWindowTitle("简易记事本")
        self.setWindowIcon(QIcon("notepad_icon.png"))  # 如果有图标可以用这行代码设置图标

        # 创建文本编辑器
        self.editor = QTextEdit(self)
        self.setCentralWidget(self.editor)  # 设置文本编辑器为主窗口的中心部件

        # 创建菜单栏
        menu_bar = self.menuBar()

        # 添加文件菜单和动作
        file_menu = menu_bar.addMenu("文件")
        
        open_action = QAction("打开", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("保存", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        exit_action = QAction("退出", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def open_file(self):
        # 打开文件对话框，选择文件并读取内容
        file_path, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.editor.setText(content)  # 将文件内容加载到文本编辑器

    def save_file(self):
        # 打开保存文件对话框，获取保存路径并写入内容
        file_path, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                content = self.editor.toPlainText()
                file.write(content)  # 将文本编辑器内容保存到文件

    def closeEvent(self, event):
        # 覆盖关闭事件，弹出消息框确认是否退出
        reply = QMessageBox.question(self, "确认退出", "是否保存更改并退出？",
                                     QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Save)
        if reply == QMessageBox.Save:
            self.save_file()
            event.accept()
        elif reply == QMessageBox.Discard:
            event.accept()
        else:
            event.ignore()

# 主程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    notepad = Notepad()
    notepad.show()
    sys.exit(app.exec())
