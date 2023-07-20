import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer


def t5_headline(text):
    # Load the fine-tuned model
    # model_path = "model.pt"
    model_path = "model_headline/model.pt"
    model = T5ForConditionalGeneration.from_pretrained('t5-base')
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()

    # Initialize the tokenizer
    tokenizer = T5Tokenizer.from_pretrained('t5-base')

    # Define your input text
    input_text = "summarize:" + text

    # Tokenize the input text
    inputs = tokenizer.encode(input_text, return_tensors='pt', max_length=256, truncation=True)

    # Generate the summary
    summary_ids = model.generate(inputs, max_length=25, num_beams=1)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    file_path = 'media/headline.txt'

    # Open the file in write mode and save the summary
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(summary)

    print(f'Headline saved to: {file_path}')

    return summary

