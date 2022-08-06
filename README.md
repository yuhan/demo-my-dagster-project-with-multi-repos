Demo: my dagster project with multiple repos
---

## How this project was created

*You can find all the steps in the commit history*

This project is scaffolded with the [`dagster project`](https://docs.dagster.io/getting-started/create-new-project) CLI tool:

- Step 1: Scaffold a brand new project:
  ```
  dagster project scaffold --name my-dagster-project
  ```
- Step 2: Scaffold a new repo in the new project directory:
  ```
  cd my-dagster-project
  dagster project scaffold-repository --name my-second-dagster-repo
  ```
- Step 3: Update workspace.yaml: add my_second_dagster_repo as another python_package

Below are optional steps:
- Note: In most cases, one single Dagster repository should get you pretty far, and we don't recommend over abstract things too early. But a project with multiple Dagster repositories can be useful when you want to keep conflicting Python dependencies separate, or execute your pipelines in different Python environments (e.g. one in py3.6 and the other in py3.10). To do so, each Dagster repository can keep their own package requirements (e.g., setup.py) and deployment specs (e.g., Dockerfile).

The following steps only demonstrate the minimal setup:

- Step 4: Refactor: move top-level first repo to "my-first-dagster-repo" (this cleans up your project structure)
- Step 5: Create a requirements.txt which helps install two repos as two python packages (this helps local development, see below)

For more advanced setup, check out [Workspaces > Loading multiple repositories](https://docs.dagster.io/concepts/repositories-workspaces/workspaces#loading-multiple-repositories).

---

## Local Development

First, install all your Dagster repositories as a Python package. By using the --editable flag, pip will install your repository in ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs) so that as you develop, local code changes will automatically apply.

```bash
pip install -r requirements.txt
```

Then, start the Dagit web server:

```bash
dagit
```

Open http://localhost:3000 with your browser to start develop your Dagster project.

## Deployment

- Open Source: [Deploying Dagster with your infrastructure](https://docs.dagster.io/deployment/open-source)
- [Dagster Cloud](https://docs.dagster.io/dagster-cloud)