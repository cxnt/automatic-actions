import setuptools
import subprocess
import os

git_repo_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)
assert "." in git_repo_version

assert os.path.isfile("cf_remote/version.py")
with open("VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{git_repo_version}\n")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="automatic-actions",
    version=git_repo_version,
    author="cxnt",
    author_email="cxnt",
    description="Automatic builds for PYPI and Docker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cxnt/automatic-actions",
    packages=setuptools.find_packages(),
    package_data={"automatic-actions": ["VERSION"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={"console_scripts": ["src = src.main:main"]},
    install_requires=[
        "setuptools>=42",
        "wheel"
    ],
)