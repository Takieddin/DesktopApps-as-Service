from kubernetes import client, config
from test.test_importlib.data03 import namespace

# config.load_kube_config()  # for local environment

# or
# config.load_incluster_config()
# v1 = client.CoreV1Api()
# t = v1.list_namespaced_service(namespace="argo-events")
# print('dd')
# print(t.items[0].metadata.name)
# print(type(t))


def create_service(name, nodePort, namespace="default"):
    config.load_kube_config()
    core_v1_api = client.CoreV1Api()
    body = client.V1Service(
        api_version="v1",
        kind="Service",
        metadata=client.V1ObjectMeta(
            name=name
        ),
        spec=client.V1ServiceSpec(
            type="NodePort",
            selector={"app": name},
            ports=[client.V1ServicePort(
                port=80,
                target_port=80,
                node_port=nodePort
            )]
        )
    )
    
    return core_v1_api.create_namespaced_service(namespace=namespace, body=body)


def delete_service(name, namespace="default"):
    config.load_kube_config()
    core_v1_api = client.CoreV1Api()
    
    return core_v1_api.delete_namespaced_service(namespace=namespace, name=name)


def create_deployment(name, image, image_pull_policy="Never", namespace="default"):
    core_v1_api = client.AppsV1Api()
    body = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(
            name=name
        ),
        spec=client.V1DeploymentSpec(replicas=1,
                                     selector=client.V1LabelSelector(
                                         match_labels={"app": name}),
                                     template=client.V1PodTemplateSpec(metadata=client.V1ObjectMeta(labels={"app": name}),
                                                                       spec=client.V1PodSpec(containers=[client.V1Container(name=name,
                                                                                                                            image=image, image_pull_policy=image_pull_policy,
                                                                                                                            ports=[client.V1ContainerPort(
                                                                                                                                container_port=80)]
                                                                                                                            )]
                                                                                             )
                                                                       )

                                     )
    )
    
    return core_v1_api.create_namespaced_deployment(namespace=namespace, body=body)


def delete_deployment(name, namespace="default"):
    core_v1_api = client.AppsV1Api()
    return core_v1_api.delete_namespaced_deployment(name=name, namespace=namespace)


t = delete_service('svc')
print(t.metadata.name)
