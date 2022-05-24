from model import PromptOptim, CrossPromptOptim
from config import cfg
import argparse
import torch

if __name__ == '__main__':
    torch.manual_seed(2022)
    device = torch.device('cpu')
    parser = argparse.ArgumentParser(description = 'training settings')
    parser.add_argument('--device', required=True, type=str)
    parser.add_argument('--dataset', required=True, help='dataset name', type=str)
    parser.add_argument('--type', required=True, default='text', type=str)
    parser.add_argument('--kshot', required=True, type=int)
    parser.add_argument('--start_epoch', required=True, type=int)
    args = parser.parse_args()

    proptim = CrossPromptOptim(cfg, args.device, args.dataset, args.kshot, args.type , args.start_epoch)
    proptim.train()