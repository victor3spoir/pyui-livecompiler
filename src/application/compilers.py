import subprocess
import sys
from pathlib import Path

import watchdog
import watchdog.events
from watchdog.events import FileSystemEventHandler, FileSystemEvent
from watchdog.observers import Observer


class UiFileHandler(FileSystemEventHandler):
    def __init__(self, src_folder: str):
        # self.ui_directory = ui_directory
        # self.output_directory = output_directory
        self.src_folder = Path(src_folder).resolve()

    def on_modified(self, event: FileSystemEvent):
        # Only process .ui files
        assert isinstance(event.src_path, str)
        # if event.src_path.endswith(".ui"):
        if Path(event.src_path).resolve().suffix.lower() == ".ui":
            print(f"Detected change in {event.src_path}. Compiling...")
            self.compile_ui(Path(event.src_path).resolve())

    def on_created(self, event: FileSystemEvent):
        # Only process newly created .ui files
        assert isinstance(event.src_path, str)
        if Path(event.src_path).resolve().suffix.lower() == ".ui":
            print(f"New file detected: {event.src_path}. Compiling...")
            self.compile_ui(Path(event.src_path).resolve())

    def compile_ui(self, ui_file_path: Path):
        # Extract the file name without extension
        file_folder = Path(ui_file_path).parent
        output_file = file_folder.joinpath(f"{ui_file_path.stem}_ui").with_suffix(".py")
        output_file.touch(exist_ok=True)
        # ui_file_name = os.path.basename(ui_file_path)
        # py_file_name = os.path.splitext(ui_file_name)[0] + "_ui.py"

        # Generate the full path for the output Python file
        # py_file_path = os.path.join(self.output_directory, py_file_name)

        # Run pyuic6 to generate Python code from the .ui file
        subprocess.run(["pyuic6", ui_file_path, "-o", output_file.as_posix()])
        # print(f"Compiled {ui_file_path} to {py_file_path}")


def main(src_directory: str):
    event_handler = UiFileHandler(src_directory)
    observer = Observer()
    observer.schedule(event_handler, src_directory, recursive=True)
    print(f"Watching for changes in {src_directory}...")
    observer.start()

    try:
        while True:
            pass  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder = Path(sys.argv[1]).resolve()
        main(folder.as_posix())
        pass
