import xgboost as xgb
import dask.array as da
from dask.distributed import Client

client = Client()
client.get_versions(packages=["xgboost"], check=True)
# X and y must be Dask dataframes or arrays
num_obs = 1e5
num_features = 20
X = da.random.random(size=(num_obs, num_features), chunks=(1000, num_features))
y = da.random.random(size=(num_obs, 1), chunks=(1000, 1))

dtrain = xgb.dask.DaskDMatrix(client, X, y)

output = xgb.dask.train(
    client,
    {"verbosity": 2, "tree_method": "hist", "objective": "reg:squarederror"},
    dtrain,
    num_boost_round=4,
    evals=[(dtrain, "train")],
)
