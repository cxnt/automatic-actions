import os
import setuptools
import subprocess

git_repo_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)
assert "." in git_repo_version

assert os.path.isfile("src/version.py")
with open("VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{git_repo_version}\n")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test-package-cxnt",
    version=git_repo_version,
    author="cxnt",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cxnt/automatic-actions",
    project_urls={
        "Bug Tracker": "https://github.com/cxnt/automatic-actions/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
