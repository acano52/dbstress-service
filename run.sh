#!/bin/bash
export dir=`pwd`

#scl enable python27 bash << eof
source     $dir/venv/bin/activate
python $dir/main.py
deactivate
#eof
