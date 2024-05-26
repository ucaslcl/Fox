import json
import argparse
import nltk
import jieba
import re
from rouge import Rouge

def cal_per_metrics(predict_root_, pred, gt):

    metrics = {}
    reference = gt.split()
    hypothesis = pred.split()
    reference = ' '.join(reference)
    hypothesis = ' '.join(hypothesis)
    rouge = Rouge()
    rouge_score = rouge.get_scores(hyps=hypothesis, refs=reference)

    return rouge_score

def doc_text_eval(predict_root_, ):

    predicts = json.load(open(predict_root_, encoding='utf-8'))
    
    result = []
    for ann in predicts[:]:
        ans = cal_per_metrics(predict_root_, ann["label"], ann["answer"])
        result.append(ans)
    
    mean_rl_dict = {'r': 0, 'p': 0, 'f': 0}

    for per_ans in result:
        rl_dict = per_ans[0]['rouge-l']

        mean_rl_dict['r'] += rl_dict['r']
        mean_rl_dict['p'] += rl_dict['p']
        mean_rl_dict['f'] += rl_dict['f']

    print("eval question num: ", len(result))

    for k, v in mean_rl_dict.items():
        mean_rl_dict[k] /= len(result)

    print('rouge-l: ', json.dumps(mean_rl_dict, indent=4))

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--out_file", type=str, required=True)
    args = parser.parse_args()
    doc_text_eval(args.out_file)