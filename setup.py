from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='d3wordcloud',
    version='0.0.1',
    description='A simple Jupyter (Lab/Notebook) port of Jason Davies d3 JS wordcloud generator https://www.jasondavies.com/wordcloud/',
    py_modules=["d3wordcloud"],
    package_dir={'': 'src'},
    extras_require={
    "dev": [
        "ipython",
        "check-manifest",
        "twine"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dominik Weckmüller",
    author_email="dominik@geo.rocks",
    url="https://github.com/do-me/d3wordcloud"
)