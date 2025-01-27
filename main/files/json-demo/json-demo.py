# project read the json file and print all the data in table format
# read the root folder and check is there json file exist if exist read and transform into the table form and display its
import itertools
import json
import os

ROOT_PATH = "C:\\stock-price"

# method read the folder
def read_root_path():
    all_file = []
    for root, dirs, files in os.walk(ROOT_PATH):
        json_files = [os.path.join(root, file) for file in files if file.endswith('.json')]
        all_file.append(json_files)
    # Flatten the list of lists
    all_file = list(itertools.chain(*all_file))
    # all file and iterate its
    for file in all_file:
        transformation(file)


# read the json and margin into single csv file
def transformation(file_path):
    print("# " * 40)
    print(f"Name For File {file_path}")
    print("# " * 40)
    if isinstance(file_path, str) and file_path.endswith('.json'):
        # Read the file for txt
        with open(file_path, 'r', encoding='utf-8') as file:
            json_string = file.read()
        # send the read text for report generate
        try:
            json_object = json.loads(json_string)
            data_view = json_object.get('dataView')
            print("# " * 40)
            print(f"Summary Detail Total Columns = {data_view.get('totalColumns')}, Total Row = {data_view.get('totalRows')}")
            print("# " * 40)
            # extract the name from the columns
            column_name = [item['name'] for item in data_view.get('columns')]
            # giving extra space
            print(','.join(column_name))
            print("# " * 40)
            for row in data_view.get('rows'):
                print(','.join(str(item) for item in row.get('text')))
        except json.JSONDecodeError as e:
            print("Invalid JSON:", e)
    else:
        print('File type not supported')


if __name__ == '__main__':
    read_root_path()
    pass
