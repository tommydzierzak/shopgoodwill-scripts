import os
import json


# Set environment variables for testing

os.environ["USERNAME"] = "test_username"
os.environ["PASSWORD"] = "test_password"
os.environ["bid_snipe_time_delta"] = "15 seconds"


# Load environment variables
USERNAME = os.getenv("USERNAME", "")
PASSWORD = os.getenv("PASSWORD", "")
bid_snipe_time_delta = os.getenv("bid_snipe_time_delta", "")

# File paths
input_file = "config.json.example"
output_file = "configTest.json"

# Read the existing config file
with open(input_file, "r") as file:
    config = json.load(file)

del config["auth_info"]["access_token"]
del config["auth_info"]["encrypted_username"]
del config["auth_info"]["encrypted_password"]


# Update the auth_info section with environment variables
config["auth_info"]["username"] = USERNAME
config["auth_info"]["password"] = PASSWORD
config["bid_sniper"]["bid_snipe_time_delta"] = bid_snipe_time_delta

# Write the updated config to a new file
with open(output_file, "w") as file:
    json.dump(config, file, indent=4)

print(f"Updated config saved to {output_file}")