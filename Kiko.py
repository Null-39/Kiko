import textblob
import openai
import time

openai.api_key = "YOUR-API"

prev_conversation = []  # user's inputs
prev_responses = []  # Kiko's responses
prev_conversation_size = 1  # size of sliding window for both inputs and responses
topic = ""
is_first_prompt = True

while True:
    prompt = input(' > ')

    if prompt == "":
        print("Error: Please enter a prompt.")
        continue
    elif prompt == 'exit':
        break
    elif prompt == '~':
        topic = ""
        prev_conversation = []  # clear user's conversation history
        prev_responses = []  # clear Kiko's conversation history
        is_first_prompt = True
        print("\n<cleared>\n")
        continue
    elif is_first_prompt:
        is_first_prompt = False
    else:
        prev_conversation.append(prompt)  # add user's input to the conversation history
        if len(prev_conversation) > prev_conversation_size:
            prev_conversation.pop(0)  # remove the oldest user's input

    prev_prompt = ' '.join(prev_conversation)  # join user's inputs
    prev_responses_prompt = ' '.join(prev_responses)  # join kiko's inputs
    sentiment = textblob.TextBlob(prompt).sentiment.polarity
    if sentiment > 0:
        prefix = '[•‿•]'
    elif sentiment < 0:
        prefix = '[•︵•]'
    else:
        prefix = '[•_•]'
    if sentiment > 0:
        # user prompt is positive
        modified_prompt = f"Write a response to the following prompt from Kiko the hikikomori nekomimi's perspective with a happy tone: {prompt} {prev_prompt} {prev_responses_prompt} topic: {topic}"
    elif sentiment < 0:
        # user prompt is negative
        modified_prompt = f"Write a response to the following prompt from Kiko the hikikomori nekomimi's perspective with a sad tone: {prompt} {prev_prompt} {prev_responses_prompt} topic: {topic}"
    else:
        # user prompt is neutral
        modified_prompt = f"Write a response to the following prompt from Kiko the hikikomori nekomimi's perspective: {prompt} {prev_prompt} {prev_responses_prompt} topic: {topic}"    
    if prompt != '~':
        try:
            response = openai.Completion.create(engine='text-davinci-003', prompt=modified_prompt, max_tokens=1024, n=1, stop=None, temperature=0.5).choices[0].text.strip()
            print(f"\n < {prefix} ", end='')
            for char in response:
                print(char, end='', flush=True)
                time.sleep(0.1)
            print("\n")
            prev_responses.append(response)  # add Kiko's response to the conversation history
            if len(prev_responses) > prev_conversation_size:
                prev_responses.pop(0)  # remove the oldest Kiko's response
        except Exception as e:
            print(f"Error: {e}")
