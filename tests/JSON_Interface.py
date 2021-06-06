from nested_lookup import nested_lookup

class JSON_Interface:
    def __init__(self, file) -> None:
        self.file = file
    def find(self, keys):
        """Find elememts from the JSON data

        Args:
            keys (list): A list of values to search for

        Returns:
            list: All values matching requirements
        """        
        values = self.file
        for key in keys:
            values = nested_lookup(key, values)
        return values

# j = JSON_Interface(test_json)
# v = j.find(test_json, ['POS 1', 'ip'])
#print(v)
