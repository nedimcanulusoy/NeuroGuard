from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast
import torch

def dbert():
    state_dict = torch.load("/app/ng_models/model_checkpoint.pth",map_location=torch.device('cpu'))

    model_weights = state_dict["model_state_dict"]

    model = DistilBertForSequenceClassification.from_pretrained(
        'distilbert-base-uncased',
        num_labels=2  #output_dim value
    )
    model.load_state_dict(model_weights)
    model.eval()

    tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')

    return model, tokenizer
