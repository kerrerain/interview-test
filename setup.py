from setuptools import setup, find_packages

setup(
    name="onepoint",
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[],
    extras_require={
        "dev": [
            "pytest",
            "pylint",
            "autopep8",
        ]
    }
)
