# LLM Committer for GitHub

This project provides a simple way to setup a custom git commit command that uses an LLM to generate a commit message.

## Features

- Automates the process of: (setup.py)

  - Copying the script to /usr/local/bin
  - Making the script executable
  - Setting up a custom git commit command

- Stages and commits all changes to the current branch (git_add_commit.py) with a single command.

## Prerequisites

- Python 3.10+
- MacOS
- Git
- An LLM API key (e.g. OpenAI, Anthropic, etc.)

## Usage

1. Clone the repository

```
git clone https://github.com/your-repo/llm-committer.git
```

2. Navigate to the repository directory

```
cd llm-committer
```

3. Run the setup script

```
python3 src/setup.py <path_to_script> <keyword_name>
```

- `<path_to_script>` is the path to the script you want to use for your custom / commit command.
- `<keyword_name>` is the name you want to use for your custom / commit command.

Example:

```
python3 src/setup.py src/git_add_commit.py gac
```

- This will copy the `git_add_commit.py` script to /usr/local/bin and make it executable, and then set up a custom git commit command called `gac`.

4. Use your custom / commit command

```
gac "Your commit message"
```
