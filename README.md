# Etcd Key-Value Store Command Line Interface

## Overview
This project implements a command-line interface (CLI) for interacting with the **etcd** key-value store. The CLI allows users to perform basic operations such as listing all keys, getting the value for a specific key, putting a new key-value pair, and deleting a key-value pair.

## Dependencies
- Python 3.x
- **etcd3** library

## Setup
1. Ensure you have Python 3.x installed on your system. If not, you can download and install it from the [official Python website](https://www.python.org/).
2. Install the **etcd3** library using pip:
    ```
    pip install etcd3
    ```
3. Clone this repository to your local machine:
    ```
    git clone https://github.com/an02ny/Batch_11.git
    ```
4. Navigate to the project directory:
    ```
    cd Batch_11
    ```


## Usage
1. Run the `week2_code.py` script to start the CLI:
    ```
    python3 week2_code.py
    ```
2. The CLI will display a list of options:
    ```
    Options:
    1. List all keys
    2. Get value for a specific key
    3. Put a new key-value pair
    4. Delete a key-value pair
    5. Exit
    Enter option number:
    ```
3. Enter the option number to perform the desired operation.
4. Follow the prompts to input key or value information as required.

## Functionality
- **List all keys**: Displays a list of all keys present in the **etcd** key-value store.
- **Get value for a specific key**: Allows the user to retrieve the value associated with a specific key.
- **Put a new key-value pair**: Adds a new key-value pair to the **etcd** key-value store.
- **Delete a key-value pair**: Deletes a key-value pair from the **etcd** key-value store.

## Contributing
Contributions are welcome! If you have any suggestions or find any issues, please open an issue or create a pull request on GitHub.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
