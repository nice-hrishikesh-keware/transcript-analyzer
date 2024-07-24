import json
import os
from dotenv import load_dotenv

import uuid

print(uuid.uuid4())


load_dotenv()

OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')

print(OPENAI_TOKEN)

f = open('transcript_summary.json')

data = json.load(f)

print(json.dumps(data))

