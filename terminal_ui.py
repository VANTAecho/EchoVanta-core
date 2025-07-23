"""Terminal user interface for browsing and opening text files."""

import curses
import os
from typing import List

class FileManager:
    """Helper class for listing and reading text files in a directory."""

    def __init__(self, directory: str = ".") -> None:
        self.directory = directory

    def list_files(self) -> List[str]:
        """Return a list of regular file names in the directory."""
        return [f for f in os.listdir(self.directory)
                if os.path.isfile(os.path.join(self.directory, f))]

    def read_file(self, filename: str) -> List[str]:
        """Return the lines of the specified file."""
        path = os.path.join(self.directory, filename)
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()


class TerminalUI:
    """Simple curses-based terminal interface to navigate and open files."""

    def __init__(self, directory: str = ".") -> None:
        self.manager = FileManager(directory)
        self.files = self.manager.list_files()
        self.position = 0

    def launch(self) -> None:
        """Launch the curses interface."""
        curses.wrapper(self._main)

    def _main(self, stdscr) -> None:
        curses.curs_set(0)
        while True:
            stdscr.clear()
            for idx, name in enumerate(self.files):
                attr = curses.A_REVERSE if idx == self.position else curses.A_NORMAL
                stdscr.addstr(idx, 0, name, attr)
            stdscr.refresh()
            key = stdscr.getch()
            if key == curses.KEY_UP and self.position > 0:
                self.position -= 1
            elif key == curses.KEY_DOWN and self.position < len(self.files) - 1:
                self.position += 1
            elif key in (curses.KEY_ENTER, ord("\n")):
                self._open_file(stdscr, self.files[self.position])
            elif key in (ord("q"), ord("Q")):
                break

    def _open_file(self, stdscr, filename: str) -> None:
        lines = self.manager.read_file(filename)
        stdscr.clear()
        height, _ = stdscr.getmaxyx()
        for idx, line in enumerate(lines[: height - 1]):
            stdscr.addstr(idx, 0, line.rstrip())
        stdscr.addstr(height - 1, 0, "Press any key to return...")
        stdscr.refresh()
        stdscr.getch()


def launch_ui() -> None:
    """Launch the terminal UI for the current directory."""
    ui = TerminalUI()
    ui.launch()


if __name__ == "__main__":
    launch_ui()
