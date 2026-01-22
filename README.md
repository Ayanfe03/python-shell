# Python Shell

A simple **python shell** implemented in Python as part of Codecrafters exercises.  
This project implements a basic command-line interface (CLI) with support for **built-in commands** and continuous input loops, designed for learning and experimentation.

---

## Features

Currently supported built-in commands:

- `echo` – prints the arguments back to the terminal.
- `type` – checks if a command is a shell builtin.
- `exit` – exits the shell.

Behavior:

- The shell displays a `$ ` prompt.
- Commands are split into words: the first word is interpreted as the command, and the rest as arguments.
- Unknown commands print a “command not found” message.
- Safely handles missing arguments for `type`.

Example usage:

```bash
$ echo Hello World
Hello World
$ type echo
echo is a shell builtin
$ type ls
ls: not found
$ exit
```

## Getting Started

Prerequisites

- Python 3.x installed on your system


# Running the Shell

- Clone the repository and run the shell:

```bash
git clone https://github.com/username/mini-shell-python.git
cd mini-shell-python
python shell.py
```


The shell will run in a loop until you type exit.


## Planned Features

- Add support for commands like cwd, pwd, etc.

- Implement command history and arrow key navigation

- Support for redirection (> / <)

- Add autocompletion

- Locating executable files etc...


## Contributing

Contributions are welcome!

- Fork the repo

- Create a feature branch (git checkout -b feature-name)

- Commit your changes (git commit -m 'Add feature')

- Push to your branch (git push origin feature-name)

- Open a pull request

## License

- MIT License
