# Contributing to PythonPad
PythonPad is an interactive Python notebook for data exploration and prototyping, built with Python, FastAPI, Pandas, and DuckDB. We welcome contributions from the community to help improve and expand the project. In this document, we outline the steps to contribute to PythonPad.

## Setup
To start contributing to PythonPad, follow these steps:

1. **Fork the repository**: Create a fork of the PythonPad repository to your own GitHub account.
2. **Clone the repository**: Clone the forked repository to your local machine using `git clone https://github.com/your-username/PythonPad.git`.
3. **Create a virtual environment**: Create a virtual environment using `python -m venv env` (or your preferred method).
4. **Install dependencies**: Install the required dependencies using `pip install -r requirements.txt`.
5. **Start the application**: Start the PythonPad application using `uvicorn main:app --reload`.

## Branch Naming Convention
We use a branch naming convention to organize our codebase. The following prefixes are used:

* **feat/**: New features or functionality.
* **fix/**: Bug fixes or corrections.
* **docs/**: Documentation updates or improvements.
* **refactor/**: Code refactoring or optimization.
* **test/**: Test additions or improvements.
* **chore/**: Miscellaneous changes or updates.

## Conventional Commits
We follow the Conventional Commits specification to ensure consistent commit messages. The commit message should be in the following format:

type(scope): brief description

body

Where:

* **type**: One of `feat`, `fix`, `docs`, `refactor`, `test`, or `chore`.
* **scope**: Optional scope of the commit (e.g., `api`, `ui`, `database`).
* **brief description**: Brief summary of the changes.
* **body**: Optional detailed description of the changes.

Example:
feat(api): Add support for Pandas data structures

Added support for Pandas data structures in the API, including DataFrames and Series.

## Pull Request Checklist
Before submitting a pull request, ensure that you have:

* [ ] Run `black` and `isort` to format the code.
* [ ] Run `flake8` to check for code quality and style issues.
* [ ] Run the tests using `pytest` to ensure the changes do not break existing functionality.
* [ ] Updated the documentation (if applicable).
* [ ] Included a clear and concise description of the changes in the commit message and pull request body.

## Code of Conduct
We follow the standard GitHub code of conduct. Be respectful, considerate, and professional in your interactions with the community.

## License
PythonPad is licensed under the [MIT License](https://opensource.org/licenses/MIT). By contributing to the project, you agree to release your contributions under the same license.

Thank you for considering contributing to PythonPad! Your contributions will help make the project better for everyone.