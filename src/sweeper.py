import wandb
import argparse
from voc_utils import voc_utils as ut
import subprocess
from pathlib import Path

git_root = Path(__file__).parent / ".."

parser = argparse.ArgumentParser()
parser.add_argument("--tree_method", default=None, type=str)
parser.add_argument("--eta", default=None, type=float)
parser.add_argument("--reg_lambda", default=None, type=float)
parser.add_argument("--gamma", default=None, type=float)
parser.add_argument("--max_depth", default=None, type=int)
parser.add_argument("--n_estimators", default=None, type=int)
parser.add_argument("--window_size", default=None, type=int)
parser.add_argument("--feature_exclude", default=None, type=str)
parser.add_argument("--model", default=None, type=str)
parser.add_argument("--feature_flags", default=None, type=str)
parser.add_argument("--mw1", default=None, type=float)
parser.add_argument("--mw2", default=None, type=float)
parser.add_argument("--ar", default=None, type=int)
parser.add_argument("--bootstrap", default=None, type=int)
parser.add_argument("--early_stopping_rounds", default=None, type=int)
parser.add_argument("--bootstrap_splits", default=None, type=int)
parser.add_argument("--cum_pred", default=None, type=int)


args = vars(parser.parse_args())
yaml_cfg = ut.load_config(git_root)

model = args["model"].split(" ")
if args["feature_exclude"] != "":
  feature_exclude = args["feature_exclude"].split(" ")
else:
  feature_exclude = []
if args["feature_flags"] != "":
  feature_flags = args["feature_flags"].split(" ")
else:
  feature_flags = []

args["feature_exclude"] = ["prev_pred", "prev_prev_pred"]


def update_yaml(yaml_cfg):
  yaml_cfg.update(
    {
      "feature_exclude": args["feature_exclude"],
      "feature_flags": feature_flags,
      "bootstrap": args["bootstrap"],
      "ar": args["ar"],
      "early_stopping_rounds": args["early_stopping_rounds"],
      "bootstrap_splits": args["bootstrap_splits"],
      "cum_pred": args["cum_pred"],
      "params": {
        "max_depth": args["max_depth"],
        "n_estimators": args["n_estimators"],
        "window_size": args["window_size"],
        "gamma": args["gamma"],
        "eta": args["eta"],
        "reg_lambda": args["reg_lambda"],
        "tree_method": args["tree_method"],
        # "mw1": args["mw1"],
        # "mw2": args["mw2"],
      },
      "debug": False,
    }
  )

  ut.dump_config(yaml_cfg, git_root)


update_yaml(yaml_cfg)

subprocess.run(["dvc", "repro"])
subprocess.run(["python", "src/training.py"])

args["group"] = "void"
ut.dump_config(args, git_root)
