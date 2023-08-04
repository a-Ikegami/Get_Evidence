from support.aws_infra_ut_module import get_evi_path, get_evi, write_evi_loop
import json
import os


def main():
    get_evi("iam_role_list")
    get_evi("iam_policy_list")

    role_list = get_role_list()
    policy_list = get_policy_list()

    write_evi_loop("iam_role", role_list)
    write_evi_loop("iam_policy", policy_list)
    write_evi_loop("iam_role_attached", role_list)


def get_role_list():
    file_path = get_evi_path("iam_role_list")

    # もし空なら空を返す
    if os.stat(file_path).st_size == 0:
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        list = json.load(f)
        return list


def get_policy_list():
    file_path = get_evi_path("iam_policy_list")

    # もし空なら空を返す
    if os.stat(file_path).st_size == 0:
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        list = json.load(f)
        return list


if __name__ == "__main__":
    main()
