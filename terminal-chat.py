#You will need to install the openai module
import openai

#You will need an api key from openai to run this code
openai.api_key = "<insert your openai api key here>"
#Note: api keys are chargable and you need to get it from openai

messages = []
inputer = 'Your role is that of a personal assistant'
triker = '...end'

def get_completion(prompt, model = "gpt-3.5-turbo"):
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0,
    )
    return response.choices[0].message["content"]

messages.append({"role": "system", "content": inputer})

print("\n\n Welcome to TERMINAL CHAT")
print(" Interact with ChatGPT 3.5\n")
print(" Instructions:\n - Type your question and click enter\n - ChatGPT will give its answer\n - To end chat type '...end' in lowercase\n")
print(" Ask your question:")

while inputer != '...end':
    inputer = input(" >>>  ")
    prompt = inputer
    response = get_completion(prompt)
    messages.append({"role": "assistant", "content": response})
    print("\n ",response,"\n")
