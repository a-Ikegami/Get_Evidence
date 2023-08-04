from support.aws_infra_ut_module import get_evi_path, get_evi, write_evi_loop
import json
import os


def main():
    get_evi("kms_aliases")

    kms_list = get_aliases()
    write_evi_loop("kms_describe", kms_list)
    write_evi_loop("kms_policy", kms_list)


def get_aliases():
    file_path = get_evi_path("kms_aliases")

    # もし空なら空を返す
    if os.stat(file_path).st_size == 0:
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        kms_list = json.load(f)
        return kms_list


if __name__ == "__main__":
    main()
