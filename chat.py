import openai

openai.api_key = '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'

response = openai.Completion.create(
    engine = 'text-davinci-003',
    prompt = 'Quien descubrío america?',
    max_tokens = 100,
    temperature = 0.9,
    top_p = 1,
    n = 1
)
print(response.choices[0].text)