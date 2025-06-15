import pickle
import pandas as pd

with open('features/all_feature_net_esm_t5.pkl', 'rb') as f:
    df_1 = pickle.load(f)

df_deduplicated = df_1.drop_duplicates(
    subset=['trimmed_sequence', 'mutatedType', 'new_mutation_index'],
    keep='first'
)

subset = ['trimmed_sequence', 'mutatedType', 'new_mutation_index']
with open('/data3/baoyh/Memo/feature/all_feature_net_esm_t5_deduplicated.pkl', 'rb') as f:
    df_train = pickle.load(f)

merged = df_deduplicated.merge(
    df_train[subset].drop_duplicates(),
    on=subset,
    how='left',
    indicator=True
)

df_deduplicated_filtered = merged[merged['_merge'] == 'left_only'].drop('_merge', axis=1)

df_deduplicated_filtered.to_pickle('features/preprocessed_dataset_final.pkl')


