from pathlib import Path

from src.dtos.movie import Movie

type Directories = list[Path]
type Commands = list[str]
type CommandsAndDirectories = tuple[Commands, Directories]
type Movies = list[Movie]
type ShowSeasonEpisodeOrNone = tuple[str, str] | tuple[None, None]
