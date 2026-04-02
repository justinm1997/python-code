"""

writing to files
date/time
calculated average.... to come

"""

import datetime

def get_sugar():
    # 2. Ask the user for their data
    blood_sugar = input("Enter your current blood sugar level: ")
    return blood_sugar

def save_to_file(timestamp_str, blood_sugar):
    # 3. Store it in a dictionary using the timestamp as the key
    health_log = {
        timestamp_str: blood_sugar
}

    # 4. Append ('a' mode) the new entry to our text file so it grows over time
    with open("blood_sugar_log.txt", "a") as file:
        file.write(f"[{timestamp_str}] Blood Sugar: {health_log[timestamp_str]}\n")



def main():


# 1. Get the current time and format it nicely

bs = get_sugar()
current_time = datetime.datetime.now()
timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
save_to_file(timestamp_str, )

print("Health data successfully logged!")
main()