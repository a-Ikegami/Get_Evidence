from support.aws_infra_ut_module import get_evi, write_evi_loop, get_arg


def main():
    get_evi("acm_list_cloudfront")
    write_evi_loop("acm_cloudfront", get_arg("acm_list_cloudfront"))


if __name__ == "__main__":
    main()
