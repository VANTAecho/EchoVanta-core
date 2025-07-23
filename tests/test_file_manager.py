import os
from terminal_ui import FileManager


def test_read_file(tmp_path):
    """FileManager should read contents of a file."""
    file_path = tmp_path / "sample.txt"
    file_path.write_text("hello")
    mgr = FileManager(str(tmp_path))
    assert mgr.read_file("sample.txt") == ["hello"]

