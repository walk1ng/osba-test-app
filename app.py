from flask import Flask, render_template, jsonify
import os
import redis
import json

app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

# Get services
if 'VCAP_SERVICES' in os.environ:
    services = json.loads(os.getenv('VCAP_SERVICES'))
else:
    services = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mysql-test')
def test_mysql():
    data = {'service_name':'mysql', 'bind':'null'}
    if services:
        mysql_services = services.get('azure-mysqldb', None)
        if mysql_services:
            data['bind'] = mysql_services[0]
    return jsonify(data)


@app.route('/postgres-test')
def test_postgres():
    data = {'service_name':'postgres', 'bind':'null'}
    if services:
        postgres_services = services.get('azure-postgresqldb', None)
        if postgres_services:
            data['bind'] = postgres_services[0]
    return jsonify(data)


@app.route('/sql-test')
def test_sql():
    data = {'service_name':'sql', 'bind':'null'}
    if services:
        sql_services = services.get('azure-sqldb', None)
        if sql_services:
            data['bind'] = sql_services[0]
    return jsonify(data)

 
if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
