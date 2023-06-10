import pickle

fId = open(r'D:\Projekte\StudiMaus\BcThesis_RL-Agent\GIT-Repo\Github_StudiMaus\schlably\BcThesis_MARL-Solution-main\data\instances\fjssp\config_job8_task2_tools0.pkl', 'rb')
genedData = pickle.load(fId)
print (f"Num of Instances {len(genedData)}")

idx = 0
print(f"Instance\tTask\tJob\tMachines\tTools"
      f"\tdeadline\tdone\truntime"
      f"\tstarted\tfinished\tselected_machine"
      )
for instance in genedData:
    for myTask in instance:
        # print(myTask.str_info())
        print(f"{idx}\t{myTask.task_index}\t{myTask.job_index}\t{str(myTask.machines)}\t{str(myTask.tools)}"
              f"\t{myTask.deadline}\t{str(myTask.done)}\t{str(myTask.runtime)}"
              f"\t{myTask.started}\t{str(myTask.finished)}\t{str(myTask.selected_machine)}"
              )
    idx += 1
    if idx > 1:
        break

