import sys

sys.path.append("toolkit/")
from usage_example import sample_regexes_usage
import pandas as pd
from prepare_regex_data import match_spec_example


def load_data_from_path(data_path):
    df = pd.read_csv(data_path, sep="\t")
    return df


if __name__ == "__main__":
    data_path = "data/raw/teste.tsv"
    df = load_data_from_path(data_path)
    dicts = df.to_dict("records")
    for d in dicts:
        regex_str = d["regex"]
        pos_example = d["pos_examples"].split(" ")
        neg_example = d["neg_examples"].split(" ")
        print("pos", [match_spec_example(regex_str, p) for p in pos_example])
        print("neg", [match_spec_example(regex_str, n) for n in neg_example])
        input()

    # regex = build_func_from_str(regex_str)
    # print(regex)
    # print(df.head())
