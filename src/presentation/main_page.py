# coding:utf-8
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QFileDialog
from presentation.templates.main_page_ui import Ui_MainPage
from presentation.templates.main_vm import MainViewmodel
from PyQt6.QtCore import pyqtSlot


class MainPage(QWidget, Ui_MainPage):
    def __init__(
        self, vm: MainViewmodel = MainViewmodel(), parent: QWidget | None = None
    ):
        super().__init__(parent)
        self.setupUi(self)  # type:ignore
        self.vm = vm

        self.initialize_bindings()
        return

    def initialize_bindings(self) -> None:
        self.button_watch.clicked.connect(self.vm.command_watch)
        self.button_stop.clicked.connect(self.vm.command_stop)
        self.button_select.clicked.connect(self.open_select_folder_dialog)
        return None

    @pyqtSlot()
    def open_select_folder_dialog(self) -> None:
        folder_name = QFileDialog.getExistingDirectory(
            self, "Choose folder to watch", ""
        )
        if not folder_name:
            return None
        folder = Path(folder_name).resolve()
        if not folder.exists():
            return None
        self.vm.update_src_path(folder.as_posix())
        return None
