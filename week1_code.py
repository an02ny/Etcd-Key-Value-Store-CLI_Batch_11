import etcd3
import sys

# Connect to etcd
etcd = etcd3.client()

def list_keys():
    """
    List all keys in etcd.
    """
    try:
        keys = etcd.get_all()
        if keys:
            return [metadata.key.decode('utf-8') for _,metadata in keys]
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
            return "Key not found."
    except Exception as e:
        print("Error occurred while getting value for key:", e)
        return None

def put_key_value(key, value):
    """
    Put a key-value pair into etcd.
    """
    try:
        etcd.put(key, value)
        print("Key-value pair added successfully.")
    except Exception as e:
        print("Error occurred while putting key-value pair:", e)


if __name__ == "__main__":
    while True:
        print("Options:")
        print("1. List all keys")
        print("2. Get value for a specific key")
        print("3. Put a new key-value pair")
        print("4. Exit")
        option = input("Enter option number: ")

        if option == "1":
            all_keys = list_keys()
            if all_keys:
                print("List of keys:", all_keys)
        elif option == "2":
            specific_key = input("Enter the key you want to retrieve value for: ")
            print("Value for key", specific_key, ":", get_value(specific_key))
        elif option == "3":
            new_key = input("Enter the new key: ")
            new_value = input("Enter the value for the new key: ")
            put_key_value(new_key, new_value)
        elif option == "4":
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid option.")
