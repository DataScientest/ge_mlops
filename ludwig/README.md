# Ludwig Demo


This is a very very simple demo with Ludwig.

To use this demo, you can follow these steps:

```sh
cd ludwig

python3 -m venv venv
source venv/bin/activate
pip3 install ludwig
```

Once this is done, you can train your model by using: 

```sh
ludwig train --config rotten_tomatoes.yml --dataset rotten_tomatoes.csv
```

It should take about 5 minutes to run.

To make some predictions, we can do:

```sh
ludwig predict --model_path results/experiment_run/model --dataset rotten_tomatoes.csv
```