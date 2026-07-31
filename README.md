dev-utils/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
└── password_generator.py
import secrets
import string


def generate_password(length=16):
    alphabet = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*()-_=+"
    )
    return "".join(secrets.choice(alphabet) for _ in range(length))


if __name__ == "__main__":
    print("Generated password:")
    print(generate_password())

    # No external dependencies

    __pycache__/
*.pyc
.venv/
venv/
.idea/
.vscode/

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...

# Dev Utils

A small collection of lightweight developer utilities written in Python.

## Features

- Secure password generation
- No third-party dependencies
- Cross-platform
- Simple and easy to extend

## Installation

```bash
git clone https://github.com/USERNAME/dev-utils.git
cd dev-utils
```

## Usage

```bash
python password_generator.py
```

Example output:

```
Generated password:
4yN!8fQk#2LmPz9@
```

## Roadmap

- Hash generator
- UUID generator
- JSON formatter
- Random string generator

## License

MIT
