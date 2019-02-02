#  In python3.x, dict.values() doesn't return a list anymore -- it returns a dict_values object. 

week_days = {'M': 'Monday', 'Tu': 'Tuesday', 'W': 'Wednesday', 'Th': 'Thursday', 'F': 'Friday', 'Sa': 'Saturday', 'Su': 'Sunday'}

print(week_days['M'])
print(len(week_days))

print(week_days) # different value for every time
print(week_days.keys()) # different value for every time
print(week_days.values()) # different value for every time

# new_dic = {}
# for i in week_days.keys():
#     print(i)
#     if i == 'Sa':
#         break
#     new_dic = {i : i in week_days}
# print(new_dic)

work_days = {k : week_days[k] for k in ('M', 'Tu', 'W', 'Th', 'F')}
print('Work days', work_days)

weekend = {k : week_days[k] for k in ('Sa', 'Su')}
print('Weekend: ', weekend)