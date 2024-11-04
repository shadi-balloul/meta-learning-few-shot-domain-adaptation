import logging
from .base_config import base_config, get_config

new_config = {
    'trainer' : 'maml',
    'n_domains' : 5,
    'valid_freq': 5,
    'valid_chunks':4,       #### validation/test data will be chunked into this many batches to fit in memory
    'fast_weight_lr' : 5e-5,
    'meta_lr' : 5e-5, ###### default 5e-5
    'collapse_domains' : False,
    'exp_name': 'maml_train_mbert_arabic_04-11-2024',
    'episodes': 500,
    'val_episodes':5,
    'test_episodes':1,
    'domain_sampling_strategy' : "uniform",
    'inner_gd_steps': 3,
    'unfreeze_layers': (10, 11),
    'num_examples' : 3500,
    'seed':40,
    'train_domains':  ['tead', 'tsac', 'att', 'res1', 'hard', 'astd', 'arsas', 'mov', 'htl', 'res2', 'bard'],
    'val_domains': ['labr'],
    'test_domains': ['prod'],
    'sort_test_by_pmi' : True,
    'k_shot': 5
}

config = get_config(base_config, new_config)