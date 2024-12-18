# coding:utf-8
import sys
import typing
from PyQt6.QtWidgets import QApplication

from presentation.shell import Shell


class Application(QApplication):
    def __init__(self) -> None:
        super().__init__(sys.argv)
        self.shell = Shell()
        return

    def launch(self) -> typing.NoReturn:
        self.shell.showNormal()
        sys.exit(self.exec())
