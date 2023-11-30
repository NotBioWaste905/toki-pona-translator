# from huggingface_hub import notebook_login

# notebook_login()

from transformers import T5Tokenizer, T5ForConditionalGeneration
# text = input()
en2tok_tokenizer = T5Tokenizer.from_pretrained("plgrm720/eng_to_tokipona_model_v1")
en2tok_model = T5ForConditionalGeneration.from_pretrained("plgrm720/eng_to_tokipona_model_v1")

tok2en_tokenizer = T5Tokenizer.from_pretrained("plgrm720/tokipona_to_eng_model_v1")
tok2en_model = T5ForConditionalGeneration.from_pretrained("plgrm720/tokipona_to_eng_model_v1")
# translator = pipeline("translation", model="plgrm720/tokipona_model_v0.2")
# en2tok_translator = pipeline("translation_en_to_tok", model="plgrm720/eng_to_tokipona_model_v1")
# tok2en_translator = pipeline("translation_tok_to_en", model="plgrm720/tokipona_to_eng_model_v1")

# en2tok_translator = pipeline("text2text-generation", model="plgrm720/eng_to_tokipona_model_v1")
# tok2en_translator = pipeline("text2text-generation", model="plgrm720/tokipona_to_eng_model_v1")

print("Model set up.")

def translate(text, target_language) -> str:
    # print(text)
    print(target_language)
    if target_language == "tokipona":
        return en2tok_translator(text)[0]["translation_text"]
    else:
        return tok2en_translator(text)[0]["translation_text"]
