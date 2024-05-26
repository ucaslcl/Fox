import json
import argparse

def cal_per_metrics(predict_root_, pred, gt):
    metrics = {}
    if pred == gt:
        return 1
    else:
        return 0

def doc_text_eval(predict_root_):

    predicts = json.load(open(predict_root_, encoding='utf-8'))
    
    result = []
    for ann in predicts:
        ans = cal_per_metrics(predict_root_, ann["label"], ann["answer"])
        result.append(ans)
    
    mean_dict = {}

    sum_true = 0
    for ans_p in result:
        sum_true += ans_p

    mean_dict["eval question num"] = len(result)
    mean_dict["total question num"] = len(predicts)
    mean_dict["true_num"] = sum_true
    mean_dict["accuracy"] = sum_true / len(predicts)

    print(json.dumps(mean_dict, indent=4))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--out_file", type=str, required=True)
    args = parser.parse_args()
    doc_text_eval(args.out_file)