import torch
from torch.utils.data import Dataset
import numpy as np


class MutationsDataset(Dataset):

    def __init__(self, df):
        self.df = df.reset_index(drop=True)

    def __len__(self):
        return len(self.df)

    def __getitem__(self, index):
        sample = self.df.iloc[index]
        data = {}
        data['netSurfP_before_local'] = torch.tensor(sample['netSurfP_before_local'], dtype=torch.float32)
        data['netSurfP_after_local'] = torch.tensor(sample['netSurfP_after_local'], dtype=torch.float32)

        data['netSurfP_before_global'] = torch.tensor(np.array(sample['netSurfP_before_global']).reshape(9, 16),
                                                      dtype=torch.float32)
        data['netSurfP_after_global'] = torch.tensor(np.array(sample['netSurfP_after_global']).reshape(9, 16),
                                                     dtype=torch.float32)

        data['ESM_Point_before'] = torch.tensor(sample['ESM_Point_before'], dtype=torch.float32)
        data['ESM_Point_after'] = torch.tensor(sample['ESM_Point_after'], dtype=torch.float32)
        data['ESM_Seq_before'] = torch.tensor(sample['ESM_Seq_before'], dtype=torch.float32)
        data['ESM_Seq_after'] = torch.tensor(sample['ESM_Seq_after'], dtype=torch.float32)
        data['T5_Point_before'] = torch.tensor(sample['T5_Point_before'], dtype=torch.float32)
        data['T5_Point_after'] = torch.tensor(sample['T5_Point_after'], dtype=torch.float32)
        data['T5_Seq_before'] = torch.tensor(sample['T5_Seq_before'], dtype=torch.float32)
        data['T5_Seq_after'] = torch.tensor(sample['T5_Seq_after'], dtype=torch.float32)

        label = int(sample['stab_label'])
        data['label'] = torch.tensor(label, dtype=torch.long)
        return data
