# Demo Video


# Python_Template

Welcome to my project! This repository contains all the code and resources related to my awesome project.

## Project Structure
- Jupyter Notebook with:
  - Cells that perform descriptive statistics using Polars or Panda.
  - Tested by using nbval plugin for pytest
- Python Script performing the same descriptive statistics using Polars or Panda
  - lib.py file that shares the common code between the script and notebook
- Makefile with the following:
  - Run all tests (must test notebook and script and lib)
  - Formats code with Python black
  - Lints code with Ruff
- Installs code via:  pip install -r requirements.txt
- test_script.py to test script
- test_lib.py to test library
- Pinned requirements.txt
- GitHub Actions performs all four Makefile commands with badges for each one in the README.md

---

- Jupyter Notebook
- Python Script
- lib.py file: The lib.py file correctly shares the common code between the script and notebook.
- Makefile
- Test files
  - Testing with nbval plugin for pytest
  - The test_script.py and test_lib.py files accurately and efficiently test the Python script and library.

## MakeFile

The `MakeFile` in this repository is a configuration file used with the `make` command. It defines a set of rules and instructions for building and managing the project. It can be used to automate common tasks such as compiling code, running tests, and more. Be sure to consult the MakeFile for specific commands and targets available for this project.

Running all tests (notebook, script, lib)
Formatting code with Python black
Linting code with Ruff


## .devcontainer

The `.devcontainer` directory contains configuration files for setting up a development container environment. This is particularly useful for ensuring that your project can be developed consistently across different platforms and development environments. It may include configuration for Docker containers, development extensions, and other development environment settings. Consult the files in this directory for more details on the development environment setup.

## requirements.txt

The `requirements.txt` file lists all the dependencies and packages required to run this project. You can use this file with package management tools like `pip` (for Python) or other package managers to install the necessary libraries and dependencies. It's a good practice to keep this file up-to-date as your project evolves, making it easier for others to set up and run your project with the correct dependencies.

## cicd.yml
The cicd.yml file is a configuration file for Continuous Integration/Continuous Deployment (CI/CD) pipelines. It defines the steps and actions that need to be taken when code changes are pushed to the repository. CI/CD pipelines automate the build, test, and deployment processes, ensuring code quality and reliability.

## License

MIT

