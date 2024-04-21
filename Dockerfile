FROM quay.io/coreos/etcd:v3.5.0

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Set Python3 as the default Python version
RUN ln -s /usr/bin/python3 /usr/bin/python

# Upgrade pip and install required Python packages
RUN pip3 install --upgrade pip && \
    pip3 install etcd3 protobuf==3.20.1

