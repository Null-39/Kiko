# Kiko

Software:

Operating System: Compatible with any platform that supports Python 3.x
Python Version: 3.x
Required Libraries: openai (v0.2.6 or above), textblob (v0.18.3 or above)
API: OpenAI API key

Functionality:

Advanced chatbot interface for conversing with a "hikikomori nekomimi" named Kiko
Precision sentiment analysis using TextBlob's polarity function with a range between -1 and 1 and a resolution of 0.1
Adjustable tone of Kiko's response based on sentiment analysis with a threshold of 0, where sentiments above 0 are considered positive, sentiments below 0 are considered negative, and sentiments equal to 0 are considered neutral
Utilizes OpenAI's cutting-edge "text-davinci-003" engine to generate responses with a maximum token count of 1024 and a temperature setting of 0.5 for added naturalness and diversity of responses
Dynamic sliding window conversation history for both user input and Kiko's responses with a maximum size of 1, allowing for a seamless conversation flow and maintaining context
Clear conversation history feature and start a new conversation with just one command
Intuitive time delay of 0.1 seconds between characters when printing out Kiko's response, adding an element of realism to the conversation for enhanced user experience.
The code contains 1 while loop, 19 if-else statements, 2 try-except blocks, several variables and lists, 6 string formatting and several string and list operations.
Code lines: around 100 lines
Characters used in the program: around 2000 characters.
