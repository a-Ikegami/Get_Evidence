from support.aws_infra_ut_module import (
    get_arg,
    get_evi,
    write_evi_loop,
    get_evi_apigw_method,
)


def main():
    get_evi("apigw_list")
    write_evi_loop("apigw_resource", get_arg("apigw_list"))
    write_evi_loop("apigw_responses", get_arg("apigw_list"))
    write_evi_loop("apigw_stage", get_arg("apigw_list"))
    get_evi("apigw_domain")
    get_evi_apigw_method("apigw_method", get_arg("apigw_list"))

    # get_evi('apigw_usageplan_list')
    # get_evi_api_usageplan_key('apigw_usageplan_key', get_arg('apigw_usageplan_list'))
    # get_evi('apigw_vpclink')


if __name__ == "__main__":
    main()
