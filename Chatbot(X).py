from openai import OpenAI
client = OpenAI()

question = input("Ask a question: ")
response = client.chat.completions.create(
    model="gpt-4o-mini",
    input=question
)

print("AI:", response.choices[0].message)