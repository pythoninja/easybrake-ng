from dataclasses import dataclass
from pathlib import Path


@dataclass
class Movie:
    title: str
    year: str
    quality: str
    filename: str
    full_path: Path
    final_quality: str
