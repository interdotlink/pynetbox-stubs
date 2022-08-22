from setuptools import setup
import os


def find_stubs(package):
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
    license="",
    version="0.0.1",
    packages=["pynetbox-stubs"],
    # PEP 561 requires these
    install_requires=[
        "pynetbox",
    ],
    package_data=find_stubs("pynetbox-stubs"),
    zip_safe=False,
)