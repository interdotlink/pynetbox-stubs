import os
from typing import Dict, List

from setuptools import setup


def find_stubs(package: str) -> Dict[str, List]:
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, "", 1)
            stubs.append(path)
    return {package: stubs}


setup(
    name="pynetbox-stubs",
    maintainer="Sebastian Wagner",
    maintainer_email="sebastian@inter.link",
    description="PEP 561 type stubs for pynetbox",
    url="",
    license="Apache License 2.0",
    version="0.0.3",
    packages=["pynetbox-stubs"],
    # PEP 561 requires these
    install_requires=[
        "pynetbox",
    ],
    package_data=find_stubs("pynetbox-stubs"),
    zip_safe=False,
)
