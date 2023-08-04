from support.aws_infra_ut_module import get_evi


def main():
    get_evi("autoscaling_group")
    get_evi("autoscaling_instance")


if __name__ == "__main__":
    main()
