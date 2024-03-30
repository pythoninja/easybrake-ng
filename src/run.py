import sys
from pathlib import Path

from src.resolver import DirectoryResolver
from src.converters.to_movie import FileMovieConverter
from src.converters.to_preset import FilePresetConverter
from src.dtos.movie import Movie
from src.finder import MovieFinder
from src.generator import CommandGenerator


def easybrake_runner(input_dir: Path, output_dir: Path, preset_path: Path) -> None:
    resolver = DirectoryResolver(target=output_dir)
    target_dir = resolver.create_target_dir()

    finder = MovieFinder(input_dir=input_dir)
    movie_files: list[Path] = finder.find_movies()

    if not movie_files:
        print(f"No video files found at selected directory: {input_dir}")
        sys.exit(1)

    preset_converter = FilePresetConverter(preset_path=preset_path)
    preset = preset_converter.get()

    movie_converter = FileMovieConverter(preset=preset, candidates=movie_files)
    movies: list[Movie] = movie_converter.get()

    command_generator = CommandGenerator(preset=preset, movies=movies, output_dir=target_dir)
    commands: list[str] = command_generator.get()

    print("# Generated hanbrake commands, just paste it to the bash, check and run\n")
    print(*commands, sep="\n\n")


if __name__ == "__main__":
    _preset_filename = "preset-example.json"
    _base_path = Path(__file__).resolve().parent.parent
    _preset_path: Path = _base_path / "example" / "presets" / _preset_filename
    _input_dir = _base_path / "example" / "videos" / "process"
    _output_dir = _base_path / "example" / "videos" / "done"

    easybrake_runner(_input_dir, _output_dir, _preset_path)
