import argparse
from .data_pull import DataPull
from .carbon_ai import CarbonAI
import logging

def main():
    # handle arguments from command line
    my_parser = argparse.ArgumentParser(description='cli for carbon_ai')
    my_parser.add_argument('ai_action', type=str, help = 'data_pull or train or predict')
    args = my_parser.parse_args()

    # run ai/data_pull program
    data_pull = DataPull()
    carbon_ai = CarbonAI()
    if args.ai_action == 'train':
        carbon_ai.train()
    elif args.ai_action == 'predict':
        carbon_ai.predict()
    elif args.ai_action == 'data_pull':
        data_pull.main()
    else:
        logging.error('invalid ai_action input: choose "train", "data_pull" or "predict"')

main()