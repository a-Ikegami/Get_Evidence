from support.aws_infra_ut_module import get_evi, get_arg, write_evi_loop, get_evi_path
import json
import os


def main():
    get_evi("s3_list")

    buckets_list = get_list()

    write_evi_loop("s3_acl", buckets_list)
    write_evi_loop("s3_accelerate", buckets_list)
    write_evi_loop("s3_cors", buckets_list)
    write_evi_loop("s3_encryption", buckets_list)
    write_evi_loop("s3_lifecycle", buckets_list)
    write_evi_loop("s3_location", buckets_list)
    write_evi_loop("s3_logging", buckets_list)
    write_evi_loop("s3_notification", buckets_list)
    write_evi_loop("s3_policy", buckets_list)
    write_evi_loop("s3_replication", buckets_list)
    write_evi_loop("s3_tagging", buckets_list)
    write_evi_loop("s3_versioning", buckets_list)
    write_evi_loop("s3_website", buckets_list)


def get_list():
    file_path = get_evi_path("s3_list")

    # もし空なら空を返す
    if os.stat(file_path).st_size == 0:
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        buckets_list = json.load(f)
        return buckets_list


if __name__ == "__main__":
    main()
