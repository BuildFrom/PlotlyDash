# =================================
# General
# =================================

PYTHON_VERSION    := 3.11
JUPYTER_PORT      := 8888
PLOTLY_DASH_PORT  := 9000

# =================================
# Data Science Related Setup 
# =================================

path:
	python3 -m venv env
	source env/bin/activate

https:
	pip3 install certifi
	"/Applications/Python ${PYTHON_VERSION}/Install Certificates.command"

# =================================
# Python Dependencies
# =================================
	
i:
	pip install pip-tools
	pip-compile --strip-extras requirements.piptools

req: # OR
	pip3 install -r requirements.txt

# =================================
# Commands
# =================================

runj:
	lsof -i :${JUPYTER_PORT} | awk 'NR!=1 {print $$2}' | xargs -r kill -9
	jupyter lab

rund:
	lsof -i :${PLOTLY_DASH_PORT} | awk 'NR!=1 {print $$2}' | xargs -r kill -9
	python3 run.py