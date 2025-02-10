from setuptools import setup, find_packages

setup(
    name="pokeDex",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",  # PokeAPI 사용 시 필요
        "pydantic",  # DataSerializer 사용 시 필요
    ],
)
