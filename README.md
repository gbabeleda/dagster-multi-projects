# Dagster Multi-Project

This repository serves as a test ground for various ETL pipeline projects, both done using Dagster, and as prototypes prior to Dagster-ification of said ETL pipeline.

Will also likely test out how code locations work using this project.

List of projects include:
- Prototype: Take CSV / Excel (of the various forms) from Google Drive and turn it into a dataframe. Extract must work on Google Colab and locally. Upload dataframe to some postges table 
- Dagster-DBT project 



# Infrastructure Setup



## Terraform
- Install terrform following the steps [here](https://developer.hashicorp.com/terraform/install)
- Add to path

```powershell
# Windows
$currentPath = [Environment]::GetEnvironmentVariable('Path', 'User')
[Environment]::SetEnvironmentVariable('Path', "$currentPath;C:\terraform", 'User')
```

```bash
# Mac
# Start with installing homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add brew to path
echo >> /Users/user/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/user/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

# Install terraform
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```
- Test with `terraform --info`
- Add a terraform/ at root of repository


# Development Setup
## Dependency Managment 
### Virtual Environment: venv
```powershell
# Windows
python -m venv venv
.\venv\Scripts\activate
```

```bash
# Unix
python -m venv venv
source venv/bin/activate
```

For windows specifically, we likely need to also run the following as admin

```powershell
set-executionpolicy RemoteSigned
```

### Pyproject.toml


### Others
Other options include
- setuptools
- poetry

## Code Quality / Static Analysis Tools

- black: formatter
- pylint: linter
- mypy: typechecker
- pytest: unit testing framework















# Infrastructure and Development Setup
## Development Setup
### Virtual Environment Setup
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Unix
python -m venv venv
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### Dagster Setup
**Initialize a dagster project**
```bash
dagster project scaffold --name ecommerce-sftp
```

**Key Concepts**
- Each dagster project is its own stand-alone thing with its own
    - Dependencies (defined in pyproject.toml)
    - Assets and Resources
    - Tests
    - Documentation
    - Can have multiple code locations
- Project dependencies are defined in pyproject.toml (preferred) rather than setup.py in newer Dagster versions, in line with modern Python best practices
- Each project has its own README.md with project-specific details

**Project dependencies `pyproject.toml`**



Local Development
```bash
cd ecommerce_sftp
pip install -e ".[dev]"
dagster dev
```