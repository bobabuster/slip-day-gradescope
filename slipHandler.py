import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("slipServiceAccount.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet by name or URL
sheet = client.open("https://docs.google.com/spreadsheets/d/13CPITdiZm45VVoSRK1n_-HwG-lKIBzyf8ZMLDdw_Q6o/edit?gid=1855817654#gid=1855817654")

# Select the tab (worksheet) with form responses by name
form_responses_tab = sheet.worksheet("Slip Days")  # or whatever your tab is called

# Get all records from that tab
rows = form_responses_tab.get_all_records()
