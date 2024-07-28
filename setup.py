from setuptools import setup, find_packages

setup(
    name="pipsetup",
    version="0.1.0",
    packages=find_packages(include=['pipsetup', 'pipsetup.*']),
    include_package_data=True,
    package_data={
        'pipsetup': ['templates/*.cfg', 'templates/*.md', 'templates/*.txt', 'templates/*.in'],  # Especifica los archivos en la carpeta templates
    },
    entry_points={
        'console_scripts': [
            'pipsetup=pipsetup.generator:main',
        ],
    },
    install_requires=[],
    author="Leonardo Daniel Gonzalo Laura",
    author_email="glleonardodaniel@gmail.com",
    description="A tool to generate Python project structures",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/leonardogonzalolaura/workspace_setup_pip",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
