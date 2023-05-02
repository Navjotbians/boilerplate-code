from invoke import task


@task
def test(c):
    c.run("pytest")


@task
def lint(c):
    """Run linting"""
    c.run("flake8 .", echo=True)


@task
def format(c):
    """Run formatting"""
    c.run("black .", echo=True)


@task
def build_docker(c, tag):
    c.run(f"docker build -t {tag} .")


@task
def run_docker(c, tag):
    c.run(f"docker run {tag}")


@task
def build_and_run_docker(c, tag):
    build_docker(c, tag)
    run_docker(c, tag)
