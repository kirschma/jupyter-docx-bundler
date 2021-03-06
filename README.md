# Jupyter docx bundler extension

[![PyPi Version](https://img.shields.io/pypi/v/jupyter_docx_bundler.svg)](https://pypi.org/project/jupyter-docx-bundler/)
[![Conda Version](https://img.shields.io/conda/vn/mrossi/jupyter_docx_bundler.svg)](https://anaconda.org/mrossi/jupyter_docx_bundler)
[![Build Status](https://dev.azure.com/m-rossi-github/jupyter-docx-bundler/_apis/build/status/m-rossi.jupyter-docx-bundler?branchName=master)](https://dev.azure.com/m-rossi-github/jupyter-docx-bundler/_build/latest?definitionId=1&branchName=master)
[![Coverage](https://img.shields.io/azure-devops/coverage/m-rossi-github/jupyter-docx-bundler/1.svg)](https://img.shields.io/azure-devops/coverage/m-rossi-github/jupyter-docx-bundler/1.svg)

Jupyter bundler extension to export notebook as a docx file

## Install

### Installing with pip

Make sure you have [Pandoc](https://pandoc.org) installed.

```
pip install jupyter_docx_bundler
jupyter bundlerextension enable --py jupyter_docx_bundler --sys-prefix
```

### Installing with conda

```
conda install -c mrossi jupyter_docx_bundler
```

## Usage

### Adding Metadata

The bundle extension uses metadata of the notebook, if you you provide it.

* You can add a title by adding `"title": "Notebook title"`
* You can add authors by adding `"authors": [{"name": "author1"}, {"name": "author2"}]`

The notebook metadata can be edited under _Edit_ -> _Edit Notebook Metadata_.

### Hiding inputs or complete code cells

You can hide individual code cells or just their inputs by defining cell tags:

* `nbconvert-remove-cell`: Remove the entire cell
* `nbconvert-remove-input`: Remove the input code of the cell

_(Currently there are no default values configured for these tags, the ones listed above are defined in my code and not in [nbconvert](https://github.com/jupyter/nbconvert). This may will change in the future.)_

Cell tags can be shown by activating the cell toolbar under _View_ -> _Cell Toolbar_ -> _Tags_.

### Direct call from console (nbconvert)

To use the bundler direct from console the nbconvert utility can be used with target format docx:

* `nbconvert --execute --to=docx <source notebook>.ipynb --output <target document>.docx`

The `--execute` option should be used to ensure that the notebook is run before generation.

## Development

### Testing

The package is tested with [pytest](https://docs.pytest.org/en/latest/). Clone the repository and install the requirements for example with conda:
```
conda install --file requirements.txt --file requirements_test.txt
```
Test the package with
```
pytest .
```

### Building

To build the package with [conda-build](https://github.com/conda/conda-build) you need to call
```
conda-build conda.recipe
```
