#!/bin/bash

echo "Removing all files in the dist/ folder..."
rm -rf dist/*

echo "Activating Poetry shell..."
poetry shell

echo "Building the package..."
poetry run python -m build

echo "Uploading the package to PyPI..."
poetry run twine upload dist/*

echo "Done!"
