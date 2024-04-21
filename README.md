Sure, here's a template for your README file:

---

# ETCD Cluster Setup and Testing

## Overview

This project demonstrates setting up a simple ETCD cluster using Docker containers and testing key-value operations across the nodes. The cluster consists of three nodes (`etcd-node1`, `etcd-node2`, `etcd-node3`) configured to communicate with each other.

## Prerequisites

- Docker installed on your system.
- Basic understanding of Docker and ETCD.
- Python 3 installed locally (for running the tests).

## Setup Instructions

1. Clone this repository to your local machine.

2. Ensure Docker is running, and the Docker daemon is accessible.

3. Navigate to the project directory in your terminal.

4. Run the following commands to set up the ETCD cluster:

    ```bash
    sudo docker network create etcd-network
    ```

    ```bash
    sudo docker run -d --net etcd-network --name etcd-node1 \
       -p 12379:2379 -p 12380:2380 \
       -e ETCD_DATA_DIR="/etcd-data" \
       -e ETCD_NAME="node1" \
       -e ETCD_INITIAL_ADVERTISE_PEER_URLS="http://etcd-node1:2380" \
       -e ETCD_LISTEN_PEER_URLS="http://0.0.0.0:2380" \
       -e ETCD_LISTEN_CLIENT_URLS="http://0.0.0.0:2379" \
       -e ETCD_ADVERTISE_CLIENT_URLS="http://etcd-node1:2379" \
       -e ETCD_INITIAL_CLUSTER="node1=http://etcd-node1:2380,node2=http://etcd-node2:2380,node3=http://etcd-node3:2380" \
       -e ETCD_INITIAL_CLUSTER_STATE="new" \
       -e ETCD_INITIAL_CLUSTER_TOKEN="etcd-cluster-1" \
       etcd-python
    ```

    ```bash
    sudo docker run -d --net etcd-network --name etcd-node2 \
       -p 22379:2379 -p 22380:2380 \
       -e ETCD_DATA_DIR="/etcd-data" \
       -e ETCD_NAME="node2" \
       -e ETCD_INITIAL_ADVERTISE_PEER_URLS="http://etcd-node2:2380" \
       -e ETCD_LISTEN_PEER_URLS="http://0.0.0.0:2380" \
       -e ETCD_LISTEN_CLIENT_URLS="http://0.0.0.0:2379" \
       -e ETCD_ADVERTISE_CLIENT_URLS="http://etcd-node2:2379" \
       -e ETCD_INITIAL_CLUSTER="node1=http://etcd-node1:2380,node2=http://etcd-node2:2380,node3=http://etcd-node3:2380" \
       -e ETCD_INITIAL_CLUSTER_STATE="new" \
       -e ETCD_INITIAL_CLUSTER_TOKEN="etcd-cluster-1" \
       etcd-python
    ```

    ```bash
    sudo docker run -d --net etcd-network --name etcd-node3 \
       -p 32379:2379 -p 32380:2380 \
       -e ETCD_DATA_DIR="/etcd-data" \
       -e ETCD_NAME="node3" \
       -e ETCD_INITIAL_ADVERTISE_PEER_URLS="http://etcd-node3:2380" \
       -e ETCD_LISTEN_PEER_URLS="http://0.0.0.0:2380" \
       -e ETCD_LISTEN_CLIENT_URLS="http://0.0.0.0:2379" \
       -e ETCD_ADVERTISE_CLIENT_URLS="http://etcd-node3:2379" \
       -e ETCD_INITIAL_CLUSTER="node1=http://etcd-node1:2380,node2=http://etcd-node2:2380,node3=http://etcd-node3:2380" \
       -e ETCD_INITIAL_CLUSTER_STATE="new" \
       -e ETCD_INITIAL_CLUSTER_TOKEN="etcd-cluster-1" \
       etcd-python
    ```

5. Once the containers are running, you can interact with the cluster using the provided Python scripts.

## Usage

- To list all keys: `sudo docker exec -it etcd-node1 python /week1_code.py`
- To get the value for a specific key: `sudo docker exec -it etcd-node1 python /week1_code.py`
- To put a new key-value pair: `sudo docker exec -it etcd-node1 python /week1_code.py`
- To run unit tests: `sudo docker exec -it etcd-node3 python /week3_unit_tests.py`

## Cleanup

To stop and remove the Docker containers:

```bash
sudo docker stop etcd-node1 etcd-node2 etcd-node3
sudo docker rm etcd-node1 etcd-node2 etcd-node3
```

## Notes

- Make sure to adjust the container names, ports, and environment variables according to your setup.
- The provided Python scripts assume a specific ETCD setup. Modify them as needed for your environment.

---

