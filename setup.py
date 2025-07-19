from setuptools import setup, find_packages

setup(
    name='quotexbot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'telethon',
        'numpy',
        'pandas',
        # agrega tus otras dependencias aquí
    ],
    entry_points={
        'console_scripts': [
            'quotexbot=quotexbot.__main__:main',  # ajusta al nombre de tu función principal
        ],
    },
    author='Victor',
    description='Bot modular para Quotex con señales y gestión de riesgo',
    url='https://github.com/vhenriquezn/QuotexBot',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
