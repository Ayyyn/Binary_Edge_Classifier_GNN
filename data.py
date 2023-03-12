from pathlib import Path
import torch
from torch.utils.data import Dataset

class MyDataset(Dataset):
    def __init__(self, data_dir):
        super().__init__()
        self.graph_files = list(Path(data_dir).rglob("*.pt"))
    
    def __getitem__(self, idx):
        graph_file = self.graph_files[idx]
        graph = torch.load(graph_file)
        return graph
    
    def __len__(self):
        return len(self.graph_files)

directory_path="./Dataset"
dataset = MyDataset(directory_path)

def interpret():
    print("Number of graphs in the dataset:", len(dataset))
    for i in range(5):
        print(dataset[i])
    for i in range(30,35):
        class_1,class_2=0,0
        for target in dataset[i]['y']:
            if target==0:
                class_1+=1
            else:
                class_2+=1
        print(f"0's: {round(class_1*100/len(dataset[i]['y']),3)}%    1's: {round(class_2*100/len(dataset[i]['y']),3)}% in graph {i}")

# interpret()