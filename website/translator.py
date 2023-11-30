import requests

en2tok_URL = "https://api-inference.huggingface.co/models/plgrm720/eng_to_tokipona_model_v1"
tok2en_URL = "https://api-inference.huggingface.co/models/plgrm720/tokipona_to_eng_model_v1"
headers = {"Authorization": "Bearer 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"}

def query(api,payload):
	response = requests.post(api, headers=headers, json=payload)
	return response.json()

def translate(text, target_language) -> str:
	if False:
		text = text.lower().replace('a', '').replace('an', '').replace('the', '').replace('  ', ' ')
		output = query(en2tok_URL, {
			"inputs": text,
			"options": {
				"wait_for_model": True
			}
		})[0]['generated_text']

	else:
		output = query(tok2en_URL, {
			"inputs": text,
			"options": {
				"wait_for_model": True
			}
		})[0]['generated_text']

	return output