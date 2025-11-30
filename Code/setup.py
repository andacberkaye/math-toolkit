from setuptools import setup

setup(
    name="math_toolkit",
    version="1.0.0",
    author="Andac Berkaye",
    author_email="your_email@example.com",
    description="A custom-built math library offering a variety of basic to intermediate level mathematical functions written from scratch without using external modules.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/andacberkaye/math-toolkit",
    py_modules=["mathOperations"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)
