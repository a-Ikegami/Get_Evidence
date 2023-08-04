from support.aws_infra_ut_module import get_evi_path, get_evi, write_evi_loop
import json
import os


def main():
    get_evi("sqs_list")

    sqs_list = get_list()

    write_evi_loop("sqs_attributes", sqs_list)


def get_list():
    file_path = get_evi_path("sqs_list")

    # もし空なら空を返す
    if os.stat(file_path).st_size == 0:
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        sqs_list = json.load(f)
        return sqs_list


if __name__ == "__main__":
    main()
