# Party Riddle Simulation
This project is a simulation of the situation present in the following riddle: 

> There is a crowd of people in the room. Each person is asked to choose another person in the room (without telling anyone). At a given signal, each person tries to reach the person they have chosen and stand behind them. • What pattern will emerge when the ‘dust settles’?
>

## Installation

1. Install uv (if not already installed):
   https://docs.astral.sh/uv/

2. Clone the repository:
    ```bash
        git clone https://github.com/username/project-name.git
        cd project-name
    ```
3. Create a virtual environment and install dependencies:
   ```bash
    uv sync
   ```
4. Run the project:
    ```bash
    uv run python main.py
    ```

## Usage

Once you run the script, you'll see a simple CLI that will guide you through the process. The main command is `simulate <n>`, where `<n>` is an integer that represents the number of nodes - people at the party.