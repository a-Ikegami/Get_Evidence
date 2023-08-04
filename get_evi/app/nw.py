from support.aws_infra_ut_module import get_evi


def main():
    get_evi("vpc")
    get_evi("subnet")
    get_evi("igw")
    get_evi("route_table")
    get_evi("endopoint")
    get_evi("eip")
    get_evi("vpc_peering")
    get_evi("natgw")
    get_evi("security_group")
    get_evi("vpc_flowlog")


if __name__ == "__main__":
    main()
