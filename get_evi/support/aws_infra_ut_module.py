# coding: UTF-8
import subprocess
import json
import logging
import datetime
import time
import global_value as g
import commands
import os
from tqdm import tqdm
from io import TextIOWrapper


commands_class = commands.Commands()


def write_log(command: list):
    today = datetime.date.today()
    log_file_path = "log/" + str(today) + "_log.txt"
    logging.basicConfig(filename=log_file_path, encoding="utf-8", level=logging.DEBUG)
    logging.debug(command)


def get_evi(file_name: str):
    """eviフォルダ内にエビデンスを出力する

    Args:
        file_name(string): ファイル名
        command(list): エビデンス取得コマンドリスト
    """

    tqdm.write(file_name + "のエビデンス取得コマンドを実行します。")

    filepath = get_evi_path(file_name)
    command = get_base_command(file_name)

    # 実行前にファイルを削除する
    if os.path.isfile(filepath):
        os.remove(filepath)

    # 特定のコマンドでは、追加の引数を当てる。
    if file_name == "vpc":
        command.append(g.vpc_id)
    elif file_name == "subnet":
        command.append("Name=vpc-id,Values=" + g.vpc_id)
    elif file_name == "route_table":
        command.append("Name=vpc-id,Values=" + g.vpc_id)
    elif file_name == "security_group":
        command.append("Name=vpc-id,Values=" + g.vpc_id)
    elif file_name == "efs":
        command.append(g.region)
    elif file_name == "sqs_list":
        command.append(g.prefix)
    elif file_name == "parameterstore_list":
        idx = command.index("--parameter-filters")
        command[idx + 1] = command[idx + 1].format(g.parameterstore_prefix)

    # --queryにより絞り込みにおいて、検索値を置換する。
    elif "--query" in command:
        idx = command.index("--query")

        if file_name == "kms_aliases":
            command[idx + 1] = command[idx + 1].format("alias/" + g.prefix)
        else:
            command[idx + 1] = command[idx + 1].format(g.prefix)

    write_log(command)
    result = subprocess.run(command, capture_output=True, text=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(result.stdout))


def get_evi_path(file_name: str) -> str:
    """対象のエビデンスファイルパスを生成します
    Args:
        file_name(string)
    """

    return "evi/" + file_name + ".txt"


def get_base_command(file_name: str) -> list:
    return commands_class.get(file_name)


def write_evi_loop(file_name: str, target_list: list):
    tqdm.write(file_name + "のエビデンス取得コマンドを実行します。")
    tqdm.write("抽出するリストは" + str(len(target_list)) + "件です。")

    # もし空なら終了する
    if (len(target_list)) == 0:
        return

    file_path = get_evi_path(file_name)
    base_command = get_base_command(file_name)

    # 実行前にファイルを削除する
    if os.path.isfile(file_path):
        os.remove(file_path)

    with open(file_path, "a", encoding="utf-8") as f:
        for i, target in enumerate(target_list):
            tqdm.write(str(i + 1) + "件目の取得コマンドを実行中...")
            command = base_command + []

            # 特定のコマンドでは、ヘッダーの出力を指定する
            if file_name == "kms_describe" or file_name == "kms_policy":
                header = target["AliasName"]
            elif file_name == "iam_policy":
                header = target["PolicyName"]
            else:
                header = target

            # 特定のコマンドでは、追加の引数を当てる。
            if file_name == "waf_acl_regional" or file_name == "waf_acl_cloudfront":
                command.insert(-1, target[0])
                command.append(target[1])
            elif file_name == "kms_describe" or file_name == "kms_policy":
                command.append(target["TargetKeyId"])
            elif file_name == "iam_policy":
                command.append(target["Arn"])
            else:
                command.append(target)

            write_log(command)
            result = subprocess.run(command, capture_output=True, text=True)

            f.write(
                "#===============================================================================\n"
            )
            f.write("# " + header + "\n")
            f.write(
                "#===============================================================================\n"
            )
            f.write(str(result.stdout))

            # iam_policyの動作中にポリシーの中身を取得するため、下記の動作が入る。
            if file_name == "iam_policy":
                get_iam_policy_version(f, file_name, result)


def get_iam_policy_version(f: TextIOWrapper, file_name: str, policy_result):
    tmp_file_path = get_evi_path("tmp_" + file_name)

    with open(tmp_file_path, "a", encoding="utf-8") as tmp:
        tmp.write(str(policy_result.stdout))

    policy_data = []
    with open(tmp_file_path, "r", encoding="utf-8") as tmp:
        data = json.load(tmp)
        policy_data = data["Policy"]

    policy_arn = policy_data["Arn"]
    policy_version = policy_data["DefaultVersionId"]
    command = get_base_command("iam_policy_version") + []

    policy_arn_index = command.index("--policy-arn")
    command.insert(policy_arn_index + 1, policy_arn)

    policy_version_index = command.index("--version-id")
    command.insert(policy_version_index + 1, policy_version)

    write_log(command)
    result = subprocess.run(command, capture_output=True, text=True)
    f.write("\n")
    f.write(str(result.stdout))

    os.remove(tmp_file_path)


