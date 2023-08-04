■前提
・本ツールは環境にある全リソースのエビデンス取得する。
※ネットワークのみVPCをフィルタリングするが、他は全リソースが対象となる
・ファイル名が[get_evi_～.py]のものが呼び出し用ファイルで、[aws_infra_ut_module.py]に関数が定義されている
・リージョンはCloudshell環境に依存する


■手順
1. 対象のリージョンでCloudChellを起動する
2. get_evi.zipをアップロードする
3. get_evi.zipを展開する
	unzipi get_evi.zip
4. ディレクトリに移動する
	cd get_evi
5. エビデンスを取得したいリソースのファイル(get_evi_で始まるファイル)をpython3（※注）で実行する
	python3 get_evi_nw.py  ## ネットワークのエビデンスが取得したい場合
	※全リソースを取得したい場合は[get_evi_all.py]を実行する

	※注)pythonだとこけます。python3を使用してください。

6.プロンプトが返ると取得完了し、eviディレクトリ内にエビデンスが格納されていることを確認する

	※注)Cloudsellのセッション（20 分 — 30 分）が切れるとプログラムが強制終了されるので注意！！たまにみてアクティブにすること！


7. 作業が完了したら、eviディレクトリ内のファイルを圧縮してダウンロードする
	zip {ファイル名} evi/*


■エビデンス取得コマンド
▼EC2
aws ec2 describe-vpcs --vpc-ids {VPC-ID} --profile名
aws ec2 describe-subnets --filters --profile名 Name=vpc-id,Values={VPC-ID}
aws ec2 describe-internet-gateways
aws ec2 describe-route-tables --filters Name=vpc-id,Values={VPC-ID}
aws ec2 describe-vpc-endpoints
aws ec2 describe-addresses
aws ec2 describe-vpc-peering-connections
aws ec2 describe-nat-gateways
aws ec2 describe-security-groups --filters Name=vpc-id,Values={VPC-ID}
aws ec2 describe-instances


▼Route53
aws route53 list-hosted-zones
aws route53 get-hosted-zone --id {HostZone-ID}
aws route53 list-resource-record-sets --hosted-zone-id {HostZone-ID}


▼IAM
aws iam list-roles
aws iam list-attached-role-policies --role-name {Role-Name}
aws iam list-role-policies --role-name {Role-Name}
aws iam list-policies


▼S3
aws s3api list-buckets
aws s3api get-bucket-accelerate-configuration --bucket {Bucket-Name}
aws s3api get-bucket-acl --bucket {Bucket-Name}
aws s3api get-bucket-cors --bucket {Bucket-Name}
aws s3api get-bucket-encryption --bucket {Bucket-Name}
aws s3api get-bucket-lifecycle-configuration --bucket {Bucket-Name}
aws s3api get-bucket-location --bucket {Bucket-Name}
aws s3api get-bucket-logging --bucket {Bucket-Name}
aws s3api get-bucket-notification-configuration --bucket {Bucket-Name}
aws s3api get-bucket-policy --bucket {Bucket-Name}
aws s3api get-bucket-replication --bucket {Bucket-Name}
aws s3api get-bucket-tagging --bucket {Bucket-Name}
aws s3api get-bucket-versioning --bucket {Bucket-Name}
aws s3api get-bucket-website --bucket {Bucket-Name}


▼ACMF(REGIONAL)
aws acm list-certificates
aws acm describe-certificate --certificate-arn {ACM-Arn}


▼ACMF(CloudFront)
aws acm list-certificates --region=us-east-1
aws acm describe-certificate --certificate-arn {ACM-Arn} --region=us-east-1


▼CloudWatchLogs
aws logs describe-log-groups


▼CloudTrail
aws cloudtrail describe-trails


▼APIGateway
aws apigateway get-rest-apis
aws apigateway get-resources --rest-api-id {API-ID}
aws apigateway get-gateway-responses --rest-api-id {API-ID}
aws apigateway get-stages --rest-api-id {API-ID}
aws apigateway get-domain-names
aws apigateway get-method --rest-api-id {API-ID} --resource-id {Resource-ID} --http-method {Method-Name}


▼ELB
aws elbv2 describe-load-balancers
aws elbv2 describe-target-groups
aws elbv2 describe-listeners --load-balancer-arn {ELB-Arn}


▼ECR
aws ecr describe-repositories


▼ECS
aws ecs list-clusters
aws ecs describe-clusters --cluster {Cluster-Name}
aws ecs list-task-definitions
aws ecs describe-task-definition --task-definition {TaskDefinition-Name}
aws ecs list-services --cluster {Cluster-Name}
aws ecs describe-services --cluster {Cluster-Name} --services {Service-Name}


▼Lambda
aws lambda list-functions


▼EventBrigde
aws events list-rules
aws events describe-rule --name {Rule-Name}


▼RDS
aws rds describe-db-clusters
aws rds describe-db-instances
aws rds describe-db-subnet-groups
aws rds describe-option-groups
aws rds describe-db-parameters --db-parameter-group-name {ParameterGroup-Name}
aws rds describe-db-cluster-parameters --db-cluster-parameter-group-name {ClusterParameterGroup-Name}
aws rds describe-db-proxies


▼DynamoDB
aws dynamodb list-tables
aws dynamodb describe-table --table-name {Table-Name}


▼ParameterStore
aws ssm describe-parameters
aws ssm get-parameter --name {Parameter-Name}


▼SecretManager
aws secretsmanager list-secrets
aws secretsmanager get-secret-value --secret-id {Secret-Name}


▼AutoScaling
aws autoscaling describe-auto-scaling-groups
aws autoscaling describe-auto-scaling-instances


▼ElastiCashe
aws elasticache describe-cache-subnet-groups
aws elasticache describe-cache-clusters
aws elasticache describe-cache-parameters --cache-parameter-group-name {PrameterGroup-Name}


▼WAF(REGIONAL)
aws wafv2 list-web-acls --scope REGIONAL
aws wafv2 get-web-acl --scope REGIONAL --name {WAF-Name} --id {WAF-ID}


▼WAF(CloudFront)
aws wafv2 list-web-acls --scope=CLOUDFRONT --region=us-east-1
aws wafv2 get-web-acl --scope=CLOUDFRONT --region=us-east-1 --name {WAF-Name} --id {WAF-ID}


▼CloudFront
aws cloudfront list-distributions


▼Firehose(REGIONAL)
aws firehose list-delivery-streams
aws firehose describe-delivery-stream --delivery-stream-name {Firehose_Name}


▼Firehose(CloudFront)
aws firehose list-delivery-streams --region=us-east-1
aws firehose describe-delivery-stream --delivery-stream-name {Firehose_Name} --region=us-east-1