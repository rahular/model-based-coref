# model-based-coref

This repository contains the data presented in "Model-based annotation of coreference" ([arXiv](https://arxiv.org/abs/1906.10724)).

### Directory structure
- `data` contains the annotated data in JSON format
- `output` contains the results of the three coreference resolvers mentioned in Table 1 of the paper

### Data format
```
"<id>": {
  "title": "title-of-the-document",
  "entities": [{ "ent_name": "some-entity", "ent_id": "wikidata-id-if-present" }, ...],
  "qas": { "qnum": { "question": "...", "answer": "..." }, ... },
  "a1": {
    "para_ann": [[ "mention-index", "mention-phrase", "antecedent" ], ...],
    "q_ann": { "qnum": [[ "mention-index", "mention-phrase", "antecedent" ], ...], ... }
  },
  "a2": { ... }
}
```

`qas`, `q_ann` fields are empty in `wiki-*.json`. `a2` is empty for singly annotated documents.

Run `check_agreement.py <data-file-path>` to get the inter-annotator agreement scores.

### Citation
```
@article{DBLP:journals/corr/abs-1906-10724,
  author    = {Rahul Aralikatte and
               Anders S{\o}gaard},
  title     = {Model-based annotation of coreference},
  journal   = {CoRR},
  volume    = {abs/1906.10724},
  year      = {2019},
  url       = {http://arxiv.org/abs/1906.10724},
  archivePrefix = {arXiv},
  eprint    = {1906.10724},
  timestamp = {Thu, 27 Jun 2019 18:54:51 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1906-10724},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
