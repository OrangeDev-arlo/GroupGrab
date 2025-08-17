import requests
import json
import csv
import time
import sys
import os
from datetime import datetime

ASCII_ART = r"""
   /$$$$$$                                                 /$$$$$$                     /$$                           
 /$$__  $$                                               /$$__  $$                   | $$                           
| $$  \__/  /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$       | $$  \__/  /$$$$$$  /$$$$$$ | $$$$$$$                      
| $$ /$$$$ /$$__  $$ /$$__  $$| $$  | $$ /$$__  $$      | $$ /$$$$ /$$__  $$|____  $$| $$__  $$                     
| $$|_  $$| $$  \__/| $$  \ $$| $$  | $$| $$  \ $$      | $$|_  $$| $$  \__/ /$$$$$$$| $$  \ $$                     
| $$  \ $$| $$      | $$  | $$| $$  | $$| $$  | $$      | $$  \ $$| $$      /$$__  $$| $$  | $$                     
|  $$$$$$/| $$      |  $$$$$$/|  $$$$$$/| $$$$$$$/      |  $$$$$$/| $$     |  $$$$$$$| $$$$$$$/                     
 \______/ |__/       \______/  \______/ | $$____/        \______/ |__/      \_______/|_______/                      
                                        | $$                                                                        
                                        | $$                                                                        
                                        |__/                                                         

Group Grab Terminal - v1.0.3 ~ By OrangeDev
A simple yet helpful tool to gain info from Roblox Groups all within seconds!
"""

SAVE_TYPE = "json"  # default
MEMBER_LIMIT = None  # None = unlimited
DATA_FILE_JSON = "group_data.json"
DATA_FILE_CSV = "group_data.csv"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(seconds=3):
    for i in range(seconds * 3):
        dots = "." * ((i % 3) + 1)
        sys.stdout.write(f"\rLoading{dots}   ")
        sys.stdout.flush()
        time.sleep(0.333)
    print("\n")

def info():
    print("\n=== Group Grab Info ===")
    print("1. Choose 'Start Group Grab' in the menu.")
    print("2. Enter the Group ID you want to scan.")
    print("3. The program will save all members' User ID, Username, Display Name, and Group Name.")
    print("4. Save format (JSON or CSV) can be changed in Settings.")
    print("5. You can also set a member logging limit in Settings (default = Unlimited).")
    input("\nPress Enter to return to the menu...")

def save_data(data, group_name):
    os.makedirs("GroupData", exist_ok=True)
    safe_group_name = group_name.replace(" ", "_").replace("/", "_")

    if SAVE_TYPE == "json":
        file_name = os.path.join("GroupData", f"{safe_group_name}-group-data.json")
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    elif SAVE_TYPE == "csv":
        file_name = os.path.join("GroupData", f"{safe_group_name}-group-data.csv")
        with open(file_name, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["User ID", "Username", "Display Name", "Group Name"])
            for row in data:
                writer.writerow([row['userId'], row['username'], row['displayName'], row['groupName']])
    return file_name

def fetch_group_members(group_id):
    members = []
    cursor = ""
    group_name = f"Group {group_id}"
    
    try:
        group_info = requests.get(f"https://groups.roblox.com/v1/groups/{group_id}").json()
        if "name" in group_info:
            group_name = group_info["name"]
    except:
        pass

    while True:
        url = f"https://groups.roblox.com/v1/groups/{group_id}/users?limit=100&sortOrder=Asc&cursor={cursor}"
        r = requests.get(url).json()
        if "data" not in r:
            print("Error: Could not fetch group data. Check the Group ID.")
            break
        for user in r['data']:
            if MEMBER_LIMIT and len(members) >= MEMBER_LIMIT:
                return members, group_name  # stop early if limit reached

            member_data = {
                "userId": user['user']['userId'],
                "username": user['user']['username'],
                "displayName": user['user']['displayName'],
                "groupName": group_name
            }
            members.append(member_data)

            # Log each user
            log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S EST")
            print(f"> Logged ~ {member_data['userId']}, {member_data['username']}, "
                  f"{member_data['displayName']}, {group_name}, {log_time}")

        if r.get('nextPageCursor'):
            cursor = r['nextPageCursor']
        else:
            break
    return members, group_name

def start_group_grab():
    group_id = input("\n> Insert Group ID: ").strip()
    print(f"Fetching members from Group {group_id}...\n")
    members, group_name = fetch_group_members(group_id)
    file_name = save_data(members, group_name)
    print(f"\n✅ Saved {len(members)} members from '{group_name}' to file: {file_name}")
    input("\nPress Enter to return to the menu...")

def settings_menu():
    global SAVE_TYPE, MEMBER_LIMIT
    while True:
        clear()
        print("\n=== Settings ===")
        print(f"A - Save File Type (Current: {SAVE_TYPE.upper()})")
        print(f"B - Member Logging Limit (Current: {'Unlimited' if MEMBER_LIMIT is None else MEMBER_LIMIT})")
        print("C - Back to Menu")
        choice = input("\n> ").strip().lower()
        if choice == "a":
            stype = input("\n1 - JSON\n2 - CSV\n> ").strip()
            if stype == "1":
                SAVE_TYPE = "json"
                print("✔ Save type set to JSON.")
            elif stype == "2":
                SAVE_TYPE = "csv"
                print("✔ Save type set to CSV.")
            time.sleep(1)
        elif choice == "b":
            limit = input("\nEnter member logging limit (0 = Unlimited): ").strip()
            try:
                limit = int(limit)
                if limit <= 0:
                    MEMBER_LIMIT = None
                    print("✔ Member logging limit set to Unlimited.")
                else:
                    MEMBER_LIMIT = limit
                    print(f"✔ Member logging limit set to {limit}.")
            except ValueError:
                print("⚠ Invalid number. Please try again.")
            time.sleep(1)
        elif choice == "c":
            break

clear()
print(ASCII_ART)
cmd = input("\nType \"$Start\" to start the program: ").strip()
if cmd.lower() != "$start":
    print("Exiting...")
    sys.exit()

loading_animation()

while True:
    clear()
    print("Welcome to the Group Grab Terminal.\n")
    print("1 - Info")
    print("2 - Start Group Grab")
    print("3 - Settings")
    print("4 - Exit")
    choice = input("\n> ").strip()
    if choice == "1":
        clear()
        info()
    elif choice == "2":
        clear()
        start_group_grab()
    elif choice == "3":
        settings_menu()
    elif choice == "4":
        sys.exit()
    else:
        print("Invalid option.")
        time.sleep(1)

# By OrangeDev
# Version 1.0.3
