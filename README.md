# Dagster Multi-Project

This repository serves as a test ground for various ETL pipeline projects, both done using Dagster, and as prototypes prior to Dagster-ification of said ETL pipeline.

Will also likely test out how code locations work using this project.

List of projects include:
- Prototype: Take CSV / Excel (of the various forms) from Google Drive and turn it into a dataframe. Extract must work on Google Colab and locally. Upload dataframe to some postges table 



General
- Included code quality tools:
    - black: black
    - pylint: linter
    - mypy: typechecker
    - pytest: unit testing framework