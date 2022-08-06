from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="my_second_dagster_repo",
        packages=find_packages(exclude=["my_second_dagster_repo_tests"]),
        install_requires=[
            "dagster",
            "dagit",
            "pytest",
        ],
    )
