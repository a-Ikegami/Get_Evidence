from support.aws_infra_ut_module import get_evi, get_arg, write_evi_loop


def main():
    get_evi("route53_list")
    write_evi_loop("route53", get_arg("route53_list"))
    write_evi_loop("route53_record", get_arg("route53_list"))


if __name__ == "__main__":
    main()
