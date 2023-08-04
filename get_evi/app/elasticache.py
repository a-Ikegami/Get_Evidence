from support.aws_infra_ut_module import get_arg, get_evi, write_evi_loop


def main():
    get_evi("elasticache_subnet")
    get_evi("elasticache_cluster")
    write_evi_loop("elasticache_parametergroup", get_arg("elasticache_cluster"))


if __name__ == "__main__":
    main()
