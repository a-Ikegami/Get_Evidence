from support.aws_infra_ut_module import get_evi, write_evi_loop, get_evi_path
import json
import os


def main():
    get_evi("rds_global_cluster")
    get_evi("rds_cluster")
    get_evi("rds_instance")
    get_evi("rds_subgrp")
    get_evi("rds_optiongroup")
    get_evi("rds_proxy")

    cluster_parametergroup_names = get_cluster_parametergroup_names()
    instance_parametergroup_names = get_instance_parametergroup_names()

    write_evi_loop("rds_cluster_parametergroup", cluster_parametergroup_names)
    write_evi_loop("rds_parametergroup", instance_parametergroup_names)


def get_cluster_parametergroup_names():
    file_path = get_evi_path("rds_cluster")

    # もし空なら空を返す
    if os.stat(file_path).st_size == 0:
        return []

    list = []

    with open(file_path, "r", encoding="utf-8") as f:
        items = json.load(f)

        for item in items:
            list.append(item["DBClusterParameterGroup"])

    return list


def get_instance_parametergroup_names():
    file_path = get_evi_path("rds_instance")

    # もし空なら空を返す
    if os.stat(file_path).st_size == 0:
        return []

    list = []

    with open(file_path, "r", encoding="utf-8") as f:
        items = json.load(f)

        for item in items:
            list.append(item["DBParameterGroups"][0]["DBParameterGroupName"])

    return list


if __name__ == "__main__":
    main()
