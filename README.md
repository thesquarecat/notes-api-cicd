# Notes API

A small FastAPI notes service, built to demonstrate a complete CI/CD pipeline using GitHub Actions and containerized delivery.

![CI/CD](https://github.com/thesquarecat/notes-api-cicd/actions/workflows/pipeline.yml/badge.svg)

## Pipeline

Every push to `main` runs:

1. **Test** lint (ruff) + pytest
2. **Build** container image built and pushed to ghcr.io
3. **Verify** published image pulled back and smoke-tested (health, create, list)

## Run locally

```bash
podman build -t notes-api .
podman run -p 8000:8000 notes-api
```

Then open http://localhost:8000/docs
