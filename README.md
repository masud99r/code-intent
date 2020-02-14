# Code Intent Analysis

## Requirements
 -  Python 2.7
 
 ## Get Started
 
 ```
 git clone https://github.com/masud99r/code-intent.git
 cd code-intent
 python codeintent.py
 ```
 
 ## Details
 
 `codeness()` method takes a sentence(query) as input and returns it's codescore. 
 Some sample queries can be found in the method `samplecodeness()`
 
 
 A length-normalized version of the code intent is given in `codeness_norm()`. It takes a sentence(query) as input and returns it's codescore normalized by sentence length.

For more details please refer to our MSR 2018 paper: [Evaluating How Developers Use General-Purpose Web-Search
for Code Retrieval](https://arxiv.org/abs/1803.08612)


## Citation
If you use this code or data, please consider citing this paper:

```
@inproceedings{rahman2018evaluating,
 author = {Rahman, Md Masudur and Barson, Jed and Paul, Sydney and Kayani, Joshua and Lois, Federico Andr{\'e}s and Quezada, Sebasti\'{a}n Fernandez and Parnin, Christopher and Stolee, Kathryn T. and Ray, Baishakhi},
 title = {Evaluating How Developers Use General-purpose Web-search for Code Retrieval},
 booktitle = {Proceedings of the 15th International Conference on Mining Software Repositories},
 year = {2018},
 publisher = {ACM}
} 
```
