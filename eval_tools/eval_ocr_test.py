import json
import argparse
import nltk
from nltk.metrics import precision, recall, f_measure
import numpy as np
import jieba
import re
from nltk.translate import meteor_score


def contain_chinese_string(text):
    chinese_pattern = re.compile(r'[\u4e00-\u9fa5]')
    return bool(chinese_pattern.search(text))

def cal_per_metrics(predict_root_, pred, gt):

    metrics = {}

    if contain_chinese_string(gt) or contain_chinese_string(pred):
        reference = jieba.lcut(gt)
        hypothesis = jieba.lcut(pred)
    else:
        reference = gt.split()
        hypothesis = pred.split()

    metrics["bleu"] = nltk.translate.bleu([reference], hypothesis)
    metrics["meteor"] = meteor_score.meteor_score([reference], hypothesis)

    reference = set(reference)
    hypothesis = set(hypothesis)
    metrics["f_measure"] = f_measure(reference, hypothesis)

    metrics["precision"] = precision(reference, hypothesis)
    metrics["recall"] = recall(reference, hypothesis)
    metrics["edit_dist"] = nltk.edit_distance(pred, gt) / max(len(pred), len(gt))
    return metrics

def doc_text_eval(predict_root_):

    predicts = json.load(open(predict_root_, encoding='utf-8'))
    
    result = []
    for ann in predicts:
        ans = cal_per_metrics(predict_root_, ann["label"], ann["answer"])
        result.append(ans)

    mean_dict = {}

    mean_dict["eval question num"] = len(result)
    for k, v in result[0].items():
        mean_dict[k] = 0
    
    for each in result:
        for k, v in each.items():
            mean_dict[k] += v

    for k, v in mean_dict.items():
        if k == "eval question num":
            continue
        mean_dict[k] /= len(result)
    print(json.dumps(mean_dict, indent=4))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--out_file", type=str, required=True)
    args = parser.parse_args()
    doc_text_eval(args.out_file)