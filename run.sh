
#!bin/bash
#chmod u+x run.sh


echo "Run."

python -B main.py

./run_clean.sh -pyc

echo "End."