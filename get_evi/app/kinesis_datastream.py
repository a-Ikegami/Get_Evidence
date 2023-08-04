from support.aws_infra_ut_module import get_evi_path, get_evi, write_evi_loop
import json
import os


def main():
    get_evi("kinesis_datastream_list")

    stream_names = get_list()

    write_evi_loop("kinesis_datastream_describe", stream_names)


def get_list():
    file_path = get_evi_path("kinesis_datastream_list")

    # もし空なら空を返す
    if os.stat(file_path).st_size == 0:
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        stream_names = json.load(f)
        return stream_names


if __name__ == "__main__":
    main()
