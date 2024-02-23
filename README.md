# Game of Life
A basic object-oriented implementation of John Conway's Game of Life

## 1. nano

```
# in ~/.nanorc
set constantshow
set tabsize 4
set tabstospaces
```

## 2. pyenv

1. Install pyenv:

    ```
    curl https://pyenv.run | bash
    ```

    Then add the lines to .bashrc, or just:
    
    ```
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    ```

2. Use pyenv:

   Install specific python version:

    ```
    pyenv install 3.10.4
    pyenv global 3.10.4 # to set default global. pyenv automatically uses the version in local .python-version file if available.
    ```

## 3. poetry

1. Install poetry:

    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```

    Then add the lines to .bashrc. Here are some useful configs:

    ```
    poetry config virtualenvs.prefer-active-python true # poetry will use active python likely set by pyenv -- whatever shows up when you type python --version
    poetry config virtualenvs.in-project true # poetry install will create .venv in the project
    ```

2. Use poetry:

    Just prepend any command line with poetry run, e.g.:
    
    ```
    poetry run python -m src/main.py
    poetry run pylint src
    poetry run pip list # to list package versions, or just poetry show
    ```
