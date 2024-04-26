import sys
from pathlib import Path

from loguru import logger

from src.named_type import Directories


class DirectoryResolver:
    def __directory_exists(self, directory: Path) -> bool:
        try:
            return directory.exists()
        except OSError as e:
            logger.error("Failed to check directory: {}, reason: {}", directory, e.strerror)
            sys.exit(1)

    def __create_dir(self, directory: Path) -> None:
        resolved_path = self.resolve(directory)

        if not self.__directory_exists(resolved_path):
            logger.info("Creating directory: {}", resolved_path)
            try:
                resolved_path.mkdir(parents=True, exist_ok=True)
            except OSError as e:
                logger.error("Failed to create directory: {}, reason: {}", resolved_path, e.strerror)
                sys.exit(1)

    def create_dirs(self, directories: Directories):
        for directory in directories:
            self.__create_dir(directory)

    def resolve(self, path: Path):
        return path.resolve()
