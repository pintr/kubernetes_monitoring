import os
from kubernetes import client, config


def get_k8s_core_client():
    d = os.path.dirname(__file__)
    cfg = os.path.join(d, 'cfg/config')
    config.load_kube_config(cfg)
    client.ApiClient()
    return client.CoreV1Api()



