
echo "" > cluster-parameters.txt
echo "#===============================================================================" >> cluster-parameters.txt
echo "# dev-24m-fr-navi-routeinfo-rdspg-sv01-cluster-v80" >> cluster-parameters.txt
echo "#===============================================================================" >> cluster-parameters.txt
aws-vault exec aisin-dev-24mm -- \
 aws rds describe-db-cluster-parameters \
 --db-cluster-parameter-group-name dev-24m-fr-navi-routeinfo-rdspg-sv01-cluster-v80 \
 >> cluster-parameters.txt


echo "#===============================================================================" >> cluster-parameters.txt
echo "# dev-24m-fr-navi-trafficmanage-rdspg-sv01-cluster-v80" >> cluster-parameters.txt
echo "#===============================================================================" >> cluster-parameters.txt
aws-vault exec aisin-dev-24mm -- \
 aws rds describe-db-cluster-parameters \
 --db-cluster-parameter-group-name dev-24m-fr-navi-trafficmanage-rdspg-sv01-cluster-v80 \
 >> cluster-parameters.txt


echo "" > db-parameters.txt
echo "#===============================================================================" >> db-parameters.txt
echo "# dev-24m-fr-navi-routeinfo-rdspg-sv01-v80" >> db-parameters.txt
echo "#===============================================================================" >> db-parameters.txt
aws-vault exec aisin-dev-24mm -- \
 aws rds describe-db-parameters \
 --db-parameter-group-name dev-24m-fr-navi-routeinfo-rdspg-sv01-v80 \
 >> db-parameters.txt


echo "#===============================================================================" >> db-parameters.txt
echo "# dev-24m-fr-navi-trafficmanage-rdspg-sv01-v80" >> db-parameters.txt
echo "#===============================================================================" >> db-parameters.txt
aws-vault exec aisin-dev-24mm -- \
 aws rds describe-db-parameters \
 --db-parameter-group-name dev-24m-fr-navi-trafficmanage-rdspg-sv01-v80 \
 >> db-parameters.txt
