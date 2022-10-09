# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

#25/500 predicted correctly
#python ./src/london_baseline.py --eval_corpus_path birth_dev.tsv --outputs_path baseline_predictions
import argparse
import utils

argp = argparse.ArgumentParser()
argp.add_argument('--eval_corpus_path', help="Path of the corpus to evaluate on", default=None)
argp.add_argument('--outputs_path', default=None)
args = argp.parse_args()

assert args.eval_corpus_path is not None

def main():
    predictions = ["London"] * len(open(args.eval_corpus_path, encoding="utf-8").readlines())     #for each line in corpus, predict London
    #below code copied from run.py
    total, correct = utils.evaluate_places(args.eval_corpus_path, predictions)
    if total > 0:
        print('Correct: {} out of {}: {}%'.format(correct, total, correct / total * 100))
    else:
        print('Predictions written to {}; no targets provided'.format(args.outputs_path))

if __name__ == "__main__":
    main()