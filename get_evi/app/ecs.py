from support.aws_infra_ut_module import (
    get_evi,
    write_evi_loop,
    get_evi_ecs_service,
    get_evi_path,
)
import json
import os


def main():
    get_evi("ecscl_list")
    get_evi("ecstk_list")

    cluster_list = get_cluster_list()
    task_list = get_task_list()
    # maximum_revision_list = get_maximum_revision_list()

    write_evi_loop("ecscl", cluster_list)
    write_evi_loop("ecstk", task_list)
    get_evi_ecs_service("ecs_service", cluster_list)


def get_cluster_list():
    file_path = get_evi_path("ecscl_list")

    # もし空なら空を返す
    if os.stat(file_path).st_size == 0:
        return []

    result = []

    with open(file_path, "r", encoding="utf-8") as f:
        cluster_arns = json.load(f)

        for cluster_arn in cluster_arns:
            # 前半が対象サービス、リージョン、アカウントIDなど
            # 後半がリソース
            cluster_arn_split = cluster_arn.split("/")
            scope = cluster_arn_split[0]
            resource_id = cluster_arn_split[1]

            result.append(resource_id)

    return result


def get_task_list():
    file_path = get_evi_path("ecstk_list")

    # もし空なら空を返す
    if os.stat(file_path).st_size == 0:
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        task_arns = json.load(f)
        return task_arns


# def get_maximum_revision_list():
#     file_path = get_evi_path("ecstk_list")

#     # もし空なら空を返す
#     if os.stat(file_path).st_size == 0:
#         return []

#     maximum_list = {}

#     with open(file_path, "r", encoding="utf-8") as f:
#         task_definition_arns = json.load(f)

#         # ここでソートすることで、必ず末端が最終revisionになる
#         task_definition_arns.sort()

#         for task_definition_arn in task_definition_arns:
#             # 前半が対象サービス、リージョン、アカウントIDなど
#             # 後半がリソース
#             arn = task_definition_arn.split("/")
#             scope = arn[0]
#             resource_id = arn[1]

#             # リソースの前半がfamily、後半がrevision
#             resource_split = resource_id.split(":")
#             family = resource_split[0]
#             revision = resource_split[1]

#             maximum_list[family] = resource_id

#     return [id for id in maximum_list.values()]


if __name__ == "__main__":
    main()
