# coding:utf-8
import sys
import typing
from pathlib import Path

from presentation.shell import Shell
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication


class Application(QApplication):
    def __init__(self) -> None:
        super().__init__(sys.argv)
        self.setApplicationName("PYUI-LiveCompiler")
        self.setApplicationDisplayName("PYUI-LiveCompiler")
        self.setWindowIcon(
            # FIXME: this must set correctly using resource manager/resource.qrc
            QIcon(
                Path(__file__)
                .parent.joinpath("resources/images/logo.jpg")
                .resolve()
                .as_posix()
            )
        )
        self.shell = Shell()
        return

    def launch(self) -> typing.NoReturn:
        self.shell.showNormal()
        sys.exit(self.exec())
