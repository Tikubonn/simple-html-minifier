
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as stream:
  long_description = stream.read()

setup(
  name="simple-html-minifier",
  description="the simple HTML minifier that made of standard libraries.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  version="1.0.0",
  license="MIT",
  author="tikubonn",
  author_email="https://twitter.com/tikubonn",
  url="https://github.com/tikubonn/simple-html-minifier",
  packages=find_packages(),
  install_requires=[],
  dependency_links=[],
  entry_points={},
  classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
  ],
  test_suite="test"
)
