from pathlib import Path

from src.resolver import DirectoryResolver
from src.converters.to_movie import FileMovieConverter
from src.converters.to_preset import FilePresetConverter
from src.dtos.movie import Movie
from src.finder import MovieFinder
from src.generator import CommandGenerator


def run() -> None:
    preset_filename = "preset-1080p60-rf19-veryslow_draft-01.json"
    base_path = Path(__file__).resolve().parent.parent
    preset_path: Path = base_path / "example" / "presets" / preset_filename
    input_dir = base_path / "example" / "videos" / "process"
    output_dir = str(base_path / "example" / "videos" / "done")

    resolver = DirectoryResolver(target=output_dir)
    target_dir = resolver.create_target_dir()

    preset_converter = FilePresetConverter(preset_path=preset_path)
    preset = preset_converter.get()

    finder = MovieFinder(input_dir=input_dir)
    movie_files: list[Path] = finder.find_movies()

    movie_converter = FileMovieConverter(preset=preset, candidates=movie_files)
    movies: list[Movie] = movie_converter.get()

    command_generator = CommandGenerator(preset=preset, movies=movies, output_dir=target_dir)
    commands: list[str] = command_generator.get()

    for command in commands:
        print(command)


if __name__ == "__main__":
    run()
