from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
key=os.getenv("API_KEY")

client = Groq(api_key=key)
completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "what are all questions that i asked prepiviously ?"
        }
    ],
    temperature=1.4,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")



# completion = client.chat.completions.create(
#     model="llama-3.1-70b-versatile",
#     messages=[
#         {
#             "role": "user",
#             "content": "what are questions that iasked previously?"
#         }
#     ],
#     temperature=1,
#     max_tokens=1024,
#     top_p=1,
#     stream=True,
#     stop=None,
# )

# for chunk in completion:
#     print(chunk.choices[0].delta.content or "", end="")
