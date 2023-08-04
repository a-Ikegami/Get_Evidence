from support.aws_infra_ut_module import get_evi, write_evi_loop, get_arg


def main():
    get_evi("parameterstore_list")
    write_evi_loop("parameterstore", get_arg("parameterstore_list"))


if __name__ == "__main__":
    main()
