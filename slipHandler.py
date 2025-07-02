import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("slipServiceAccount.json", scope)
client = gspread.authorize(creds)


sheet = client.open("https://docs.google.com/spreadsheets/d/13CPITdiZm45VVoSRK1n_-HwG-lKIBzyf8ZMLDdw_Q6o/edit?gid=1855817654#gid=1855817654")
form_responses_tab = sheet.worksheet("Slip Days") 
rows = form_responses_tab.get_all_records() # list of dictionaries corresponding to each row/slip day request

slip_days_remaining = {} # Keeps track of remaining slip days per student; defaults to 8


for rowdict in rows:
    # check if that row/request has been processed yet (need to add processed column to the tab)
    # if processed, continue
    # if not, check student has enough slip days remaining
        # if not enough, throw error
        # else subtract the days from the student's entry in slip_days_remaining
    continue
    











