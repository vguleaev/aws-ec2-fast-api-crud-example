FROM python:3.12-slim-bookworm

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.5.14 /uv /uvx /bin/

# Copy the project into the image
ADD . /app

WORKDIR /app

# Install dependencies
RUN uv sync --frozen

# Activate the environment by placing the executables in the path
ENV PATH="/app/.venv/bin:$PATH"

# Run the application
CMD ["fastapi", "run", "app/main.py"]