from support.aws_infra_ut_module import get_evi, get_arg, write_evi_loop


def main():
    get_evi("event_list")
    write_evi_loop("event", get_arg("event_list"))


if __name__ == "__main__":
    main()
