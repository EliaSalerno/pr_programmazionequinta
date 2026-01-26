from python
env http_proxy=http://proxy:3128
env https_proxy=http://proxy:3128
run python3 -m pip install flask
run python3 -m pip install requests
copy . /
env http_proxy=
env https_proxy=
cmd python3 -m flask --app webApp.py run --host 0.0.0.0 --port 8000
