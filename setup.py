from setuptools import setup, find_packages

setup(
    name="ArcGISPyGnu",
    version="0.1.0",
    description="A Python library for interacting with ArcGIS REST APIs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Johan Louwers",
    author_email="LouwersJ@gmail.com",
    url="https://github.com/yourusername/ArcGISPyGnu",
    license="GPL-3.0-or-later",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
)
