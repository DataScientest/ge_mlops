ludwig train --config rotten_tomatoes.yml --dataset rotten_tomatoes.csv
ludwig predict --model_path results/experiment_run/model --dataset rotten_tomatoes.csv
