import pickle
import json

# Initialize an empty dictionary to store events
event_dict = {}

def load_data_from_disk():
    try:
        with open('data.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

def save_data_to_disk(data):
    with open('data.pkl', 'wb') as file:
        pickle.dump(data, file)

def update_dictionary_from_json(json_data):
    global event_dict
    events = json_data.get('Events', [])
    for event in events:
        event_id = event.get('Id')
        if event_id:
            event_dict[event_id] = event

def list_all_types():
    unique_types = set(event['EventType'] for event in event_dict.values())
    print("All different types:")
    print(', '.join(unique_types))

def list_entries_by_type(event_type):
    matching_entries = [event for event in event_dict.values() if event['EventType'] == event_type]
    print(f"All entries with type '{event_type}':")
    for entry in matching_entries:
        print(json.dumps(entry, indent=2))

def export_entries_to_json(event_type):
    matching_entries = [event for event in event_dict.values() if event['EventType'] == event_type]
    file_name = f"{event_type}.json"
    with open(file_name, 'w') as file:
        json.dump(matching_entries, file)
    print(f"Entries of type '{event_type}' exported to {file_name}")

def export_pretty_entries_to_json(event_type):
    matching_entries = [event for event in event_dict.values() if event['EventType'] == event_type]
    file_name = f"{event_type}_pretty.json"
    with open(file_name, 'w') as file:
        json.dump(matching_entries, file, indent=2)
    print(f"Pretty JSON entries of type '{event_type}' exported to {file_name}")

def print_dictionary_size():
    print(f"Number of entries in the dictionary: {len(event_dict)}")

def display_help():
    print("Available commands:")
    print("update - Update dictionary from a JSON file")
    print("list types - List all different event types")
    print("list entries - List entries by a specific type")
    print("size - Print the number of entries in the dictionary")
    print("help - Display this help message")
    print("quit - Save the dictionary and exit")
    print("quit! - Exit without saving the dictionary")
    print("export - Export entries of a given type to a JSON file")
    print("export pretty - Export entries of a given type to a pretty JSON file")

def main():
    global event_dict
    event_dict = load_data_from_disk()

    while True:
        command = input("Enter a command (type 'help' for available commands): ").lower()

        if command == 'update':
            file_path = input("Enter the path to the JSON file: ")
            try:
                with open(file_path, 'r') as file:
                    json_data = json.load(file)
                    update_dictionary_from_json(json_data)
                    print("Dictionary updated successfully.")
            except FileNotFoundError:
                print("File not found. Please enter a valid path.")

        elif command == 'list types':
            list_all_types()

        elif command == 'list entries':
            event_type = input("Enter the type to list entries: ")
            list_entries_by_type(event_type)

        elif command == 'size':
            print_dictionary_size()

        elif command == 'help':
            display_help()

        elif command == 'quit':
            save_data_to_disk(event_dict)
            print("Dictionary saved to disk. Exiting...")
            break

        elif command == 'quit!':
            print("Exiting without saving the dictionary.")
            break

        elif command == 'export':
            event_type = input("Enter the type to export entries: ")
            export_entries_to_json(event_type)

        elif command == 'export pretty':
            event_type = input("Enter the type to export entries: ")
            export_pretty_entries_to_json(event_type)

        else:
            print("Invalid command. Type 'help' for available commands.")

if __name__ == "__main__":
    main()
