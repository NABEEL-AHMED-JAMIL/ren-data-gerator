# all generator
from generators import TYPES_TO_GENERATORS
# schemas detail
from schemas import (
    CUSTOMERS_SCHEMA,
    LEADS_SCHEMA,
    PEOPLE_SCHEMA,
    ORGANIZATIONS_SCHEMA,
    PRODUCTS_SCHEMA,
    OFFERS_SCHEMA
)

# Schema to dict
SCHEMA_TO_DICT = {
    'customers' : CUSTOMERS_SCHEMA,
    'leads' : LEADS_SCHEMA,
    'people' : PEOPLE_SCHEMA,
    'organizations' : ORGANIZATIONS_SCHEMA,
    'products': PRODUCTS_SCHEMA,
    'offers' : OFFERS_SCHEMA
}

# method use to return the list by dic-key
def dictionary_by_key(schema_dict, key, type=1):
    if type == 1:
        return [elem[key] for elem in schema_dict]
    else:
        return [TYPES_TO_GENERATORS[elem[key]] for elem in schema_dict]

# generate file [generate the file]
# headers 'elem have object which contain name|type' return list 'name'
# headers = [elem['name'] for elem in schema_dict]
# return 'elem type' target schema => return list 'type'
# types = [elem['type'] for elem in schema_dict]
# return the function from the types
# faker_function = [TYPES_TO_GENERATORS[elem] for elem in types]
# faker_value = [elem() for elem in faker_function]
def generate_file(schema='customers', count=1000000):
    # passing key so its return the schema dictionary
    schema_dict = SCHEMA_TO_DICT[schema]
    if schema_dict:
        # headers 'elem have object which contain name|type' return list 'name'
        headers = dictionary_by_key(schema_dict, 'name', 1)
        # return 'elem type' target schema => return list 'type'
        faker_function = dictionary_by_key(schema_dict, 'type', 2)
        return process_data(headers, faker_function, count)
    else:
        print('schema not found.')

# method use to create the json string
def process_data(headers, faker_function, count=1000000):
    # Step 1: Create a dictionary with an initial key-value pair
    data_view_json = {}
    # convert the header into format
    header_list = []
    for index, hd in enumerate(headers):
        hd_obj = {
            "name": hd,
            "order": index
        }
        header_list.append(hd_obj)
    # adding the total col count
    data_view_json["totalColumns"] = len(headers)
    # adding the col list
    data_view_json["columns"] = header_list
    # total count
    total_rows = 0
    # total row in file
    records = []
    # read the remaining rows
    for row in range(1, count+1):
        # appending each row into rows
        records.append({
            "text": [elem() for elem in faker_function]
        })
        total_rows = total_rows + 1
    data_view_json["totalRows"] = total_rows
    data_view_json["rows"] = records
    # root json
    root = {
        "dataView": data_view_json
    }
    return root


# root path to run the code
if __name__ == '__main__':
    # customers
    print(generate_file('customers',1))
    # leads
    print(generate_file('leads', 1))
    # people
    print(generate_file('people', 1))
    # organizations
    print(generate_file('organizations', 1))
    # test with products & offers
    print(generate_file('offers', 5))