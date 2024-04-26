from pathlib import Path

from cyclopts import App

from log import configure_logger
from src.run import easybrake_runner
from src import __version__, __app_name__

app = App(version=f"{__app_name__} v{__version__}", version_flags=["--version"], help_flags=["--help"])


@app.command()
def process(input_dir: Path, output_dir: Path, preset_path: Path):
    """
    Process the path and generate easybrake commands
    """

    easybrake_runner(input_dir, output_dir, preset_path)


if __name__ == "__main__":
    configure_logger()
    app()
