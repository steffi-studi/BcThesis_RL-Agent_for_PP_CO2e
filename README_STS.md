[Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)


# BcThesis_MARL-Solution

Verwendung von Framework SCHLABLY https://github.com/tmdt-buw/schlably <br>
pip install -r requirements.txt

Link zu einer ausführlicheren Beschreibung 
https://schlably.readthedocs.io/en/latest/installation.html

wandb für Darstellung des Trainingslaufs
wandb angemeldet mit Github und HfT-Name 0125251bif
Zugangscode: 60c59a0aed79e3c741c386bcbd8f1bce934e0700


## Check ob torch CUDA verwendet

`>>> import torch`<br>
`>>> torch.cuda.is_available()`<br>
`True`<br>
`>>> torch.cuda.device_count()`<br>
`1`<br>
`>>> torch.cuda.current_device()`<br>
`0`<br>
`>>> torch.cuda.device(0)`<br>
`<torch.cuda.device object at 0x0000016DFC61FA60>`<br>
`>>> torch.cuda.get_device_name(0)`<br>
`'NVIDIA GeForce RTX 3070 Laptop GPU'`<br>


## Start data_generator
python -m src.data_generator.instance_factory -fp data_generation/fjssp/config_job8_task2_tools0.yaml

## Start training
python -m src.agents.train -fp training/dqn/config_job8_task2_tools0.yaml