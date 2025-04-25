from setuptools import setup, find_packages

setup(
    name='pip-project',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'generator = comando.main:main',  # Esto asocia el comando 'mi_comando' a la función `main` de `main.py`
        ],
    },
)