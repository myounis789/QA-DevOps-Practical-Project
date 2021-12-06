#!/bin/bash
declare -a directories=("Service1" "Service2" "Service3" "Service4")
for dir in "${directories[@]}"
do
  cd ${dir}
  sudo apt-get update
  sudo apt-get install python3 python3-pip python3-venv
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r ../test_requirements.txt
  python3 -m pytest --cov=app --cov-report xml --cov-report term-missing --junitxml junit.xml
  deactivate
  cd ..
done