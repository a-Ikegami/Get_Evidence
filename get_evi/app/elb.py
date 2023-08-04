from support.aws_infra_ut_module import get_evi, write_evi_loop, get_arg


def main():
    get_evi("elb")
    get_evi("elb_target_group")
    write_evi_loop("elb_listener", get_arg("elb"))


if __name__ == "__main__":
    main()
