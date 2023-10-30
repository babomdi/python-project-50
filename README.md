### Hexlet tests and linter status:
[![Actions Status](https://github.com/babomdi/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/babomdi/python-project-50/actions)
[![Python CI](https://github.com/babomdi/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/babomdi/python-project-50/actions/workflows/main.yml)
<a href="https://codeclimate.com/github/babomdi/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/d1b52c3276d4b58c24d3/maintainability" /></a>
<a href="https://codeclimate.com/github/babomdi/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/d1b52c3276d4b58c24d3/test_coverage" /></a>

## About the project
Generate difference is a program that determines the difference between two data structures and displays it on screen

# Supported file formats:
- `json`
- `yaml`

## Getting started:
1. Clone the repo
```
git clone https://github.com/babomdi/python-project-50.git
```
2. Navigate to the installed repo
```
cd python-project-50
```
3. Install the package
```
poetry install
```

## `usage`
1. Put the files you want to check in the `tests/fixtures/` folder
2. Run this command:
```
gendiff tests/fixtures/your_file1 tests/fixtures/your_file2
```

## Output formats
To choose format add flag `-f` or `--format`.
Available formats:
- stylish (default)
- plain
- json

# Commands examples
- stylish
```
gendiff tests/fixtures/your_file1 tests/fixtures/your_file2
```
- plain
```
gendiff -f plain tests/fixtures/your_file1 tests/fixtures/your_file2
```
- json
```
gendiff -f json tests/fixtures/your_file1 tests/fixtures/your_file2
```

## Demo
[![asciicast](https://asciinema.org/a/617911.svg)](https://asciinema.org/a/617911)
[![asciicast](https://asciinema.org/a/617912.svg)](https://asciinema.org/a/617912)
[![asciicast](https://asciinema.org/a/617913.svg)](https://asciinema.org/a/617913)
