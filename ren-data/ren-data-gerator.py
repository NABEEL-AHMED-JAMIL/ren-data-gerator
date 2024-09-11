import json
import os
import random
import string
import time
from faker import Faker
import mongodb

fake = Faker()

# Function to generate a random alphanumeric string
def generate_random_id(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

# Function to create a random RTB JSON request
def create_random_truck_request():
    rtb_request = {
        "id": generate_random_id(),
        "imp": [
            {
                "id": generate_random_id(),
                "truck": {
                    "w": random.randint(100, 1000),
                    "h": random.randint(100, 500),
                    "pos": random.choice([1, 2, 3, 4])
                },
                "spd": random.randint(100, 1000),
            }
        ],
        "device": {
            "ua": random.randint(100, 1000),
            "ip": fake.ipv4_public()
        }
    }
    return rtb_request

def write_rtb_request_to_file():
    # Generate a random RTB request
    random_rtb_request = create_random_truck_request()
    # Convert to JSON
    json_rtb_request = json.dumps(random_rtb_request, indent=4)
    # Get current timestamp
    current_time = time.strftime("%Y-%m-%d-%H-%M-%S")
    current_time_file = f'file_{current_time}'
    folder_directory_path = f'D:/efs/input/{time.strftime("%Y-%m-%d-%H")}'
    # Write JSON to a text file with timestamp in the filename
    file_path = f'{folder_directory_path}/{current_time_file}.txt'
    # check the path exist or not if not create the new one
    if not os.path.exists(folder_directory_path):
        print(f"Directory added {folder_directory_path}")
        os.makedirs(folder_directory_path)

    with open(file_path, 'w') as file:
        file.write(json_rtb_request)
        save_file_detail(folder_directory_path, file_path, time.ctime())
    print(f"JSON content written to {file_path}")


# function use to store the file detail in mongodb
def save_file_detail(folder_directory_path, file_path, current_data):
    rtb_request = {
        "folderPath": folder_directory_path,
        "filePath": file_path,
        "tag": generate_random_id(),
        "created": current_data
    }
    mongodb.save_data('rawData', rtb_request)

if __name__ == "__main__":
    # Run indefinitely, generating and writing a new RTB request every 5 seconds
    while True:
        write_rtb_request_to_file()
        time.sleep(5)  # Wait for 10 seconds