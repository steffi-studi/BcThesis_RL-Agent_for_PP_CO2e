import pickle


fileP = r'D:\Projekte\StudiMaus\BcThesis_RL-Agent\GIT-Repo\Github_StudiMaus\schlably\BcThesis_MARL-Solution-main\data\instances\fjssp'
fileN = r'config_job8_task2_tools0'

fId = open(r'{}\{}.pkl'.format(fileP, fileN), 'rb')
genedData = pickle.load(fId)
print (f"Num of Instances {len(genedData)}")
fId.close()

fId = open(r'{}\{}.csv'.format(fileP, fileN), 'w')
idx = 0
fId.write(f"Instance\tTask\tJob\tMachines\tTools"
          f"\tdeadline\tdone\truntime"
          f"\tstarted\tfinished\tselected_machine"
          f"\n"
          )
for instance in genedData:
    for myTask in instance:
        # print(myTask.str_info())
        fId.write(f"{idx}\t{myTask.task_index}\t{myTask.job_index}\t{str(myTask.machines)}\t{str(myTask.tools)}"
                  f"\t{myTask.deadline}\t{str(myTask.done)}\t{str(myTask.runtime)}"
                  f"\t{myTask.started}\t{str(myTask.finished)}\t{str(myTask.selected_machine)}"
                  f"\n"
                  )
    idx += 1
#    if idx > 1:
#        break
fId.close()
