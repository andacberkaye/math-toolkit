from setuptools import setup, find_packages

setup(
    name="math-toolkit-tr",
    version="0.1.0",
    author="Andac Berkaye",
    author_email="andacberkayekren@example.com",
    description="A custom-built math library offering a variety of basic to intermediate level mathematical functions.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/andacberkaye/math-toolkit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)
