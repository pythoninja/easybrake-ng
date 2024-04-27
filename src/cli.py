from pathlib import Path
from typing import Annotated

from cyclopts import App, Parameter

from logger import init_logger
from src.run import easybrake_runner
from src import __version__, __app_name__

app = App(version=f"{__app_name__} v{__version__}", version_flags=["--version"], help_flags=["--help"])


@app.command()
def process(input_dir: Path, output_dir: Path, preset_location: Annotated[str, Parameter(name="--preset-path")]):
    """
    Process the path and generate easybrake commands
    """

    easybrake_runner(input_dir, output_dir, preset_location)


if __name__ == "__main__":
    init_logger()
    app()
