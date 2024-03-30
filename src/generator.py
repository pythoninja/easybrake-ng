from pathlib import Path

from src.dtos.movie import Movie
from src.dtos.preset import Preset


class CommandGenerator:
    def __init__(self, preset: Preset, movies: list[Movie], output_dir: Path) -> None:
        self.preset = preset
        self.output_dir = output_dir
        self.movies = movies
        self.additional_params = ["--all-audio"]

    def get(self) -> list[str]:
        commands: list[str] = []

        for movie in self.movies:
            title = movie.title
            year = movie.year
            final_quality = movie.final_quality
            output_file = f"{self.output_dir}/{title} ({year}) [imdbid-] - {final_quality}.mp4"

            template = (
                "# Convert {filename}\n"
                "handbrakecli --preset-import-file '{preset_path}'"
                " --preset '{preset_name}'"
                " --input '{input_file}'"
                " --output '{output_file}'"
                " {params}"
            )
            commands.append(
                template.format(
                    preset_path=self.preset.path,
                    preset_name=self.preset.name,
                    input_file=movie.full_path,
                    output_file=output_file,
                    filename=movie.filename,
                    params=" ".join(self.additional_params),
                )
            )

        return commands
