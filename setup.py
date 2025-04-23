from setuptools import setup, find_packages

setup(
    name='pip_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
       'setuptools' # Aquí tus dependencias si las tienes''
    ],
    entry_points={
        'console_scripts': [
            'generator = pip_project.main:main',  # Esto asocia el comando 'mi_comando' a la función `main` de `main.py`
        ],
    }
)