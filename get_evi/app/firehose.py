from support.aws_infra_ut_module import get_evi, write_evi_loop, get_arg


def main():
    get_evi("firehose_list_regional")
    write_evi_loop("firehose_regional", get_arg("firehose_list_regional"))


if __name__ == "__main__":
    main()
