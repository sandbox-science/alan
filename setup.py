from setuptools import setup, find_packages

setup(
    name='Alan',
    version='1.0.0',
    author='Sandbox Science',
    description='The Sandbox Science Matrix community Bot',
    url="https://github.com/sandbox-science/alan",
    license="GNU General Public License v3.0",
    python_requires='>=3.10.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'matrix-py @ git+https://github.com/Code-Society-Lab/matrixpy.git@main',
        'PyYAML>=6.0',
        'timezonefinder>=6.5',
        'pytz>=2025.2',
        'requests>=2.32'
    ],
    scripts=['bin/alan'],
)
