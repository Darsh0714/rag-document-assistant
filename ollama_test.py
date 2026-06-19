import ollama

response=ollama.chat(
    model="phi3:mini",
    messages=[
        {
            "role":"user",
            "content":"What is Retrival Augmented Generation?"
        }
    ]
)

print(response["message"]["content"])