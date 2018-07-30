# A linear like 
import torch
import torch.nn.functional


# Linear like layer
class LinearLikeLayer(torch.nn.Module):

    def __init__(self, in_features, out_features):
        self.in_features = in_features
        self.out_features = out_features
        super(LinearLikeLayer, self).__init__()

    def getWeight(self):
        raise Exception("Not implemented")
        
    def getBias(self):
        raise Exception("Not implemented")
        
    def forward(self, input):
        return torch.nn.functional.linear(input, self.getWeight(), self.getBias())



