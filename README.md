# Computer Use Demo

This repo is for showing Upsonic computer use capabilities.


## Installation - Client

Creating venv and installing requirements.

```console
uv venv
uv sync
```

## Installation - Docker Server

```console
docker pull upsonic/server:v0.55.5
```





## Running


### 1) Run the Docker Server

```console
docker run -d --name upsonic-server -p 5901:5901 -p 7541:7541 upsonic/server:v0.55.5
```

### 2) Connect Over VNC Viewer

Open a VNC viewer and connect to `localhost:5901`


#### 3) Run the client script

```console
uv run client.py
```