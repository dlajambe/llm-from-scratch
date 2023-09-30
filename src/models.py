import torch
import torch.nn as nn
import torch.nn.functional as F

class BiGramModel(nn.Module):
    def __init__(self, vocab_size):
        super(BiGramModel, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, vocab_size)

    def forward(self, X: torch.Tensor) -> None:
        logits = self.embeddings(X)
        print(logits.shape)
        n_samples, sample_length, vocab_size = logits.shape

        # Reshaping in this way gives the embeddings for all characters
        # received in X
        logits = logits.view(n_samples*sample_length, vocab_size)

        return logits
    
    def generate(self, idx, output_length):
        output = [idx]
        for i in range(output_length):
            output.append(self.forward())

    def calc_loss(self, logits: torch.Tensor, targets: torch.Tensor) -> float:
        pass

    def train(self, X: torch.Tensor, y: torch.Tensor) -> None:
        pass

    def predict(self) -> torch.Tensor:
        pass

class CharModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(CharModel, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.hidden_1 = nn.Linear(embedding_dim, 500)
        self.hidden_2 = nn.Linear(500, 500)
        self.output = nn.Linear(500, vocab_size)

    def forward(self, X: torch.Tensor) -> None:
        pass
    
    def generate(self, idx, output_length):
        pass

    def calc_loss(self, logits: torch.Tensor, targets: torch.Tensor) -> float:
        pass

    def train(self, X: torch.Tensor, y: torch.Tensor) -> None:
        pass

    def predict(self) -> torch.Tensor:
        pass