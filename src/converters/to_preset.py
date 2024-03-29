import json
import sys
from pathlib import Path
from typing import Any

from src.dtos.preset import Preset


class FilePresetConverter:
    def __init__(self, preset_path: Path):
        self.preset_path = preset_path
        self.preset_json: dict[str, Any] | None = self.parse_json()

    def parse_json(self) -> dict[str, Any]:
        try:
            with self.preset_path.open(encoding="UTF-8") as preset_file:
                return json.load(preset_file)
        except FileNotFoundError:
            print(f"File {self.preset_path} does not exist.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"File {self.preset_path} is not a valid JSON.")
            sys.exit(1)

    def get(self) -> Preset:
        return Preset(
            name=self.__get_name(),
            picture_width=self.__get_picture_width(),
            picture_height=self.__get_picture_height(),
            path=self.preset_path,
            upscale_enabled=self.__get_upscale(),
        )

    def __get_name(self) -> str:
        return self.__get_preset_property("PresetName")

    def __get_picture_width(self) -> int:
        return self.__get_preset_property("PictureWidth")

    def __get_picture_height(self) -> int:
        return self.__get_preset_property("PictureHeight")

    def __get_upscale(self) -> bool:
        return self.__get_preset_property("PictureAllowUpscaling")

    def __get_preset_property(self, property_name: str) -> str | int | bool:
        try:
            return self.preset_json["PresetList"][0][property_name]
        except (KeyError, TypeError):
            print(f"Invalid JSON structure: Missing {property_name} key.")
            sys.exit(1)
