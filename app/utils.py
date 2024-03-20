import cloudpickle
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def load_conversational_chain(chain_path):
    with open(chain_path, 'rb') as f:
        chain = cloudpickle.load(f)
    return chain

def perform_inference(chain, question):
    return chain({"question": question})