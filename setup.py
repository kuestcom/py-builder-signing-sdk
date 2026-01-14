import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kuest-py-builder-signing-sdk",
    version="0.0.1",
    author="Kuest Engineering",
    author_email="engineering@kuest.com",
    maintainer="Kuest Engineering",
    maintainer_email="engineering@kuest.com",
    description="Python builder signing sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kuestcom/py-builder-signing-sdk",
    install_requires=[
        "python-dotenv",
        "requests",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/kuestcom/py-builder-signing-sdk/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.9.10",
)
