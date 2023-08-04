from support.aws_infra_ut_module import get_evi, write_evi_loop, get_arg


def main():
    get_evi("dynamodb_list")
    write_evi_loop("dynamodb", get_arg("dynamodb_list"))


if __name__ == "__main__":
    main()
