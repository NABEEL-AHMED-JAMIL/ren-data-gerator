import csv
import os # need to study the os topic

# read file
# Files are loaded from secondary memory to the main memory and then processed by the CPU.
# Once the processing is done, the data is written back to the secondary memory.
def read_file(file_path):
    """
    => method use to read the file and return content method need to check the file type and also add try catch
    :param file_path:
    :return: {
        "dataView": {
            "totalColumns": 7,
            "columns": [
                {
                    "name": "Date",
                    "order": 0
                }
            ],
            "totalRows": 1000,
            "rows": [
                {
                    "text": []
                }
            ]
        }
    }
    """
    # Step 1: Create a dictionary with an initial key-value pair
    data_view = {}
    try:
        with open(file_path, mode="r") as csvfile:
            # method use to read the csv file
            reader = csv.reader(csvfile)
            # reading the header row
            header = next(reader)
            # adding the total count of header columns
            header_list = []
            for index, hd in enumerate(header):
                hd_obj = {
                    "name": hd,
                    "order": index
                }
                header_list.append(hd_obj)
            # adding the total col count
            data_view["totalColumns"] = len(header)
            # adding the col list
            data_view["columns"] = header_list
            # total count
            total_rows = 0
            # total row in file
            records = []
            # read the remaining rows
            for row in reader:
                # appending each row into rows
                records.append({
                    "text": row
                })
                total_rows = total_rows + 1
            data_view["totalRows"] = total_rows
            data_view["rows"] = records
        # root json
        root = {
            "dataView": data_view
        }
        return root
    except FileNotFoundError as e:
        print(f"Error: The file was not found. {e}")
    except csv.Error as e:
        print(f"Error: There was a problem reading the CSV file. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# write file [w => write| a => append]
def write_file(file_path, rows):
    try:
        with open(file_path, mode='w', newline='') as csvfile:
            # method use to read the csv file
            writer = csv.writer(csvfile)
            # get the rows
            writer.writerows(rows)
    except csv.Error as e:
        print(f"Error: There was a problem write the CSV file. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# update file
def update_file(file_path, rows):
    try:
        with open(file_path, mode='a', newline='') as csvfile:
            # method use to read the csv file
            writer = csv.writer(csvfile)
            # get the rows
            writer.writerows(rows)
    except FileNotFoundError as e:
        print(f"Error: The file was not found. {e}")
    except csv.Error as e:
        print(f"Error: There was a problem write the CSV file. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# delete file
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    else:
        print(f"The file {file_path} does not exist.")

if __name__ == '__main__':
    new_data = [
        ["David", 28, "Miami"],
        ["Eva", 22, "Houston"]
    ]
    write_file("example.csv", new_data)
    update_file("example.csv", new_data)
    print(read_file("example.csv"))
    delete_file("example.csv")