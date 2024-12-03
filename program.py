import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

# 定义主窗口类
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("PySide Example")
        self.resize(1000, 1200)

        # 创建一个标签
        self.label = QLabel("请输入文字：", self)

        # 创建一个文本输入框
        self.text_input = QLineEdit(self)

        # 创建一个按钮
        self.button = QPushButton("显示文本", self)
        self.button.clicked.connect(self.show_text)  # 连接按钮点击事件到 show_text 函数

        # 创建垂直布局，并添加组件
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.button)
        self.setLayout(layout)

    # 定义点击按钮后的行为
    def show_text(self):
        input_text = self.text_input.text()  # 获取文本框内容
        self.label.setText(f"你输入的内容是：{input_text}")  # 将内容显示在标签上

# 主程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建窗口实例并显示
    window = MyWindow()
    window.show()

    # 运行应用程序事件循环
    sys.exit(app.exec())
