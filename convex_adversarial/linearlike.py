# A linear like 
import torch
import torch.nn.functional


# Linear like layer
class LinearLikeLayer(torch.nn.Module):

    def __init__(self):
        super(LinearLikeLayer, self).__init__()

    def getWeight(self):
        raise Exception("Not implemented")
        
    def getBias(self):
        raise Exception("Not implemented")
        
    def forward(self, input):
        return torch.nn.functional.linear(input, self.getWeight(), self.getBias())




class SplitNetwork(torch.nn.Module):
    
    def __init__(self, partA, partB, factors):
        super(SplitNetwork, self).__init__()
        self.moduleA = partA
        self.moduleB = partB
        self.factors = factors
        
    def forward(self, input):
        
        parts = input.split(self.factors,dim=1)
        outA = self.moduleA(parts[0])
        outB = self.moduleB(parts[1])
        return torch.cat((outA,outB),dim=1)

