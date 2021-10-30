# Instructions
Install minikube

`minikube start`

`helm repo add dask https://helm.dask.org/`   
`helm repo update`     
`helm install my-dask dask/dask -f config.yaml`

`minikube kubectl -- port-forward svc/my-dask-jupyter 8000:80`

Browse to [localhost](http://localhost:8000) after waiting for the containers to spin up and the libraries to install.

Copy [train.py](./train.py) into a notebook cell.  Run the cell to see it work!

To upgrade:

`helm upgrade my-dask dask/dask -f config.yaml`

Cleanup:

`minikube delete`