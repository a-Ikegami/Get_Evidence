from support.aws_infra_ut_module import get_evi, write_evi_loop, get_arg


def main():
    get_evi("waf_list_cloudfront")
    write_evi_loop("waf_acl_cloudfront", get_arg("waf_list_cloudfront"))


if __name__ == "__main__":
    main()
