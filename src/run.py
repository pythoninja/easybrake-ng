import sys
from pathlib import Path

from loguru import logger

from src.resolver import DirectoryResolver
from src.converters.to_movie import FileMovieConverter
from src.converters.to_preset import FilePresetConverter
from src.finder import MovieFinder
from src.generator import CommandGenerator
from src.named_type import Directories, Commands, Movies


def easybrake_runner(input_dir: Path, output_dir: Path, preset_path: Path) -> None:
    resolver = DirectoryResolver()
    target_dir = resolver.resolve(output_dir)

    logger.info("Easybrake started")
    logger.info("Preset file: {}", preset_path)
    logger.info("Input directory: {}", input_dir)
    logger.info("Output directory: {}", output_dir)

    finder = MovieFinder(input_dir=input_dir)
    movie_files: list[Path] = finder.find_movies()

    if not movie_files:
        logger.error(f"No video files found at selected directory: {input_dir}")
        sys.exit(1)

    preset_converter = FilePresetConverter(preset_path=preset_path)
    preset = preset_converter.get()
    logger.info("Preset name: {}", preset.name)
    logger.info(
        "Preset parameters: picture_height={}, picture_width={}, upscale_enabled={} ",
        preset.picture_height,
        preset.picture_width,
        preset.upscale_enabled,
    )

    movie_converter = FileMovieConverter(preset=preset, candidates=movie_files)
    movies: Movies = movie_converter.get()

    command_generator = CommandGenerator(preset=preset, movies=movies, output_dir=target_dir)
    commands: Commands
    dirs: Directories
    commands, dirs = command_generator.get()

    resolver.create_dirs(dirs)

    print("\n# Generated hanbrake commands, just paste it to the bash script, check and run\n")
    print(*commands, sep="\n\n")
    print("# Paste the code above this line \n")

    logger.info("Easybrake finished")


if __name__ == "__main__":
    from log import configure_logger

    configure_logger()

    _preset_filename = "preset-example.json"
    _base_path = Path(__file__).resolve().parent.parent
    _preset_path: Path = _base_path / "example" / "presets" / _preset_filename
    _input_dir = _base_path / "example" / "videos" / "process"
    _output_dir = _base_path / "example" / "videos" / "done"

    easybrake_runner(_input_dir, _output_dir, _preset_path)
