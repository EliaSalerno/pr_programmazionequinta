from python
env http_proxy=http://proxy:3128
env https_proxy=http://proxy:3128
run python3 -m pip install mysql-connector-python==8.0.29
run python3 -m pip install flask
copy . /
env http_proxy=
env https_proxy=
cmd python3 -m flask --app apiApp.py run --host 0.0.0.0
