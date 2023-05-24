import openai
import os
from settings import apiKey

os.environ["OPENAI_API_KEY"] = apiKey
# fp = "openAIdata_prepared.jsonl"
# openai.api_key = apiKey
# os.system(f"openai api fine_tunes.create -t {fp} -m ada")

# os.system("openai api fine_tunes.follow -i ft-Zd3wxFLHnboNAm1ZrH8HB7Zs")

os.system('openai api completions.create -m ada:ft-personal-2023-05-22-22-17-54 -p "what is 2x learning?"')