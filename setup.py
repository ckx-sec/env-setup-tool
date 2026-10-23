from setuptools import setup, find_packages

setup(
    name="env-setup-tool",
    version="1.0.1",
    packages=find_packages(),
    package_data={"env_setup": ["data/*"]},
    include_package_data=True,
    entry_points={"console_scripts": ["env-check=env_setup.cli:main"]},
    python_requires=">=3.6",
)
