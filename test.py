import torch
from torch.utils.data import DataLoader
import pickle
from src.loaddata import MutationsDataset

from sklearn.metrics import (
    matthews_corrcoef, f1_score, confusion_matrix,
    precision_score, recall_score, roc_auc_score
)
from model import memostab2


device = torch.device('cuda:1' if torch.cuda.is_available() else 'cpu')
with open('data/test_stab.pkl', 'rb') as f:
    test_data = pickle.load(f)
kk_list = test_data['accession'].unique().tolist()
test_dataset = MutationsDataset(test_data)

test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

val_losses = []
val_accuracies = []
val_mccs = []
val_f1s = []
val_precisions = []
val_recalls = []
val_aucs = []
conf_matrix_values = []

memostab2_model = memostab2()
memostab2_model = memostab2_model.to(device)
memostab2_model.load_state_dict(torch.load('weight/memostab2.pth'))
supervised_model = memostab2_model.to(device)

supervised_model.eval()
correct_val = 0
total_val = 0
all_preds = []
all_labels = []
all_probs = []
all_embs = []
all_embs_before = []
all_embs_after = []

with torch.no_grad():
    for batch in test_loader:
        for key in batch:
            batch[key] = batch[key].to(device)
        labels = batch["label"].to(device)

        outputs = supervised_model(batch)
        _, predicted = torch.max(outputs, 1)
        total_val += labels.size(0)
        correct_val += (predicted == labels).sum().item()

        all_preds.extend(predicted.cpu().numpy())
        all_labels.extend(labels.cpu().numpy())
        all_probs.extend(torch.softmax(outputs, dim=1)[:, 1].cpu().numpy())

    val_acc = 100 * correct_val / total_val
    val_mcc = matthews_corrcoef(all_labels, all_preds)
    val_f1 = f1_score(all_labels, all_preds, average='binary')
    val_precision = precision_score(all_labels, all_preds, average='binary')
    val_recall = recall_score(all_labels, all_preds, average='binary')

    val_auc = roc_auc_score(all_labels, all_probs)

    conf_matrix = confusion_matrix(all_labels, all_preds)
    tn, fp, fn, tp = conf_matrix.ravel()

    print(
          f"Acc: {val_acc:.2f}%, "
          f"MCC: {val_mcc:.4f}, F1: {val_f1:.4f}, "
          f"Precision: {val_precision:.4f}, Recall: {val_recall:.4f}, "
          f"AUC: {val_auc:.4f}, Conf Matrix: TP={tp}, FP={fp}, TN={tn}, FN={fn}")
