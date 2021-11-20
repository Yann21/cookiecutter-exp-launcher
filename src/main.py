#%%
from pyforest import *

# Prepare dataset
iris = sklearn.datasets.load_iris()
X = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=42)
dtrain = xgb.DMatrix(x_train, y_train)
dtest = xgb.DMatrix(x_test, y_test)

# %%
param = {
  "max_depth": 3,
  "eta": 0.3,
  "objective": "multi:softprob",
  "num_class": 3,
  "eval_metric": "mlogloss"
}
num_round = 20

# Evaluate parameters
def score_model(params):
  bst = xgb.train(params, dtrain, num_round)
  y_pred = bst.predict(dtest).argmax(axis=1)
  return metrics.precision_score(y_test, y_pred, average="macro")

score_model(param)