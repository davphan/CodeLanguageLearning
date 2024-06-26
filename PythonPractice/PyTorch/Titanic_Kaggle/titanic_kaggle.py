import pandas as pd
from torch.utils.data import Dataset
import torch

class TitanicDataset(Dataset):
  def __init__(self, csvpath, mode = "train"):
    self.mode = mode
    df = pd.read_csv(csvpath)
    le = LabelEncoder()

    # data preprocessing
    if self.mode == "train":
      df = df.dropna()
      self.inp = df.iloc[:, 1:].values
      self.oup = df.iloc[:,0].values.reshape(891,1)
    else:
      self.inp = df.values
  def __len__(self):
    return len(self.inp)
  def __getitem__(self, idx):
    if self.mode == 'train':
      inpt  = torch.Tensor(self.inp[idx])
      oupt  = torch.Tensor(self.oup[idx])
      return { 'inp': inpt,
              'oup': oupt,
      }
    else:
      inpt = torch.Tensor(self.inp[idx])
      return { 'inp': inpt
      }

# initialize dataset
data = TitanicDataset("train.csv")
# load dataset
data_train = DataLoader(dataset = data, batch_size = BATCH_SIZE, shuffle=False)
