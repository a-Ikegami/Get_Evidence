from support.aws_infra_ut_module import get_evi, write_evi_loop, get_arg, get_evi_path
import json
import os


def main():
    get_evi("datasync_task_list")
    get_evi("datasync_location_s3_list")
    get_evi("datasync_location_efs_list")

    write_evi_loop("datasync_task", get_list("datasync_task_list"))
    write_evi_loop("datasync_location_s3", get_list("datasync_location_s3_list"))
    write_evi_loop("datasync_location_efs", get_list("datasync_location_efs_list"))


def get_list(file_name: str):
    file_path = get_evi_path(file_name)

    # もし空なら空を返す
    if os.stat(file_path).st_size == 0:
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        list = json.load(f)

    return list


if __name__ == "__main__":
    main()
