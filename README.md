# Static Site Generator

The Static Site Generator takes one or more markdown files and converts them into html files which can then be statically displayed on the web. The project can take in a folder of nested markdown files and more folders and traverses through them, creating all necessary html files. It can handle headings, links, images, code blocks, block quotes, and more.

## Table of Contents

- [Features](#features)
- [Setup and Usage](#setup)

## Features
- **Markdown to HTML** - Converts markdown (.md) files into html files
- **Recursive File Handler** - Recursively creates and copies over static files and generates html files.

## Setup
To run the Static Site Generator on your own machine:

- Install python 3.6+
- Clone Repository
- If needed, give permissions to run scripts
- Run test script ```python3 ./test.sh``` to make sure everything is working correctly
- Run main script ```python3 ./main.sh```