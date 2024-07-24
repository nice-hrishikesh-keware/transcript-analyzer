from openai import OpenAI
import json
import os
from dotenv import load_dotenv
import uuid

load_dotenv()
OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')

client = OpenAI(api_key=OPENAI_TOKEN)

with open('transcript.json') as f:
    transcriptData = json.load(f)

with open('expectedSummerydataFormat.json') as f:
    expected_format = json.load(f)

json_transcript = json.dumps(transcriptData)

# Prepare the conversation history for the API
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": f"I need data for each product, and related issues with date in json format. Also add a category of each product, also add a brand. Remove all new lines and whitespaces. Don't explain data just give raw json without formatting it.I want output in this format {expected_format}"
        },
        {
            "role": "user",
            "content": json_transcript
        }
    ],
    temperature=0.5,
    max_tokens=600,
    top_p=1
)

transcript_summary = response.choices[0].message.content

fileId = uuid.uuid4()
with open(f'transcript_summary_{fileId}.json', 'w') as f:
    json.dump(transcript_summary, f)
