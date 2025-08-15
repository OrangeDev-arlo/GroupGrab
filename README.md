# Group Grab

Group Grab is a terminal-based Python tool that collects all members from a Roblox group and saves their information to either JSON or CSV format.  
It records each member’s User ID, Username, Display Name, and the Group Name they were scanned from.  
All files are saved in a `GroupData` folder for easy organization.  

## Features
- Saves member data in either JSON or CSV format
- File name includes the group’s name for easier identification
- Automatic creation of a `GroupData` folder for saved files
- Menu system with Info, Start, and Settings options
- Configurable save format in the settings

## Requirements
- Python 3.7 or newer  
- An internet connection  
- The `requests` library

## Installation
1. Download or clone this repository to your computer.
2. Open a terminal (Command Prompt, PowerShell, or any terminal application).
3. Install dependencies by running:
   ```bash
   pip install requests
   ```

## Usage
1. Navigate to the folder containing the script:
   ```bash
   cd path/to/folder
   ```
2. Run the script:
   ```bash
   python groupgrab.py
   ```
3. When prompted, type:
   ```
   $Start
   ```
4. Choose from the menu:
   - **Info**: Basic instructions on using the program.
   - **Start Group Grab**: Enter a Roblox group ID to collect data.  
     The file will be saved in the `GroupData` folder with the format:  
     ```
     <GroupName>-group-data.json
     ```  
     or  
     ```
     <GroupName>-group-data.csv
     ```
   - **Settings**:  
     - Change the save file type (JSON or CSV)  
     - Delete all saved data from the `GroupData` folder

## Getting a Roblox Group ID
1. Go to the Roblox group page in your browser.
2. Look at the URL in your address bar:
   ```
   https://www.roblox.com/groups/1234567/Group-Name
   ```
3. The number in the URL is the Group ID (in this example, `1234567`).

## Notes
- This tool uses Roblox’s public API to retrieve group members.
- Very large groups may take longer to scan due to pagination.
- The program only collects publicly available group membership information.
- Visual Learner? I get it! Here is a video of the live demo of me setting up the program. 

**Please contact orange_dev_arlo on Discord for any questions or suggestions!**
