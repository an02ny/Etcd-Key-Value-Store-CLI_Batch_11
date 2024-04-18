import etcd3
import sys

# Connect to etcd
etcd = etcd3.client()

# ANSI escape codes for bold text
BOLD = "\033[1m"
RESET = "\033[0m"

def list_keys():
    """
    List all keys in etcd.
    """
    try:
        keys = etcd.get_all()
        if keys:
            return [metadata.key.decode('utf-8') for _, metadata in keys if metadata]
        else:
            print("No keys found.")
            return []
    except Exception as e:
        print("Error occurred while listing keys:", e)
        return []


def get_value(key):
    """
    Get the value for a specific key.
    """
    try:
        value, _ = etcd.get(key)
        if value is not None:
            return value.decode('utf-8')
        else:
            return BOLD + "Key not found." + RESET
    except Exception as e:
        print("Error occurred while getting value for key:", e)
        return None

def put_key_value(key, value):
    """
    Put a key-value pair into etcd.
    """
    try:
        etcd.put(key, value)
        print(BOLD + "Key-value pair added successfully." + RESET)
    except Exception as e:
        print(BOLD + "Error occurred while putting key-value pair:" + RESET, e)

def delete_key_value(key):
    """
    Delete a key-value pair from etcd.
    """
    try:
        value, _ = etcd.get(key)
        if value is not None:
            etcd.delete(key)
            print(BOLD + "Key-value pair deleted successfully." + RESET)
        else:
            print(BOLD + "Key not found." + RESET)
    except Exception as e:
        print(BOLD + "Error occurred while deleting key-value pair:" + RESET, e)

if __name__ == "__main__":
    while True:
        print("Options:")
        print("1. List all keys")
        print("2. Get value for a specific key")
        print("3. Put a new key-value pair")
        print("4. Delete a key-value pair")
        print("5. Exit")
        option = input("Enter option number: ")

        if option == "1":
            all_keys = list_keys()
            if all_keys:
                print(BOLD + "List of keys:" + RESET, all_keys)
        elif option == "2":
            specific_key = input("Enter the key you want to retrieve value for: ")
            value = get_value(specific_key)
            print(BOLD + "Value for key", specific_key, "is:" + RESET, value)
        elif option == "3":
            new_key = input("Enter the new key: ")
            new_value = input("Enter the value for the new key: ")
            put_key_value(new_key, new_value)
        elif option == "4":
            key_to_delete = input("Enter the key you want to delete: ")
            delete_key_value(key_to_delete)
        elif option == "5":
            print(BOLD + "Exiting program." + RESET)
            sys.exit()
        else:
            print(BOLD + "Invalid option." + RESET)

