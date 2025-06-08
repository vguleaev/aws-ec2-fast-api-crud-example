# FastAPI Python CRUD on AWS EC2 + RDS Postgres

This is an example of basic FastAPI app deployed on AWS with Terraform files managing infrastructure.

**Tech Stack:**

- Python
- FastAPI
- Docker
- Terraform
- Pydantic
- sqlmodel
- Ruff
- mypy
- uv
- pytest

**AWS:**

- EC2
- RDS

### Run project

Install dependencies:

```
uv sync
```

Activate virtual environment:

```
source .venv/bin/activate
```

Inside virtual environment, you have access to fastapi cli, use it to run app:

```
fastapi dev app/main.py
```

For production use run (auto reload is disabled):

```
fastapi run app/main.py
```

To run linting and formatting:

```
uv run scripts/lint.sh
```

To run tests:

```
uv run scripts/test.sh
```

### Docker

Build docker image:

```
docker build -t aws-ec2-fast-api-crud-example .
```

Run docker image:

```
docker run -p 8000:8000 aws-ec2-fast-api-crud-example
```
