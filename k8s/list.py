from k8s.connect import get_k8s_core_client
from pprint import pprint


def pods(k8s):
    print("Listing pods:")
    all_pods = k8s.list_pod_for_all_namespaces(pretty=True, watch=False)

    # pprint(all_pods)
    for i in all_pods.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


def test(k8s):
    nodes(k8s)

    k8s = get_k8s_core_client()


def nodes(k8s):
    print("Listing pods:")
    all_nodes = k8s.list_node(pretty=True, watch=False)

    pprint(all_nodes)
    # for i in all_nodes.items:
    #     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
