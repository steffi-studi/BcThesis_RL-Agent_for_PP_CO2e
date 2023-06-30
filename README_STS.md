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
`<torch.cuda.device object at 0x0000024AB8264D00>`<br>
`>>> torch.cuda.get_device_name(0)`<br>
`'GeForce GTX 1050'`<br>


## Start data_generator
python -m src.data_generator.instance_factory -fp data_generation/fjssp/pyconfig_job8_task2_tools0.yaml

## Start training
python -m src.agents.train -fp training/dqn/config_job8_task2_tools0.yaml

## Analyse generated data

`python`<br>
`import pickle`<br>
`fId = open(r'D:\Projekte\StudiMaus\BcThesis_RL-Agent\GIT-Repo\Github_StudiMaus\schlably\BcThesis_MARL-Solution-main\data\instances\fjssp\config_job8_task2_tools0.pkl', 'rb')`<br>
`genedData = pickle.load(fId)`<br>
`firstTask = genedData[0][0]`<br>
``<br>
``<br>
``<br>
``<br>
``<br>
``<br>
``<br>
``<br>

## co2_timesteps - Angaben in CO2-Verbrauch pro kWh
*******************************************************************************
erste Testreihe
[[6, 90], [18, 30], [24, 60]]
*******************************************************************************
über 2 Tage - in 48 Timesteps (24 timesteps pro Tag)  mit schlecht Wetter                                                    
[[5, 495.6], [8, 366.5], [12, 279.4],[18, 549.7],[24, 621.3],[29, 645.8],[33, 465.1],[37, 366.4],[42, 617.3],[48, 723.4]]
*******************************************************************************
über 2 Tage - in 48 Timesteps (24 timesteps pro Tag)  nur mit Sonnenenschein                                                   
[[5, 495.6], [8, 366.5], [12, 199.2],[18, 290.7],[24, 621.3],[29, 645.8],[33, 329.1],[37, 232.4],[42, 289.3],[48, 723.4]]
*******************************************************************************