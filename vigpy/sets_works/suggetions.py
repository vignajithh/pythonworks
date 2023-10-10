all_users=["sachin","rahul","rohit","kholi","dravid","laxman","ganguly"]

sachin_followers=["rahul","ganguly","dravid"]

sachin_su=set(all_users).difference(set(sachin_followers))
sachin_su.remove("sachin")
print(sachin_su)
