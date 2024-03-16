#!/usr/bin/env just --justfile

# Variables
project_dir := "src"
work_branch := "master"

# Commands
dev:
    poetry install --no-root --with dev

enable-sign:
    git config --local commit.gpgsign true1

switch branch:
    @echo 'Fetching and switching to {{branch}}'
    git fetch origin && git switch '{{branch}}'

master-pull:
    git switch {{work_branch}}
    git pull

clear-env:
    rm -rf {{justfile_directory()}}/.venv

check:
    poetry run ruff check {{justfile_directory()}}/{{project_dir}}
    poetry run ruff format {{justfile_directory()}}/{{project_dir}}
