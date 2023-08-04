from support.aws_infra_ut_module import get_evi, write_evi_loop, get_arg


def main():
    get_evi("acm_list_regional")
    write_evi_loop("acm_regional", get_arg("acm_list_regional"))


if __name__ == "__main__":
    main()
