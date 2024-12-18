# coding:utf-8

from PyQt6.QtWidgets import QMainWindow

from presentation.main_page import MainPage


class Shell(QMainWindow):
    def __init__(self) -> None:
        super().__init__(None)
        self.setCentralWidget(MainPage())
