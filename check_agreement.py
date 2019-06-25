import sys
import json
import toolz
import metrics


def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_ann(data):
    for key in data.keys():
        a1 = data[key].get('a1', None)
        a2 = data[key].get('a2', None)

        a1_ann, a2_ann = [], []
        if a1:
            a1_ann = [ann[2] for ann in toolz.unique(
                a1['para_ann'], key=lambda x: x[0])]
            a1_ann.extend([ann[2] for qno in a1['q_ann'].keys()
                           for ann in toolz.unique(a1['q_ann'][qno], key=lambda x: x[0])])
        if a2:
            a2_ann = [ann[2] for ann in toolz.unique(
                a2['para_ann'], key=lambda x: x[0])]
            a2_ann.extend([ann[2] for qno in a2['q_ann'].keys()
                           for ann in toolz.unique(a2['q_ann'][qno], key=lambda x: x[0])])

        yield a1_ann, a2_ann


def get_stats(data, ratio=100):
    count_1, count_2, total_a2 = 0, 0, 0
    exact_match, f1_score = 0, 0
    for a1, a2 in get_ann(data):
        total_a2 += len(a2)
        if not a2:
            count_1 += 1
        else:
            count_2 += 1
            assert len(a1) == len(a2), (a1, a2)
            em, f1 = metrics.evaluate(a1, a2)
            exact_match += em
            f1_score += f1
    return {
        'single-ann': count_1,
        'double-ann': count_2,
        'em': round(exact_match / total_a2, 2),
        'f1': round(f1_score / total_a2, 2)
    }


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Required: path of file to read...')
        sys.exit(0)
    data = read(sys.argv[1])
    print(json.dumps(get_stats(data), indent=2))
