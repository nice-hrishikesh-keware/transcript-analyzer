from openai import OpenAI
import json
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')

client = OpenAI(api_key=OPENAI_TOKEN)

# Load JSON data from a file or directly as a string
json_data = '''
[
    {"date":"2024-07-03","start_time":"10:00:00","end_time":"10:15:00","transcript":[
        {"datetime":"2024-07-03 10:00:00","speaker":"customer","message":"Hi,I'm looking for a new laptop for both work and gaming.Can you help me find something suitable?"},
        {"datetime":"2024-07-03 10:01:00","speaker":"agent","message":"Of course!Could you please let me know your budget and any specific requirements you have?"},
        {"datetime":"2024-07-03 10:02:00","speaker":"customer","message":"I'm looking to spend around $1000.I need something with a good graphics card for gaming and enough RAM for multitasking."},
        {"datetime":"2024-07-03 10:03:00","speaker":"agent","message":"Got it.For that budget,I recommend the Acer Nitro 5.It comes with a 10th Gen Intel Core i5 processor,16GB of RAM,and an NVIDIA GeForce GTX 1650 graphics card.It should handle both your work and gaming needs quite well."},
        {"datetime":"2024-07-03 10:05:00","speaker":"customer","message":"That sounds great.How much storage does it have?"},
        {"datetime":"2024-07-03 10:06:00","speaker":"agent","message":"The Acer Nitro 5 has a 512GB SSD,which offers fast performance and ample storage for most users.You can also expand the storage if needed."},
        {"datetime":"2024-07-03 10:07:00","speaker":"customer","message":"Perfect,I think I'll go with that.How soon can it be delivered?"},
        {"datetime":"2024-07-03 10:08:00","speaker":"agent","message":"If you order today,it can be delivered within 3-5 business days.Would you like me to assist you with placing the order?"},
        {"datetime":"2024-07-03 10:10:00","speaker":"customer","message":"Yes,please.Thank you for your help!"}
    ]},
    {"date":"2024-07-15","start_time":"11:15:00","end_time":"11:30:00","transcript":[
        {"datetime":"2024-07-15 11:15:00","speaker":"customer","message":"Hi,my smartphone isn't charging properly.It sometimes stops charging even though it's plugged in.Can you help?"},
        {"datetime":"2024-07-15 11:16:00","speaker":"agent","message":"I'm sorry to hear that you're having trouble with your phone.Could you please tell me the make and model of your smartphone?"},
        {"datetime":"2024-07-15 11:17:00","speaker":"customer","message":"It's a Samsung Galaxy S21."},
        {"datetime":"2024-07-15 11:18:00","speaker":"agent","message":"Thank you.There are a few things we can try to troubleshoot the issue.First,have you tried using a different charging cable and adapter?"},
        {"datetime":"2024-07-15 11:19:00","speaker":"customer","message":"Yes,I tried another cable and adapter,but the problem persists."},
        {"datetime":"2024-07-15 11:20:00","speaker":"agent","message":"I see.Sometimes debris can get stuck in the charging port.Have you checked and cleaned the charging port on your phone?"},
        {"datetime":"2024-07-15 11:21:00","speaker":"customer","message":"I haven't tried that yet."},
        {"datetime":"2024-07-15 11:22:00","speaker":"agent","message":"Please use a small brush or compressed air to gently clean the charging port.If the issue still persists,we may need to perform a software update or reset."},
        {"datetime":"2024-07-15 11:24:00","speaker":"customer","message":"Okay,I'll try cleaning the port and see if that helps."},
        {"datetime":"2024-07-15 11:25:00","speaker":"agent","message":"Great.If cleaning the port doesn't resolve the issue,please reach out again,and we'll explore further troubleshooting steps or consider a service repair."},
        {"datetime":"2024-07-15 11:26:00","speaker":"customer","message":"Will do.Thanks for your assistance!"}
    ]},
    {"date":"2024-07-15","start_time":"14:30:00","end_time":"14:50:00","transcript":[
        {"datetime":"2024-07-15 14:30:00","speaker":"customer","message":"Hello,I recently purchased a TV from your store,and I wanted to know more about the warranty."},
        {"datetime":"2024-07-15 14:31:00","speaker":"agent","message":"Sure,I'd be happy to help.Could you please provide me with the model number of the TV and the date of purchase?"},
        {"datetime":"2024-07-15 14:32:00","speaker":"customer","message":"The model number is LG OLED55CXPUA,and I bought it on June 15th."},
        {"datetime":"2024-07-15 14:33:00","speaker":"agent","message":"Thank you.The LG OLED55CXPUA comes with a standard 1-year manufacturer warranty,which covers any manufacturing defects or issues that arise during normal use."},
        {"datetime":"2024-07-15 14:34:00","speaker":"customer","message":"What about extended warranties?Are there any options available?"},
        {"datetime":"2024-07-15 14:35:00","speaker":"agent","message":"Yes,we offer extended warranties.You can choose from a 2-year,3-year,or 5-year extended warranty plan.These plans cover additional repairs and service beyond the manufacturer warranty period."},
        {"datetime":"2024-07-15 14:37:00","speaker":"customer","message":"How much would a 3-year extended warranty cost?"},
        {"datetime":"2024-07-15 14:38:00","speaker":"agent","message":"The 3-year extended warranty for your TV model costs $150.This covers all parts and labor for any repairs needed during the warranty period."},
        {"datetime":"2024-07-15 14:40:00","speaker":"customer","message":"I think I'll go with the 3-year warranty.How do I purchase it?"},
        {"datetime":"2024-07-15 14:41:00","speaker":"agent","message":"I can assist you with that.I'll need some information to complete the purchase.May I proceed with your details?"},
        {"datetime":"2024-07-15 14:42:00","speaker":"customer","message":"Yes,please go ahead."},
        {"datetime":"2024-07-15 14:43:00","speaker":"agent","message":"Great.I'll take your details now and process the warranty purchase.Thank you for choosing our service!"}
    ]},
    {"date":"2024-07-22","start_time":"09:45:00","end_time":"10:00:00","transcript":[
        {"datetime":"2024-07-22 09:45:00","speaker":"customer","message":"Hi,I bought a pair of wireless earbuds from your store,but they're not working properly.I'd like to request a refund."},
        {"datetime":"2024-07-22 09:46:00","speaker":"agent","message":"I'm sorry to hear that you're having issues with the earbuds.Can you please provide me with the order number or receipt for the purchase?"},
        {"datetime":"2024-07-22 09:47:00","speaker":"customer","message":"Yes,the order number is 123456789."},
        {"datetime":"2024-07-22 09:48:00","speaker":"agent","message":"Thank you.I'll look up your order and verify the purchase details.Can you describe the issue you're facing with the earbuds?"},
        {"datetime":"2024-07-22 09:49:00","speaker":"customer","message":"The earbuds keep disconnecting from my phone and the battery life is significantly shorter than expected."},
        {"datetime":"2024-07-22 09:50:00","speaker":"agent","message":"I apologize for the inconvenience.Since the product is within the refund period,we can process your request.Would you prefer a refund to your original payment method or store credit?"},
        {"datetime":"2024-07-22 09:51:00","speaker":"customer","message":"I'd like a refund to my original payment method,please."},
        {"datetime":"2024-07-22 09:52:00","speaker":"agent","message":"Understood.I'll initiate the refund process right away.You should see the refund reflected in your account within 5-7 business days.Please make sure to return the earbuds with all original packaging and accessories."},
        {"datetime":"2024-07-22 09:54:00","speaker":"customer","message":"Thank you for your help.I'll return them as soon as possible."},
        {"datetime":"2024-07-22 09:55:00","speaker":"agent","message":"You're welcome.If you need any further assistance,please don't hesitate to reach out.Have a great day!"}
    ]},
    {"date":"2024-07-22","start_time":"15:00:00","end_time":"15:20:00","transcript":[
        {"datetime":"2024-07-22 15:00:00","speaker":"customer","message":"Hi,I bought the LG OLED55CXPUA TV from your store a few weeks ago,and I'm really disappointed with it."},
        {"datetime":"2024-07-22 15:01:00","speaker":"agent","message":"I'm sorry to hear that you're not satisfied with the LG OLED55CXPUA TV.Could you please tell me more about the issues you're facing?"},
        {"datetime":"2024-07-22 15:02:00","speaker":"customer","message":"The picture quality is not as good as I expected.There are strange color banding issues,and the screen flickers occasionally.It's really frustrating."},
        {"datetime":"2024-07-22 15:03:00","speaker":"agent","message":"I apologize for the inconvenience you've experienced.That certainly doesn't sound like the performance we expect from the LG OLED55CXPUA TV.Have you tried adjusting the picture settings or checking for any firmware updates?"},
        {"datetime":"2024-07-22 15:05:00","speaker":"customer","message":"Yes,I've tried adjusting the settings and updating the firmware,but the issues persist.The light spots are especially annoying during dark scenes."},
        {"datetime":"2024-07-22 15:07:00","speaker":"agent","message":"I understand your frustration.Since you've already tried basic troubleshooting,it may be a hardware issue.I recommend bringing the TV to one of our service centers for a thorough inspection.If it's found to be defective,we'll repair or replace it under warranty."},
        {"datetime":"2024-07-22 15:10:00","speaker":"customer","message":"I didn't expect to have these issues with a brand-new TV.It's really disappointing."},
        {"datetime":"2024-07-22 15:12:00","speaker":"agent","message":"I apologize for the inconvenience you've faced.We aim to provide quality products and services,and I'm sorry this wasn't your experience.Let's get this resolved as quickly as possible.Can I help you set up an appointment at the nearest service center?"},
        {"datetime":"2024-07-22 15:14:00","speaker":"customer","message":"Yes,please.I'd like to get this sorted out as soon as possible."}
    ]},
    {"date":"2024-07-23","start_time":"11:00:00","end_time":"11:20:00","transcript":[
        {"datetime":"2024-07-23 11:00:00","speaker":"customer","message":"Hi,I recently purchased the Sony Bravia X900H TV from your store,and I just wanted to share my experience with it."},
        {"datetime":"2024-07-23 11:01:00","speaker":"agent","message":"Hello!We're thrilled to hear from you.How has your experience been with the Sony Bravia X900H TV?"},
        {"datetime":"2024-07-23 11:02:00","speaker":"customer","message":"It's been incredible!The picture quality is stunning,and the 4K resolution makes everything look so sharp and clear.The smart features are also very responsive and easy to use."},
        {"datetime":"2024-07-23 11:04:00","speaker":"agent","message":"That's wonderful to hear!We're glad the Sony Bravia X900H TV is meeting your expectations.Is there anything specific you like the most about it?"},
        {"datetime":"2024-07-23 11:06:00","speaker":"customer","message":"I really love the motion handling and the overall picture quality.Watching sports and action movies is a real treat.The colors are vibrant,and the blacks are deep and rich."},
        {"datetime":"2024-07-23 11:08:00","speaker":"agent","message":"Thank you for sharing your positive feedback!We're always happy to hear that our customers are satisfied with their purchases.If you ever need any assistance or have questions about your TV,feel free to reach out."},
        {"datetime":"2024-07-23 11:10:00","speaker":"customer","message":"Will do!Thanks for the excellent service and the amazing product."},
        {"datetime":"2024-07-23 11:12:00","speaker":"agent","message":"You're welcome!Enjoy your new TV and have a great day!"}
    ]}
]
'''

with open('transcript.json') as f:
    dataFromFile = json.load(f)

print(dataFromFile)

expected_format = '''{"products":[{"name":"Acer Nitro 5","category":"Laptop","issues":[{"date":"2024-07-03","issue":"Customer inquired about a suitable laptop for work and gaming. Recommendation was provided."}]}]}'''

data = json.loads(json_data)

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
            "content": json_data
        }
    ],
    temperature=0.5,
    max_tokens=600,
    top_p=1
)

print(response.choices[0].message.content)