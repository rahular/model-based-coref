# model-based-coref

This repository contains the data presented in "Model-based annotation of coreference" (link coming soon).

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
