import numpy as np
import matplotlib.pyplot as plt
total_time = 1000
unit_time = 1
utility_all = []
for tag_count in range(1,6000,50):
    utility = []
    for x in range(20):
        msg_count_per_tag = 1
        time_seq_all = []
        time_seq_all = np.sort(np.random.randint(0,total_time,size=tag_count*msg_count_per_tag))
#         plt.bar(time_seq_all,1,width=unit_time)
#         plt.grid(b=True,axis="x")
#         plt.xlim(0,total_time)
#         plt.show()
        collide_count = 0
        i = 0
        j = i + 1
        flag = False
        while j < len(time_seq_all):
            while j < len(time_seq_all) and time_seq_all[j] == time_seq_all[i] :
                j += 1
                collide_count += 1
                flag = True
            if flag:
                collide_count += 1
                flag = False
            i = j
            j = i+1
        collide_probility = collide_count*1.0/tag_count
        us = (tag_count - collide_count)*unit_time*1.0/total_time
#         print(time_seq_all)
#         print("collide_count: {}, tag_count: {},probability: {}".format(collide_count,tag_count,collide_probility))
#         print("usage:", us)
        utility.append(us)
#     print(utility)
    print(sum(utility)/len(utility))
    utility_all.append(sum(utility)/len(utility))
print(utility_all)
plt.plot(range(1,6000,50),utility_all)
plt.grid(b=True,axis="x")
plt.grid(b=True,axis="y")
plt.show()