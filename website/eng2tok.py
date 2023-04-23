# from huggingface_hub import notebook_login

# notebook_login()

from transformers import pipeline
# text = input()
translator = pipeline("translation", model="plgrm720/tokipona_model_v0.2")
print("Model set up.")

def translate(text="bad") -> str:
    # print(text)
    return translator(text)[0]["translation_text"]