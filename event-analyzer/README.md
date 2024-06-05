# Event Analyzer

This python script is used to analyze and parse the events that are located in the JSON file sent to `https://storeapi.kobo.com/v1/analytics/event`. The script manages a dictionary of events stored in memory. It allows you to update the dictionary from a JSON file, list all different event types, list entries by a specific type, print the number of entries, and export entries of a given type to JSON files. Additionally, it provides a command to export entries in a pretty-printed JSON format.

To add new events, you need to save the JSON object from the request in the same folder as this script. Execute the `update` command and provide the correct JSON filename to update the dictionary.

The dictionary is saved to disk with pickle and is loaded everytime the script starts.

## Usage

1. Run the script.
2. Enter commands interactively.
   - `update`: Update the dictionary from a JSON file.
   - `list types`: List all different event types.
   - `list entries`: List entries by a specific type.
   - `size`: Print the number of entries in the dictionary.
   - `export`: Export entries of a given type to a JSON file.
   - `export pretty`: Export entries of a given type to a pretty JSON file.
   - `help`: Display available commands.
   - `quit`: Save the dictionary and exit.
   - `quit!`: Exit without saving the dictionary.

