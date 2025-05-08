from setuptools import setup, find_packages

setup(
    name="legal_advisor_validator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Delega en requirements.txt si lo deseas.
    ],
    entry_points={
        "console_scripts": [
            "legal-validator=validador.service:main"
        ]
    },
    author="Tu Nombre",
    description="Sistema de validación legal semántica",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)