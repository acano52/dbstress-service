#!/bin/bash

export dir=`pwd`
python -V
#sudo apt-get install python-dev 
#                     build-essential 
#                     libssl-dev 
#                     libffi-dev
#                     libxml2-dev 
#                     libxslt1-dev 
#                     zlib1g-dev
#                     python-pip


# Virtual environment needs to be created using python 2.7
#scl enable python27 bash << eof
python -V
virtualenv $dir/venv 
source     $dir/venv/bin/activate
pip install mysql-connector
pip install flask flask-jsonpify flask-sqlalchemy flask-restful flask_api
pip install pyyaml
#pip install mysql-python
#pip install flask_mysqldb
pip install flask_mysqlpool
pip install flask_caching
pip list

deactivate
#eof
