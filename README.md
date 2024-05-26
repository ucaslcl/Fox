<h3><a href="https://github.com/ucaslcl/Fox/blob/main/Fox_paper.pdf">Fox: Focus Anywhere for Fine-grained Multi-page Document Understanding</a></h3>
<a href="https://arxiv.org/abs/2405.14295"><img src="https://img.shields.io/badge/Paper-PDF-orange"></a> 
<a href="https://ucaslcl.github.io/foxhome/"><img src="https://img.shields.io/badge/Project-Page-Green"></a>
<!-- <a href='https://huggingface.co/kppkkp/OneChart/tree/main'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Models-blue'></a> -->
<a href="https://zhuanlan.zhihu.com/p/699450474"><img src="https://img.shields.io/badge/zhihu-yellow"></a> 

Chenglong Liu, [Haoran Wei](https://scholar.google.com/citations?user=J4naK0MAAAAJ&hl=en), Jinyue Chen, Lingyu Kong, [Zheng Ge](https://joker316701882.github.io/), Liang Zhao, [Jianjian Sun](https://scholar.google.com/citations?user=MVZrGkYAAAAJ&hl=en), Chunrui Han, [Xiangyu Zhang](https://scholar.google.com/citations?user=yuB-cfoAAAAJ&hl=en)
	


<p align="center">
<img src="assets/Fox.png" style="width: 150px" align=center>
</p>

## Release
- [2024/5/26] 🔥 We have released the fine-grained benchmark [data]() to test the focusing capabilities of LVLM on dense PDF documents. 


## Contents
- [1. Benchmark Data and Evaluation Tool](#1-benchmark-data-and-evaluation-tool)

<p align="center">
<img src="assets/append_all.png" style="width: 700px" align=center>
</p>

## 1. Benchmark Data and Evaluation Tool
- Download the images and jsons [here](). 
- Modify json path at the beginning of `_eval/eval_.py`. Then run eval script:
   
```shell
python _eval/eval_.py
```


## Acknowledgement
- [Vary](https://github.com/Ucas-HaoranWei/Vary): the codebase and initial weights we built upon!

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/tatsu-lab/stanford_alpaca/blob/main/LICENSE)
[![Data License](https://img.shields.io/badge/Data%20License-CC%20By%20NC%204.0-red.svg)](https://github.com/tatsu-lab/stanford_alpaca/blob/main/DATA_LICENSE)

**Usage and License Notices**: The data, code, and checkpoint are intended and licensed for research use only. They are also restricted to use that follow the license agreement of Vary, Opt. 


## Citation
If you find our work useful in your research, please consider citing Fox:
```bibtex
@article{liu2024focus,
  title={Focus Anywhere for Fine-grained Multi-page Document Understanding},
  author={Liu, Chenglong and Wei, Haoran and Chen, Jinyue and Kong, Lingyu and Ge, Zheng and Zhu, Zining and Zhao, Liang and Sun, Jianjian and Han, Chunrui and Zhang, Xiangyu},
  journal={arXiv preprint arXiv:2405.14295},
  year={2024}
}
```
