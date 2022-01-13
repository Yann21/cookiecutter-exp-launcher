from sklearn.datasets import load_boston
from pyforest import *
import argparse
import wandb

# Inject Weights and biases parameters
parser = argparse.ArgumentParser()
parser.add_argument("--max_depth", default=None, type=int)
parser.add_argument("--eta", default=None, type=float)
parser.add_argument("--num_round", default=None, type=int)
parser.add_argument("--reg_lambda", default=None, type=float)
args = vars(parser.parse_args())

params = {
  "max_depth": args["max_depth"],
  "reg_lambda": args["reg_lambda"],
  "eta": args["eta"],
  "objective": "reg:linear",
}
num_round = args["num_round"]


################################################################################
# Begin section containing the experiment
################################################################################
# Prepare dataset
boston = load_boston()
X, y = boston.data, boston.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
dtrain = xgb.DMatrix(X_train, y_train)
dtest = xgb.DMatrix(X_test, y_test)

# Evaluate parameters
def score_model(params):
  bst = xgb.train(params, dtrain, num_round)
  y_pred = bst.predict(dtest)
  return metrics.mean_squared_error(y_pred, y_test)

################################################################################
# End of section
################################################################################


with wandb.init(
  config=params, 
  reinit=True, 
  project="{{cookiecutter.project_slug}}"
) as run:
  mse = score_model(params)
  # Send metrics to WandB
  wandb.log({"mse": mse})