#!/bin/bash

export dir=`pwd`
python -V
virtualenv $dir/venv 
source     $dir/venv/bin/activate
pip install -r ./requeriments.txt
pip list
deactivate
