echo "Downloading Cloud_SQL_Proxy..."
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
chmod +x cloud_sql_proxy
./cloud_sql_proxy -credential_file=churn_api/secrets/key.json
./cloud_sql_proxy -instances=yotta-square-ml3:europe-west1:group-2=tcp:5432