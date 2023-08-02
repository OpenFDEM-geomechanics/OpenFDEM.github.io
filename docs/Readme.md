# How to Use This File Structure to Make Documentation

Documentation is available in `html`, `pdf` and `latex` formats for OpenFDEM Solver.

To generate documentation, three main tools are used:
- Doxygen
- Sphinx
- Breathe API

Documentation is created for `.h ` files under the `src` main folder.

Folder structure:
- **Doxygen folders** with build XMLs are found in the following subfolders:
    -   [docs_common](docs_common) : linked to src/common `.h` files
    -   [docs_geometry](docs_geometry) : linked to src/geometry `.h` files
    -   [docs_solid](docs_solid) : linked to src/solid `.h` files
    -   [docs_solve](docs_solve) : linked to src/solid `.h` files
    -   [docs_test](docs_test) : linked to src/test `.h` files

- **Documentation** is built out of the following folders:
    -   [sphinx_run](sphinx_run/_build/html/)

# Where to Find Config Files
All build settings for documentation are controlled in [conf.py](sphinx_run/conf.py). The start page and display menu are found under the file [index.rst](sphinx_run/index.rst).

# Running Sphinx Engine Builder

1. Update comments to `.h` files, using \** ... *\ formatting.
2. Navigate to the Doxygen documentation folder and run `doxygen` in terminal.

## HTML Build
To rerun the HTML build (ex. if a docstring is updated), navigate to the [sphinx_run](sphinx_run) folder and run:
 `make html` 
 in terminal.

To view the `HTML` files locally, navigate to  `_build` -> `html` -> [index.html](sphinx_run/_build/html/index.html). From there the sub-modules can be accessed in your browser.
To format the HTML files, refer to `index.rst` and `conf.py`.

## Latex and PDF Build
To rerun the Latex and PDF build (ex. if a docstring is updated), run
 `make latexpdf` 
 in terminal.

To view the PDF file, navigate to  `_build` -> `latex` -> `openfdem.pdf`.
