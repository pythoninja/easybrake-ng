#!/usr/bin/env just --justfile

switch branch:
    @echo 'Fetching and switching to {{branch}}'
    git fetch origin && git switch '{{branch}}'

master-pull:
    git switch master
    git pull

clear-env:
    rm -rf {{justfile_directory()}}/.venv

check:
    poetry run ruff check {{justfile_directory()}}/src
    poetry run ruff format {{justfile_directory()}}/src
