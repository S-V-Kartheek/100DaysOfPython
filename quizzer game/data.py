# questions can be generated from open trivia database
import requests

parameters={
    "amount":10,
    "type":"boolean",
    "category":18
}
responce=requests.get(url="https://opentdb.com/api.php",params=parameters)
responce.raise_for_status()
question_data=responce.json()["results"]








# question_data = [
#     {"text": "The Indian government has announced a $10 billion incentive program for semiconductor manufacturing.", "answer": "True"},
#     {"text": "OpenAI's GPT-4 Turbo is claimed to be cheaper and faster than GPT-4.", "answer": "True"},
#     {"text": "Samsung's latest Exynos processor is more powerful than Apple's M3 chip.", "answer": "False"},
#     {"text": "Apple Vision Pro, the company's first mixed reality headset, runs on iOS.", "answer": "False"},
#     {"text": "Tesla's Optimus humanoid robot is expected to replace most factory workers by 2025.", "answer": "False"},
#     {"text": "Microsoft's $68.7 billion acquisition of Activision Blizzard was the largest tech acquisition in history.", "answer": "True"},
#     {"text": "Google’s AI model 'Gemini' was developed after the merger of DeepMind and Google Brain.", "answer": "True"},
#     {"text": "Amazon’s AI-powered cashier-less stores are called 'Just Walk Out' technology.", "answer": "True"},
#     {"text": "Meta's new AI language model, Llama 3, is expected to outperform GPT-4.", "answer": "False"},
#     {"text": "The EU fined Apple over $10 billion for anti-competitive behavior in the App Store.", "answer": "False"},
#     {"text": "NVIDIA's AI-powered GPUs dominate the data center market, with a market share of over 80%.", "answer": "True"},
#     {"text": "SpaceX's Starlink project aims to provide high-speed internet globally using over 50,000 satellites.", "answer": "False"}
# ]

