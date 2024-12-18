# coding:utf-8

from pathlib import Path

from application.compilers import UiFileHandler
from watchdog.observers import Observer


class MainViewmodel:
    def __init__(self) -> None:
        self.observer = Observer()
        self.event_handler: UiFileHandler
        self.src_path: Path
        self.latest_src_path: Path = Path.home()
        return

    def update_src_path(self, folder_name: str) -> None:
        self.src_path = Path(folder_name).resolve()
        self.latest_src_path = self.src_path
        self.event_handler = UiFileHandler(self.src_path.as_posix())
        self.observer.schedule(self.event_handler, self.src_path.as_posix())
        return None

    def command_watch(self) -> None:
        if self.observer.is_alive():
            return
        self.observer.start()
        return None

    def command_stop(self) -> None:
        self.observer.stop()
        self.observer.join()
        return None
