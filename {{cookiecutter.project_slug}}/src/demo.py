from pyforest import *
from sklearn.datasets import load_iris
import wandb
import argparse

# Inject Weights and biases parameters
parser = argparse.ArgumentParser()
parser.add_argument("--max_depth", default=None, type=int)
parser.add_argument("--eta", default=None, type=float)
parser.add_argument("--num_round", default=None, type=int)
parser.add_argument("--reg_lambda", default=None, type=float)
args = vars(parser.parse_args())

# Prepare dataset
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
dtrain = xgb.DMatrix(X_train, y_train)
dtest = xgb.DMatrix(X_test, y_test)

param = {
  "max_depth": args["max_depth"],
  "reg_lambda": args["reg_lambda"],
  "eta": args["eta"],
  "objective": "multi:softprob",
  "eval_metric": "mlogloss",
  "num_class": 3,
}
num_round = args["num_round"]

# Evaluate parameters
def score_model(params):
  bst = xgb.train(params, dtrain, num_round)
  y_pred = bst.predict(dtest).argmax(axis=1)
  return metrics.precision_score(y_test, y_pred, average="macro")

with wandb.init(config=param, reinit=True, project="{{cookiecutter.project_slug}}",
#  entity="changemeuser"
 ) as run:
  precision = score_model(param)
  wandb.log({"precision": precision})