#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name="hello_luki",
    version="0.1.0",
    description="Short description of hello_luki",
    long_description="Looong description of hello_luki",
    url="https://example.com/pup/helo_luki",
    author="Luki",
    author_email="luki@example.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="sample setuptools development hello luki",

    packages=find_packages(exclude=["docs", "tests"]),

    # py_modules=["my_module"],
    # install_requires=["peppercorn"],
    # extras_require={"dev": ["check-manifest"], "test": ["coverage"]},
    # package_data={"sample": ["package_data.dat"]},
    # data_files=[("my_data", ["data/data_file"])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        "console_scripts": [
            "hello_luki=hello_luki.hello_cli:main",
        ],
    },
)
