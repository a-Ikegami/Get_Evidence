from support.aws_infra_ut_module import get_evi


def main():
    get_evi("ec2")
    get_evi("ec2_launch_template")


if __name__ == "__main__":
    main()