# ファイルから引数を取得
def get_arg(list_file):
    """
    エビデンス取得コマンドで引数が必要な場合、出力ファイルから引数を取得してリストで返す
    """
    filepath = "evi/" + list_file + ".txt"
    # json_open = open(filepath, 'r', encoding="utf-8")
    # json_load = json.load(json_open)

    # もし空なら空を返す
    if os.stat(filepath).st_size == 0:
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        json_load = json.load(f)
        if list_file == "elb":
            arn = []
            for v in json_load.values():
                for l in v:
                    arn.append(l["LoadBalancerArn"])
            return arn
        elif list_file == "dynamodb_list":
            for v in json_load.values():
                return v
        elif list_file == "route53_list":
            id = []
            for v in json_load.values():
                for l in v:
                    id.append(l["Id"].split("/")[2])
            return id
        elif list_file == "apigw_list":
            id = []
            for v in json_load.values():
                for l in v:
                    id.append(l["id"])
            return id
        elif list_file == "acm_list_regional" or list_file == "acm_list_cloudfront":
            arn = []
            for v in json_load.values():
                for l in v:
                    arn.append(l["CertificateArn"])
            return arn
        elif list_file == "event_list":
            name = []
            for v in json_load.values():
                for l in v:
                    name.append(l["Name"])
            return name
        elif list_file == "parameterstore_list":
            name = []
            for v in json_load.values():
                for l in v:
                    name.append(l["Name"])
            return name
        elif list_file == "secretmanager_list":
            name = []
            for v in json_load.values():
                for l in v:
                    name.append(l["Name"])
            return name
        elif list_file == "elasticache_cluster":
            name = []
            for v in json_load.values():
                for l in v:
                    a = l["CacheParameterGroup"]["CacheParameterGroupName"]
                    name.append(a)
            return name
        elif list_file == "waf_list_regional" or list_file == "waf_list_cloudfront":
            l = []
            name = []
            for v in json_load.values():
                l.append(v)
            for n in l[1]:
                waf = n["Name"], n["Id"]
                name.append(waf)
            return name
        elif (
            list_file == "firehose_list_regional"
            or list_file == "firehose_list_cloudfront"
        ):
            l = []
            name = []
            for v in json_load.values():
                l.append(v)
            for n in l[0]:
                name.append(n)
            return name


# API Gateway method
def get_evi_apigw_method(rname, arg_list):
    """
    APIGatewayメソッド用のエビデンス取得コマンドをリスト化
    arg_listはAPI-ID
    tmpファイルからAPIに登録されているメソッドID（arg2）とメソッド名（arg3）を取得
    API-UD（arg）とメソッドID（arg2）とメソッド名（arg3からエビデンス取得コマンドをリスト化
    セパレートの記載方法がこのCLIのみのため共通化はしない
    """
    filepath = get_evi_path(rname)
    # TODO: apigw_resourceファイルを利用させる
    for arg in arg_list:
        argument = ["aws", "apigateway", "get-resources", "--rest-api-id"]
        argument.append(arg)
        write_log(command)
        result = subprocess.run(argument, capture_output=True, text=True)
        with open("tmp.txt", "w", encoding="utf-8") as f:
            f.write(str(result.stdout))

        id = []
        method = []
        with open("tmp.txt", "r") as f:
            json_load = json.load(f)
            for v in json_load.values():
                for l in v:
                    try:
                        dict = l["resourceMethods"]
                        for k in dict.keys():
                            method.append(k)
                            id.append(l["id"])
                    except KeyError:
                        pass
            for arg2, arg3 in zip(id, method):
                argument = [
                    "aws",
                    "apigateway",
                    "get-method",
                    "--rest-api-id",
                    arg,
                    "--resource-id",
                    arg2,
                    "--http-method",
                    arg3,
                ]
                write_log(command)
                result = subprocess.run(argument, capture_output=True, text=True)
                with open(filepath, "a", encoding="utf-8") as f:
                    f.write(
                        "#===============================================================================\n"
                    )
                    f.write("# " + arg + "/" + arg2 + "\n")
                    f.write(
                        "#===============================================================================\n"
                    )
                    f.write(str(result.stdout))
                time.sleep(0.01)


def get_evi_ecs_service(file_name, cluster_list):
    """ECSサービス用のエビデンス取得コマンドをリスト化

    Args:
        file_name(string): ファイル名
        cluster_list(list): クラスターのリスト

    tmpファイルからクラスターに登録されているサービス名（service_list）を取得
    クラスター名（cluster_name）とサービス名（service_name）からエビデンス取得コマンドをリスト化
    """

    tqdm.write("ECSサービス用のエビデンス取得コマンドを実行します。")
    tqdm.write("抽出するクラスターは" + str(len(cluster_list)) + "件です。")

    file_path = get_evi_path(file_name)

    # 実行前にファイルを削除する
    if os.path.isfile(file_path):
        os.remove(file_path)

    with open(file_path, "a", encoding="utf-8") as f:
        for i, cluster_name in enumerate(cluster_list):
            tqdm.write(str(i + 1) + "件目の取得コマンドを実行中...")

            # クラスターに登録されているARNを取得
            command = ["aws", "ecs", "list-services", "--cluster", cluster_name]
            write_log(command)
            result = subprocess.run(command, capture_output=True, text=True)
            serviceArns_json = result.stdout
            serviceArns_data = json.loads(serviceArns_json)

            # APIの取得値からサービス名を特定
            service_list = []
            for service_arn in serviceArns_data["serviceArns"]:
                # example:
                # service_arn: arn/cluster_name/service_name
                elements = service_arn.split("/")
                service_list.append(elements[2])

            # 特定したサービスの詳細情報を取得する。
            for service_name in service_list:
                command = [
                    "aws",
                    "ecs",
                    "describe-services",
                    "--cluster",
                    cluster_name,
                    "--services",
                    service_name,
                ]
                write_log(command)
                result = subprocess.run(command, capture_output=True, text=True)

                f.write(
                    "#===============================================================================\n"
                )
                f.write("# " + service_name + "\n")
                f.write(
                    "#===============================================================================\n"
                )
                f.write(str(result.stdout))
