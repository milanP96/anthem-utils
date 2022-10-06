import pathlib
from setuptools import setup, find_packages

from anthem import __version__

HERE = pathlib.Path().cwd()
DESCRIPTION = HERE.joinpath("README.md").read_text()
VERSION = __version__

setup(
    name="anthem",
    version=VERSION,
    description="Generate directory tree diagrams for Real Python articles",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/anthem-utils",
    author="Real Python",
    author_email="info@realpython.com",
    maintainer="Leodanis Pozo Ramos",
    maintainer_email="leodanis@realpython.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['boto3'],
    entry_points={
        "console_scripts": [
            "anthem=anthem.__main__:main",
        ]
    },
)
