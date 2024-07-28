from setuptools import setup, find_packages
import setuptools_scm

setup(
    name="my_new_project",
    use_scm_version=True,
    setup_requires=["setuptools>=42", "setuptools_scm"],
    packages=find_packages(include=['setup', 'folder_library.*']),
    install_requires=['library_externals'],
    test_suite='tests',
    author="John Doe",
    author_email="john.doe@example.com",
    description="A simple example of a Python library",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/John Doe/my_new_project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)