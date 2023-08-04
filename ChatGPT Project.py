#Install the openai
!pip install -q openai

#Import openai and connect to the 
import openai
sheet_id="Your_Google_Sheet_ID"
worksheet_name="Sheet1"
from google.colab import drive
drive.mount('/content/drive')
from google.colab import auth
auth.authenticate_user()
import gspread
from google.auth import default
from oauth2client.service_account import ServiceAccountCredentials
creds, _ = default()
gc=gspread.authorize(creds)
sheet_name='chatgpt'
sh = gc.open(sheet_name)
sh.worksheets()
worksheet = sh.worksheet(worksheet_name)
worksheet.get_all_records()
sheet=gc.open(sheet_name).sheet1
websites=sheet.col_values(1)
openai.api_key = 'Your_API_KEY'
messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]
for i,Website in enumerate(websites):
  if (i != 0):
    message=Website
    if message:
      messages.append(
        {"role": "user", "content": message},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301", messages=messages
    )
reply = chat.choices[0].message.content
sheet.update_cell(i+1,2,reply)

