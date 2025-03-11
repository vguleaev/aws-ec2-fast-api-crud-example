### Dev Notes

- Pydantic - validation
- Ruff - linting
- mypy - type checking
- uv - pip replacement
- Docker
- Pytest
- Use orjson instead of the built in json library
- Always use f strings instead of string concatonation or .format or %s formatted strings
- Use pathlib instead of os.path
- Use click instead of argparse or heaven forbid, sys.argv
- Upgrade to python 3.8+

You do not need to create `venv` and `requirements.txt` to isolate and handle dependencies. `uv` package manager will make it for you.

#### Step by step create new project:

**Create project with uv**:

```
mkdir fastapi-todo
cd fastapi-todo
```

```
pip install uv
uv init
```

**How to add dependencies:**

```
uv add "fastapi[all]" pydantic mypy ruff
```

**Hot to add Dev dependency:**

```
uv add pytest --dev
```

#### Run project:

**Install dependencies:**

```
uv sync
```

**Activate virtual environment**

```
source .venv/bin/activate
```

Inside virtual environment, you have access to fastapi cli, use it to run app:

```
fastapi dev app/main.py
```

For production use run (auto reload is disabled)

```
fastapi run app/main.py
```

You can use command `uv run` to run a command inside project environment, e.g. `uv run fastapi run app/main.py`

> Empty `__init__.py` file is needed in `app` dir to indicate a python package.

#### Linting & Formatting:

**Run mypy for static type checking**

```
mypy app
```

**Run Ruff for linting:**

```
ruff check
```

**Run Ruff for formatting:**

```
ruff format
```

**To run all linting together use scripts:**

```
uv run scripts/lint.sh
```

### Links

Official example of Fastapi CRUD in Docker with uv [here.](https://github.com/fastapi/full-stack-fastapi-template/tree/master)

- Fast API docs: https://fastapi.tiangolo.com/tutorial/first-steps/
- Pydantic docs: https://docs.pydantic.dev/latest/
- Uv docs: https://docs.astral.sh/uv/
- Ruff docs: https://docs.astral.sh/ruff/

### Run Terraform

To init project run:

```
terraform init
```

Add variables to `terraform.tfvars` file and create `variables.tf` file with variables.

Directory `terraform` contains terraform state (should not be commited to git).

To run plan and apply (inside terraform directory):

```
terraform plan
terraform apply
```
