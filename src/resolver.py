import sys
from pathlib import Path


class DirectoryResolver:
    def __init__(self, target: str):
        self.target: str = target
        self.resolved_path: Path = Path(self.target).resolve()

    def directory_exists(self) -> bool:
        try:
            return self.resolved_path.exists()
        except OSError as e:
            print(f"Failed to check directory: {self.resolved_path}, reason: {e.strerror}")
            sys.exit(1)

    def create_target_dir(self) -> Path:
        if not self.directory_exists():
            try:
                self.resolved_path.mkdir(parents=True, exist_ok=True)
            except OSError as e:
                print(f"Failed to create directory: {self.resolved_path}, reason: {e.strerror}")
                sys.exit(1)
            else:
                return self.resolved_path
