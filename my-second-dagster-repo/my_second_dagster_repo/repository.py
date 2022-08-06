from dagster import load_assets_from_package_module, repository

from my_second_dagster_repo import assets


@repository
def my_second_dagster_repo():
    return [load_assets_from_package_module(assets)]
