from pathlib import Path


class MovieFinder:
    def __init__(self, input_dir: Path):
        self.input_dir = input_dir
        self.extensions = [".mp4", ".mkv", ".avi", ".mov", ".m4v"]

    def find_movies(self) -> list[Path]:
        return [file for file in self.input_dir.rglob("*") if file.is_file() and file.suffix.lower() in self.extensions]
