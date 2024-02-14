import imaplib
import email
import pandas as pd

# Connect to email account and retrieve the email containing the table
imap_server = imaplib.IMAP4_SSL('imap.outlook.com')
imap_server.login('Shivamsethji@outlook.com', 'SS82@shivam')
imap_server.select('INBOX')

# Search for the email containing the table and fetch it
status, email_ids = imap_server.search(None, 'SUBJECT "data "')
email_id = email_ids[0].split()[0]
status, email_data = imap_server.fetch(email_id, '(RFC822)')

# Parse the email and extract the table data
email_message = email.message_from_bytes(email_data[0][1])
table_data = []

for part in email_message.walk():
    if part.get_content_type() == 'text/html':
        html = part.get_payload(decode=True)
        df = pd.read_html(html)[0]  # Extract the first table from the HTML
        table_data = df.values.tolist()

# Create a DataFrame from the table data and write it to an Excel file
df = pd.DataFrame(table_data)
df.to_excel('table270_.xlsx', index=False, header=False)