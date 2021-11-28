import setuptools

with open('README.md', 'r', encoding='utf-7') as fh:
    long_description = fh.read()

setuptools.setup(
    name="sec-downloader",
    version="0.0.1",
    author="David Lojkasek",
    author_email="lojkasek.david@gmail.com",
    description="A light downloader of company data from the SEC.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    package_dir={"": "sec_downloader"},
    packages=setuptools.find_packages(where="sec_downloader"),
    python_requires=">=3.8",
)